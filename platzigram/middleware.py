# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile

                if not profile.picture or not profile.biography:
                    exception_urls = [reverse('users:update'), reverse('users:logout')]
                    if request.path not in exception_urls:
                        return redirect('users:update')
        
        response = self.get_response(request)
        return response