from django.urls import reverse
from django_seed import Seed    # pip install django_seed

from .models import Employee, EmpDetails
from rest_framework.test import APITestCase

seeder = Seed.seeder()


class EmpDetailsTestCase(APITestCase):
    def test_list_EmpDetails(self):
        # Add dummy data to the Author and Book Table
        # seeder.add_entity(EmpDetails, 5)
        # seeder.add_entity(Employee, 5)
        # seeder.execute()
        # we expect the result in 1 query
        with self.assertNumQueries(1):
            # response = self.client.get(reverse("EmpDetails_list"), format="json")
            response = self.client.get(reverse("EmpDetails"), format="json")
