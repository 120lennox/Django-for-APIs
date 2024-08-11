from django.test import TestCase
from .models import Todo

# Create your tests here.

#what to test?
'''
    we want to make sure that the title in our models is displaying texts as expected 
'''

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.todo = Todo.objects.create(
            title = "First todo",
            body = "Go to Gymn"
        )
        
    def test_model_content(self):
        self.assertEqual(self.todo.title, "First todo")
        self.assertEqual(self.todo.body, "Go to Gymn")
        self.assertEqual(str(self.todo), "First todo")

