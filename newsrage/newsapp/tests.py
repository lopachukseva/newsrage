from django.test import TestCase
from .models import News


class NewsModelTest(TestCase):
    def test_news_model_save_and_retrieve(self):
        post1 = News(
            title='post1',
            content='post1_content',
            slug='post1_slug'
        )
        post1.save()

        post2 = News(
            title='post2',
            content='post2_content',
            slug='post2_slug'
        )
        post2.save()

        all_posts = News.objects.all()

        self.assertEqual(len(all_posts), 2)

        self.assertEqual(
            all_posts[0].title,
            post1.title
        )

        self.assertEqual(
            all_posts[0].content,
            post1.content
        )

        self.assertEqual(
            all_posts[0].slug,
            post1.slug
        )

        self.assertEqual(
            all_posts[1].title,
            post2.title
        )

        self.assertEqual(
            all_posts[1].content,
            post2.content
        )

        self.assertEqual(
            all_posts[1].slug,
            post2.slug
        )
