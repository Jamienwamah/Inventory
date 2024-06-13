from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Item
from .serializers import ItemSerializer


class ItemTests(APITestCase):

    def setUp(self):
        # Create some sample items to use in tests
        self.item1 = Item.objects.create(
            name="Item1", description="Description1", price=10.00)
        self.item2 = Item.objects.create(
            name="Item2", description="Description2", price=20.00)

    def test_get_all_items(self):
        """
        Ensure we can get a list of all items.
        """
        url = reverse('item_list')
        response = self.client.get(url)
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_item(self):
        """
        Ensure we can create a new item.
        """
        url = reverse('item_list')
        data = {'name': 'Item3', 
                'description': 'Description3', 'price': 30.00}
        response = self.client.post(
            url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Item.objects.count(), 3)
        self.assertEqual(
            Item.objects.get(id=3).name, 'Item3')

    def test_get_single_item(self):
        """
        Ensure we can get a single item by id.
        """
        url = reverse('item_detail', kwargs={'pk': self.item1.pk})
        response = self.client.get(url)
        item = Item.objects.get(
            pk=self.item1.pk)
        serializer = ItemSerializer(item)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, serializer.data)

    def test_update_item(self):
        """
        Ensure we can update an item.
        """
        url = reverse('item_detail',
                      kwargs={'pk': self.item1.pk})
        data = {'name': 'Updated Item', 
                'description': 'Updated Description', 'price': 15.00}
        response = self.client.put(
            url, data, format='json')
        self.item1.refresh_from_db()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.item1.name, 'Updated Item')
        self.assertEqual(
            self.item1.description, 'Updated Description')

    def test_delete_item(self):
        """
        Ensure we can delete an item.
        """
        url = reverse(
            'item_detail', kwargs={'pk': self.item1.pk})
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Item.objects.count(), 1)