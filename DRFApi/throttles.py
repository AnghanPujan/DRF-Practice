
from rest_framework.throttling import UserRateThrottle

class AuthTestScopedThrottle(UserRateThrottle):
    scope = 'auth_test'