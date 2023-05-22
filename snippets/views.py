from django.shortcuts import render, redirect, reverse
from .models import Snippet, Language, Framework
from .forms import SnippetForm, SnippetUpdateForm, LanguageForm, FrameworkForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required
def index(request):
    # fetch 10 snippets with most views
    snippets = Snippet.objects.all().order_by('-views')[:10]
    languages = Language.objects.all()
    frameworks = Framework.objects.all()
    context = {
        'snippets': snippets,
        'languages': languages,
        'frameworks': frameworks
    }
    return render(request, 'snippets/index.html', context)


@login_required
def snippet_list(request):
    snippets = Snippet.objects.all()
    languages = Language.objects.all()
    frameworks = Framework.objects.all()
    context = {
        'snippets': snippets,
        'languages': languages,
        'frameworks': frameworks
    }
    return render(request, 'snippets/snippet_list.html', context)

@login_required
def snippet_detail(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    snippet.views += 1
    snippet.save()
    context = {
        'snippet': snippet
    }
    return render(request, 'snippets/snippet_detail.html', context)

@login_required
def search(request):
    query = request.GET.get('query')
    snippets = Snippet.objects.filter(title__icontains=query)
    languages = Language.objects.all()
    frameworks = Framework.objects.all()
    context = {
        'snippets': snippets,
        'languages': languages,
        'frameworks': frameworks
    }
    return render(request, 'snippets/snippet_search.html', context)
    
@login_required
def snippet_delete(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    snippet.delete()
    messages.success(request, 'Snippet deleted successfully.')
    return redirect(reverse('snippet_list'))


@login_required
def upvote(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    snippet.upvotes += 1
    snippet.save()
    messages.success(request, 'Snippet upvoted successfully.')
    return redirect(reverse('snippet_list'))


@login_required
def downvote(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    snippet.downvotes += 1
    snippet.save()
    messages.success(request, 'Snippet downvoted successfully.')
    return redirect(reverse('snippet_list'))


@login_required
def snippet_create(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            # save
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            messages.success(request, 'Snippet created successfully.')
            return redirect(reverse('snippet_list'))
        else:
            messages.error(request, 'Unsuccessful snippet creation. Invalid information.')
    else:
        form = SnippetForm()
    return render(request, 'snippets/snippet_create.html', {'form': form})

@login_required
def snippet_edit(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    if request.method == 'POST':
        form = SnippetUpdateForm(request.POST, instance=snippet)
        if form.is_valid():
            # save
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            messages.success(request, 'Snippet updated successfully.')
            return redirect(reverse('snippet_list'))
        else:
            messages.error(request, 'Unsuccessful snippet update. Invalid information.')
    else:
        form = SnippetUpdateForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})

@login_required
def language_create(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            # save
            language = form.save()
            messages.success(request, 'Language created successfully.')
            return redirect(reverse('snippet_list'))
        else:
            messages.error(request, 'Unsuccessful language creation. Invalid information.')
    else:
        form = LanguageForm()
    return render(request, 'snippets/language_create.html', {'form': form})

@login_required
def framework_create(request):
    if request.method == 'POST':
        form = FrameworkForm(request.POST)
        if form.is_valid():
            # save
            framework = form.save()
            messages.success(request, 'Framework created successfully.')
            return redirect(reverse('snippet_list'))
        else:
            messages.error(request, 'Unsuccessful framework creation. Invalid information.')
    else:
        form = FrameworkForm()
    return render(request, 'snippets/framework_create.html', {'form': form})

@login_required
def language_list(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, 'snippets/language_list.html', context)

@login_required
def framework_list(request):
    frameworks = Framework.objects.all()
    context = {
        'frameworks': frameworks
    }
    return render(request, 'snippets/framework_list.html', context)

@login_required
def language_edit(request, pk):
    language = Language.objects.get(pk=pk)
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            # save
            language = form.save()
            messages.success(request, 'Language updated successfully.')
            return redirect(reverse('language_list'))
        else:
            messages.error(request, 'Unsuccessful language update. Invalid information.')
    else:
        form = LanguageForm(instance=language)
    return render(request, 'snippets/language_edit.html', {'form': form})

@login_required
def framework_edit(request, pk):
    framework = Framework.objects.get(pk=pk)
    if request.method == 'POST':
        form = FrameworkForm(request.POST, instance=framework)
        if form.is_valid():
            # save
            framework = form.save()
            messages.success(request, 'Framework updated successfully.')
            return redirect(reverse('framework_list'))
        else:
            messages.error(request, 'Unsuccessful framework update. Invalid information.')
    else:
        form = FrameworkForm(instance=framework)
    return render(request, 'snippets/framework_edit.html', {'form': form})


@login_required
def language_delete(request, pk):
    language = Language.objects.get(pk=pk)
    language.delete()
    messages.success(request, 'Language deleted successfully.')
    return redirect(reverse('language_list'))

@login_required
def framework_delete(request, pk):
    framework = Framework.objects.get(pk=pk)
    framework.delete()
    messages.success(request, 'Framework deleted successfully.')
    return redirect(reverse('framework_list'))