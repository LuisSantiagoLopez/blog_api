from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post 


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com",password="password"
        )

        cls.post = Post.objects.create(
            author=cls.user, title="Blog title", body="Body content..."
        )

    def test_blog_content(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Blog title")
        self.assertEqual(self.post.body, "Body content...")
        self.assertEqual(str(self.post), "Blog title")