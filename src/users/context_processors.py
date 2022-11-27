from django.http import HttpRequest


def user(request):
    if hasattr(request, 'user'):
        return {'user':request.user }
    return {'user':None}

def user(request: HttpRequest) -> str:
    if request.session.get("user"):
        return {"username": request.session["user"]["userinfo"]["given_name"]}
    return {"username": None}