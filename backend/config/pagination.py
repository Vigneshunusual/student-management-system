from rest_framework.pagination import PageNumberPagination
class CustomPagination(PageNumberPagination):
    page_size = 10     #10 records per page
    page_size_query_param = 'page_size'   #Allow clients to set the page size using a query parameter
    max_page_size = 50  #maximum page size that can be requested by clients
                        #They can request at most 50 records per page.