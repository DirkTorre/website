from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message'] = 'Welcome to the Home Page you bastard!!'
        return context