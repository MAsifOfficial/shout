from django.views.generic import FormView
from .forms import MessageForm


class HomePageView(FormView):
    template_name = 'main/home.html'
    form_class = MessageForm
