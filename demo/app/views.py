from django.template.response import TemplateResponse
from django.views import View

from . import forms, queries


class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = forms.NovelForm(request.GET)
        if not form.is_valid():
            return TemplateResponse(
                request,
                "index.html",
                {
                    "context": {
                        "form": form,
                        "novels": [],
                    }
                },
            )
        novels = queries.search_novel(
            author_name=form.cleaned_data["author_name"],
            keyword=form.cleaned_data["keyword"],
        )
        context = {"form": form, "novels": novels}
        return TemplateResponse(request, "index.html", {"context": context})
