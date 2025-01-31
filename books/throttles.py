from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class BookAnonRateThrottle(AnonRateThrottle):
    scope = 'book_anon'

class BookUserRateThrottle(UserRateThrottle):
    scope = 'book_user'
