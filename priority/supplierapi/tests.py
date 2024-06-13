from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Supplier
from .serializers import SupplierSerializer


class SupplierTests(APITestCase):

    def setUp(self):
        # Create some sample suppliers to use in tests
        self.supplier1 = Supplier.objects.create(
            name="Supplier1", contact_info="Contact Info 1")
        self.supplier2 = Supplier.objects.create(
            name="Supplier2", contact_info="Contact Info 2")

    def test_get_all_suppliers(self):
        """
        Ensure we can get a list of all suppliers.
        """
        url = reverse('supplier_list')
        response = self.client.get(url)
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_supplier(self):
        """
        Ensure we can create a new supplier.
        """
        url = reverse('supplier_list')
        data = {'name': 'Supplier3', 'contact_info': 'Contact Info 3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 3)
        self.assertEqual(Supplier.objects.get(id=3).name, 'Supplier3')

    def test_get_single_supplier(self):
        """
        Ensure we can get a single supplier by id.
        """
        url = reverse('supplier_detail', kwargs={'pk': self.supplier1.pk})
        response = self.client.get(url)
        supplier = Supplier.objects.get(pk=self.supplier1.pk)
        serializer = SupplierSerializer(supplier)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_supplier(self):
        """
        Ensure we can update a supplier.
        """
        url = reverse('supplier_detail', kwargs={'pk': self.supplier1.pk})
        data = {'name': 'Updated Supplier', 
                'contact_info': 'Updated Contact Info'}
        response = self.client.put(url, data, format='json')
        self.supplier1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.supplier1.name, 
                         'Updated Supplier')
        self.assertEqual(self.supplier1.contact_info, 
                         'Updated Contact Info')

    def test_delete_supplier(self):
        """
        Ensure we can delete a supplier.
        """
        url = reverse('supplier_detail', kwargs={'pk': self.supplier1.pk})
        response = self.client.delete(url)
        