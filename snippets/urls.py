from django.urls import path
from .views import index, snippet_list, snippet_detail, snippet_create, snippet_edit, snippet_delete, search, upvote, downvote, framework_create,framework_edit, framework_delete, language_create, language_edit, language_delete, language_list, framework_list

urlpatterns = [
    path('', index, name='home'), # top snippets
    path('list/', snippet_list, name='snippet_list'),
    path('view/<int:pk>/', snippet_detail, name='snippet_detail'),
    path('search', search, name='search'),
    path('create/', snippet_create, name='snippet_create'),
    path('edit/<int:pk>/', snippet_edit, name='snippet_edit'),
    path('delete/<int:pk>/', snippet_delete, name='snippet_delete'),
    # upvote snippet
    path('upvote/<int:pk>/', upvote, name='upvote'),
    # downvote snippet
    path('downvote/<int:pk>/', downvote, name='downvote'),
    # create framework
    path('framework/create/', framework_create, name='framework_create'),
    # edit framework
    path('framework/edit/<int:pk>/', framework_edit, name='framework_edit'),
    # delete framework
    path('framework/delete/<int:pk>/', framework_delete, name='framework_delete'),
    # create language
    path('language/create/', language_create, name='language_create'),
    # edit language
    path('language/edit/<int:pk>/', language_edit, name='language_edit'),
    # delete language
    path('language/delete/<int:pk>/', language_delete, name='language_delete'),
    # list languages
    path('language/list/', language_list, name='language_list'),
    # list frameworks
    path('framework/list/', framework_list, name='framework_list'),
]

