from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'ps'   # Dynamic page number in query 
    page_size_query_param = 'limit'  # limit in each page