from django.utils.timezone import now
from users.models import User
from django.utils.deprecation import MiddlewareMixin


class SetLastVisitMiddleware(MiddlewareMixin):
    # def process_response(self, request, response):
    #     if request.user.is_authenticated():
    #         User.objects.filter(pk=request.user.pk).update(last_login=now())
    #     return response
    
    ...