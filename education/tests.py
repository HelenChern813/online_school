from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

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

        Lesson.objects.create(
            name="Биология",
            description="Интересная наука со знаниями о человеке",
            video="https://www.youtube.com/",
            course=self.course,
        )

        response = self.client.get("http://127.0.0.1:8000/education/lesson/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.maxDiff = None

        self.assertEqual(
            response.json(),
            {
                "count": 2,
                "next": None,
                "previous": None,
                "results": [
                    {'course': 1,
                     'description': 'Интересная наука со знаниями о человеке',
                     'id': 2,
                     'name': 'Биология',
                     'owner': None,
                     'photo': None,
                     'video': 'https://www.youtube.com/'},
                    {
                        "id": 1,
                        "name": "Математика",
                        "description": "Царица/королева/мне не подвластная наука :)",
                        "video": "https://www.youtube.com/",
                        "photo": None,
                        "course": 1,
                        "owner": 1,
                    }
                ],
            },
        )
