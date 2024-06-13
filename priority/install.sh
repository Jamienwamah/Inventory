# To set up the project, follow these steps:
# Clone the Repository:
git clone https://github.com/Jamienwamah/Inventory.git
cd Inventory

# Create and Activate a Virtual Environment:
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Dependencies:
pip install -r requirements.txt

# Apply Migrations:
./manage.py makemigrations
./manage.py migrate

# Create a Superuser (optional):
./manage.py createsuperuser

# Running the Application
# To run the Django development server, execute:
./manage.py runserver

# Testing the API
# Using Django Test Framework
# To run the tests, use the following command:
./manage.py test

