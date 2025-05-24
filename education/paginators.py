from rest_framework.pagination import PageNumberPagination


class LessonPagination(PageNumberPagination):
    """Класс настройки пагинации страниц с выводом уроков"""

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 10


class CoursePagination(PageNumberPagination):
    """Класс настройки пагинации страц с курсами"""

    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10
