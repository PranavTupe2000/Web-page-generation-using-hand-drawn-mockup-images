from django.views.generic import TemplateView

class MainView(TemplateView):
	template_name = 'Main.html'

class marksView(TemplateView):
	template_name = 'marks.html'

