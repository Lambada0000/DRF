from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Ims.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@gmail.com")
        self.course = Course.objects.create(
            name="Алгебра",
            description="Интересный курс!",
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="Логарифм",
            description="Интересный урок!",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse("Ims:lesson_create")
        data = {
            "name": "lesson TEST",
            "description": "description TEST",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_retrieve(self):
        url = reverse("Ims:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_update(self):
        url = reverse("Ims:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "New lesson TEST",
            "description": "New description TEST",
            "video_url": "https://www.youtube.com/watch?v=t-yCg-0-baE",
            "course": self.course.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "New lesson TEST")

    def test_lesson_delete(self):
        url = reverse("Ims:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("Ims:lesson_list")
        response = self.client.get(url)
        data = response.json()
        # print(response.json())
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "preview_image": None,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@gmail.com")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name="Course TEST",
            description="Description TEST",
        )
        self.lesson = Lesson.objects.create(
            name="Lesson TEST",
            description="Description TEST",
            course=self.course,
        )
        self.url = reverse("users:subscription_create")

    def test_subscription_create(self):
        data = {
            "user": self.user.pk,
            "course": self.course.pk
            }
        response = self.client.post(self.url, data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка добавлена")
        self.assertEqual(Subscription.objects.all().count(), 1)

    def test_subscription_delete(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка удалена")
        self.assertEqual(Subscription.objects.all().count(), 0)
