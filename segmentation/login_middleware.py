# from django.conf import settings
# from django.http import HttpResponseRedirect
# from django.utils.deprecation import MiddlewareMixin
# from django.utils.http import is_safe_url
# import re


# EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
# if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
#     EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


# class Login_RequiredMiddleware(MiddlewareMixin):

#     def process_request(self, request):
#         try:
#             assert hasattr(request, 'user'), "The Login Required Middleware"
#             if not request.user.is_authenticated:
#                 path = request.path_info.lstrip('/home/')
#                 if not any(m.match(path) for m in EXEMPT_URLS):
#                     redirect_to = settings.LOGIN_URL
#                     # 'next' variable to support redirection to attempted page after login
#                     if request.user.is_authenticated:
#                         if len(path) > 0 and is_safe_url(
#                             url=request.path_info, allowed_hosts=request.get_host()):
#                             redirect_to = f"{settings.LOGIN_URL}?next={request.user_profile}"
#                     else:
#                         return HttpResponseRedirect('/')
#         except(request):
#             return redirect_to(settings.LOGIN_URL)