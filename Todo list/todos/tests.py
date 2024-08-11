from django.test import TestCase
from .models import Todo

# Create your tests here.

# test 1
# #what to test?
# '''
#     we want to make sure that the title in our models is displaying texts as expected 
# '''

# class TodoModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         cls.todo = Todo.objects.create(
#             title = "First todo",
#             body = "Go to Gymn"
#         )
        
#     def test_model_content(self):
#         self.assertEqual(self.todo.title, "First todo")
#         self.assertEqual(self.todo.body, "Go to Gymn")
#         self.assertEqual(str(self.todo), "First todo")

#test 2
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title = "Todo title",
            body = "Todo body here"
        )
    
    def test_model_content(self):
        self.assertEqual(self.todo.title, "Todo title")
        self.assertEqual(self.todo.body, "Todo body here")
        self.assertEqual(Todo.objects.count(), 1)
    
    def test_api_list_view(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
    
    def test_api_detail_view(self):
        response = self.client.get(
            "todo_detail",
            kwargs={"pk": self.todo.id},
            format = "json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Todo title")

