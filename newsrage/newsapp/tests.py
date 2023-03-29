from django.test import TestCase
from .models import News, Comments
from django.contrib.auth.models import User


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


class CommentsModelTest(TestCase):
    def test_comments_model_save_and_retrieve(self):
        test_user = User.objects.create_user('myname')
        test_news = News.objects.create(title='post', content='post_content', slug='post_slug')

        comment1 = Comments(
            user=test_user,
            comment='comment1',
            news=test_news,
        )
        comment1.save()

        comment2 = Comments(
            user=test_user,
            comment='comment2',
            news=test_news,
        )
        comment2.save()

        all_comments = Comments.objects.all()

        self.assertEqual(
            len(all_comments), 2
        )

        self.assertEqual(
            all_comments[0].user,
            comment1.user
        )

        self.assertEqual(
            all_comments[0].comment,
            comment1.comment
        )

        self.assertEqual(
            all_comments[0].news,
            comment1.news
        )

        self.assertEqual(
            all_comments[1].user,
            comment2.user
        )

        self.assertEqual(
            all_comments[1].comment,
            comment2.comment
        )

        self.assertEqual(
            all_comments[1].news,
            comment2.news
        )
