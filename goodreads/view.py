from django.shortcuts import render
from django.views import View

import user
from book.models import BookReview
from user.models import CustomUser


class landing_page(View):
    def get(self, request):

        return render(request, template_name='landing_page.html')

class home_page(View):
        def get(self, request):
            users = CustomUser.objects.all()
            req_user = list(filter(lambda user: request.user.is_following(user), [user for user in users]))
            comments = BookReview.objects.filter(user__in=req_user)
            context = {
                'comments': comments,
                'req_user': req_user
            }

            return render(request, 'home.html', context)
