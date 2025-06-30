from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Lesson, UpdateSubscriptionCourse
from users.models import User


class LessonTestCase(APITestCase):
    """Класс теста модели урока и его функционала"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(
            name="Общеобразовательные предметы",
            description="Тем, кто хочет повторить школьные знания",
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            name="Математика",
            description="Царица/королева/мне не подвластная наука :)",
            video="https://www.youtube.com/",
            owner=self.user,
            course=self.course,
        )
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            "name": "Химия",
            "description": "Интересная наука с забавными реакциями",
            "video": "https://www.youtube.com/",
        }
        response = self.client.post("http://127.0.0.1:8000/education/lesson/create/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {
                "id": 2,
                "name": "Химия",
                "description": "Интересная наука с забавными реакциями",
                "video": "https://www.youtube.com/",
                "photo": None,
                "course": None,
                "owner": 1,
            },
        )

        self.assertTrue(Lesson.objects.all().exists())

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""

        url = reverse('education:lesson_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.pk,
                        "name": "Математика",
                        "description": "Царица/королева/мне не подвластная наука :)",
                        "video": "https://www.youtube.com/",
                        "photo": None,
                        "course": self.course.pk,
                        "owner": self.user.pk,
                    },
                ],
            },
        )

    def test_retrieve_lesson(self):
        """Тестирование выводы конкретного урока"""

        url = reverse('education:lesson_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": self.lesson.pk,
                "name": "Математика",
                "description": "Царица/королева/мне не подвластная наука :)",
                "video": "https://www.youtube.com/",
                "photo": None,
                "course": self.course.pk,
                "owner": self.user.pk,
            },
        )

    def test_update_lesson(self):
        """Тестирование обновления урока"""

        data = {"name": "Геометрия"}
        url = reverse('education:lesson_update', args=(self.lesson.pk,))
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), response.json().get("name"))

    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        url = reverse('education:lesson_delete', args=(self.lesson.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    class UpdateSubscriptionCourseTestCase(APITestCase):
        """Класс тестирования обновления подписки и его функционал"""

        def setUp(self):
            self.user = User.objects.create(
                email="testsub@testsub.com",
            )
            self.course = Course.objects.create(name="Шитье и вязание", owner=self.user)
            self.lesson = Lesson.objects.create(
                name="Как правильно хранить нитки и пряжу",
                course=self.course,
                video="https://www.youtube.com",
                owner=self.user,
            )
            self.course_subscription = UpdateSubscriptionCourse(user=self.user, course=self.course)
            self.client.force_authenticate(user=self.user)

        def test_course_subscribe(self):
            url = reverse("education:subscribe_on_course", args=(self.course.pk,))
            data = {"course": self.course.pk}
            response = self.client.post(url, data)
            data = response.json()

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(data["message"], "Подписка добавлена")

            data = {"course": self.course.pk}
            response = self.client.post(url, data)
            data = response.json()

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(data["message"], "Подписка удалена")
