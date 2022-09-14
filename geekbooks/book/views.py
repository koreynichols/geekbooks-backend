from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import BookSerializer
from .models import Book

book_fields_dict = {
    'id': None,
    'selfLink': None,
    'thumbnail': None,
    'authors': None,
    'title': None,
    'listPrice': None,
    'description': None,
    'publisher': None,
    'publishedDate': None,
    'pageCount': None,
    'categories': None,
}

keysToFind = ['id', 'selfLink']
nestedKeysToFind = ['authors', 'title', 'description', 'publisher', 'publishedDate', 'pageCount', 'categories']
imageKeyToFind = 'thumbnail'
priceKeyToFind = 'listPrice'
class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['GET'])
    def create_book(self, request):

        def validate_data(data):
            for key in keysToFind:
                try:
                    book_fields_dict[key] = data[key]
                except:
                    book_fields_dict[key] = None
            
            for key in nestedKeysToFind:
                try:
                    book_fields_dict[key] = data['volumeInfo'][key]
                except:
                    book_fields_dict[key] = None

            try:
                book_fields_dict[imageKeyToFind] = data['volumeInfo']['imageLinks'][imageKeyToFind]
            except:
                book_fields_dict[imageKeyToFind] = None

            try:
                book_fields_dict[priceKeyToFind] = data['saleInfo']['listPrice'][priceKeyToFind]
            except:
                book_fields_dict[priceKeyToFind] = None
            return


        validate_data(request)
        print(book_fields_dict)

        Book.objects.create(
                book_id = book_fields_dict['id'] or None,
                book_url = book_fields_dict['selfLink'] or None,
                cover_image = book_fields_dict['thumbnail'] or None,
                author = book_fields_dict['authors'] or None,
                title = book_fields_dict['title'] or None,
                price = book_fields_dict['listPrice'] or None,
                description = book_fields_dict['description'] or None,
                publisher = book_fields_dict['publisher'] or None,
                published_date = book_fields_dict['publishedDate'] or None,
                number_of_pages = book_fields_dict['pageCount'] or None,
                genre = book_fields_dict['categories'] or None,
            )

        response = {'message': 'its working'}
        return Response(response, status=status.HTTP_200_OK)