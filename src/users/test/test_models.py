from django.test import TestCase

from users.models import User


class TestUser(TestCase):
    

    def test_should_create_user(self):
        user = User.objects.create(
            username = 'Test1', 
            email = 'test1@gmail.com'
            
        )

        user.set_password(
            'Test123!'
        )

        user.save()

        self.assertEqual(str(user),user.username)