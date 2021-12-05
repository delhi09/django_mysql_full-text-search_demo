from typing import Optional

from django.db.models.query import QuerySet

from .models import Novel


def search_novel(
    author_name: Optional[str] = None, keyword: Optional[str] = None
) -> QuerySet[Novel]:
    qs = Novel.objects
    if author_name:
        qs = qs.filter(author_name=author_name)
    if keyword:
        qs = qs.filter(search_text__search=keyword)
    return qs.all().order_by("-created_at")
