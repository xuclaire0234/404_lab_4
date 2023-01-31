from django.urls import path
from . import views
# # 1:
# urlpatterns = [
#   path('', views.index, name='index'),
# ]

# 2:
# app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'), 
# ]

# 3 Amend URLconf
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),  # still use question_id to show up 
    # path('<str:question_id>/vote/', views.vote, name='vote')
    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),
]