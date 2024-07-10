from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from book.models import Book, BookReview
from user.models import CustomUser


class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="muhammadziyo", first_name="muhammadziyo")
        self.user.set_password("somepassword")
        self.user.save()
        self.client.login(username='muhammadziyo', password='somepassword')


    def test_book_review_details(self):
        book1 = Book.objects.create(title="Sport", desk="Description1", isbn="123121")
        br = BookReview.objects.create(book=book1, stars=5, user=self.user, comment='Very good book')

        response = self.client.get(reverse('api:review-detail', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['stars'], 5)
        self.assertEqual(response.data['comment'], 'Very good book')
        # print(response.data)
        self.assertEqual(response.data['user']['id'], 1)
        self.assertEqual(response.data['user']['username'], 'muhammadziyo')
        self.assertEqual(response.data['user']['first_name'], 'muhammadziyo')
        self.assertEqual(response.data['book']['id'], 1)
        self.assertEqual(response.data['book']['title'], 'Sport')
        self.assertEqual(response.data['book']['desk'], 'Description1')
        self.assertEqual(response.data['book']['isbn'], '123121')

    def test_book_review_list(self):
        user_two = CustomUser.objects.create(username="somebody", first_name="Somebody")
        book1 = Book.objects.create(title="Sport", desk="Description1", isbn="123121")
        br = BookReview.objects.create(book=book1, stars=5, user=self.user, comment='Very good book')
        br_two = BookReview.objects.create(book=book1, stars=2, user=user_two, comment='Not bad')

        response = self.client.get(reverse('api:review-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)

        # print(response.data)
        self.assertEqual(response.data['results'][1]['id'], br_two.id)
        self.assertEqual(response.data['results'][1]['stars'], br_two.stars)
        self.assertEqual(response.data['results'][1]['comment'], br_two.comment)
        self.assertEqual(response.data['results'][0]['id'], br.id)
        self.assertEqual(response.data['results'][0]['stars'], br.stars)
        self.assertEqual(response.data['results'][0]['comment'], br.comment)