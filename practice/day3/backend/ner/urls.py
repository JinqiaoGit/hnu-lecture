from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/help', views.ner_help, name='ner_help'),
    path('data/<str:element_name>/<int:doc_id>', views.get_doc_data, name='ner_data'),
    path('template/', views.TemplateViewTest.as_view(), name='view_template_test'),
    path('ListView/<int:pk>', views.ListViewTest.as_view(), name='list_view_test'),
    path('templateView/<int:pk>/', views.DocumentsDetail.as_view(), name='detail_view_test')
]
