from rest_framework import generics, status
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer
from .throttles import BookAnonRateThrottle, BookUserRateThrottle
import time

def get_rate_limit_headers(view, request):
    """Retrieve rate-limit headers from the applied throttle classes."""
    headers = {}
    for throttle in view.get_throttles():
        if hasattr(throttle, "get_cache_key"):
            throttle_key = throttle.get_cache_key(request, view)
            if not throttle_key:
                continue

            rate = throttle.get_rate()
            if not rate:
                continue

            num_requests, duration_unit = rate.split('/')
            num_requests = int(num_requests)

            duration_map = {'sec': 1, 'min': 60, 'hour': 3600, 'day': 86400}
            duration = duration_map.get(duration_unit, 60)

            history = throttle.cache.get(throttle_key, [])
            remaining = max(num_requests - len(history), 0)
            reset_time = int(history[0] + duration) if history else int(time.time())

            headers.update({
                'X-RateLimit-Limit': str(num_requests),
                'X-RateLimit-Remaining': str(remaining),
                'X-RateLimit-Reset': str(reset_time)
            })
    return headers


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [BookAnonRateThrottle, BookUserRateThrottle]

    def list(self, request, *args, **kwargs):
        """Retrieve books with rate-limit headers"""
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return self._custom_response("Books retrieved successfully!", serializer.data, request)

    def create(self, request, *args, **kwargs):
        """Create a book with rate-limit headers"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self._custom_response("Book created successfully!", serializer.data, request, status.HTTP_201_CREATED)

    def _custom_response(self, message, data, request, http_status=status.HTTP_200_OK):
        """Helper function to format responses consistently"""
        headers = get_rate_limit_headers(self, request)
        return Response(
            {"status": "success", "message": message, "data": data, "headers": headers},
            status=http_status
        )


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [BookAnonRateThrottle, BookUserRateThrottle]

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a book with rate-limit headers"""
        return self._custom_response("Book retrieved successfully!", self.get_serializer(self.get_object()).data, request)

    def update(self, request, *args, **kwargs):
        """Update a book with rate-limit headers"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return self._custom_response("Book updated successfully!", serializer.data, request)

    def destroy(self, request, *args, **kwargs):
        """Delete a book with rate-limit headers"""
        self.perform_destroy(self.get_object())
        return self._custom_response("Book deleted successfully!", None, request, status.HTTP_204_NO_CONTENT)

    def _custom_response(self, message, data, request, http_status=status.HTTP_200_OK):
        """Helper function to format responses consistently"""
        headers = get_rate_limit_headers(self, request)
        response_data = {"status": "success", "message": message, "headers": headers}
        if data is not None:
            response_data["data"] = data
        return Response(response_data, status=http_status)
