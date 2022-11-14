from django.test import TestCase
from threeknightsapp.models import Exercise

# Create your tests here.



class PostTestCase(TestCase):
    def testExercise(self):
        exerc = Exercise(name="My Exercise1", points =3)
        self.assertEqual(exerc.name, "My Exercise1")
        self.assertEqual(exerc.points, 3)
        