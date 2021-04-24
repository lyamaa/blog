from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from blog.models import Post, Category

class Test_create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="django")
        testuser1 = User.objects.create(username='test_user1', password='123456')
        test_post = Post.objects.create(title='post Title', excerpt='Post Blog', content='Blog Content', slug='blogger', status='published', category_id=1, author_id=1 )


    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content= f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'post Title')
        self.assertEqual(excerpt, 'Post Blog')
        self.assertEqual(content, 'Blog Content')
        self.assertEqual(str(cat), 'django')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "post Title")


class PostTests(APITestCase):
    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def create_post(self):
        self.test_category = Category.objects.create(name='django')

        self.testuser1  = User.objects.create_user(
            username='test_user1', password='123456'
        )

        data = {
            "title": "new",
            "author": 1,
            "excerpt": "new",
            "content": "new"
        }

        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_post_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')

        client.login(username=self.testuser1.username,
                     password='123456789')

        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "author": 1,
                "slug": "abcd",
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



