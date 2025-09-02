from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'ps'   # Dynamic page number in query 
    page_size_query_param = 'limit'  # limit in each page

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5 
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 6 


class MyCursorPagination(CursorPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 6  
    ordering = '-id'   