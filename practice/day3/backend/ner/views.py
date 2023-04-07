# from django.shortcuts import render
from django.http import HttpResponse
from .database_utils import get_doc_element
from django.views import generic
from .models import Documents
# Create your views here.


def index(request):
    return HttpResponse("Hello, world")


def ner_help(request, name: str):
    return HttpResponse(f"Hi {name} Please check the detail in README.md file.")


def get_doc_data(request, doc_id: int, element_name: str):
    return HttpResponse(get_doc_element(doc_id, element_name))


class TemplateViewTest(generic.TemplateView):
    template_name = 'testTemplate.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateViewTest, self).get_context_data()
        context['name'] = "Hi Jinqiao"
        return context


class ListViewTest(generic.ListView):
    model = Documents
    template_name = 'testListView.html'
    context_object_name = 'doc_list'

    def get_queryset(self):
        return Documents.objects.order_by('doc_id')[:2]


class DocumentsDetail(generic.DetailView):
    model = Documents
    template_name = 'testDetailView.html'
