from django.views.generic import FormView
from .forms import MessageForm
from .models import Message


class HomePageView(FormView):
    template_name = 'main/home.html'
    form_class = MessageForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        context['messages'] = Message.objects.all()
        return context

    def form_valid(self, form):
        message_content = form.cleaned_data['message_content']

        Message.objects.create(
            message_content = message_content
        )

        return super().form_valid(form)
