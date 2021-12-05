import factory
from app.models import Novel


class NovelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Novel

    title = "テストタイトル"
    author_name = "山田太郎"
    content = "テストコンテント"
    search_text = "テストタイトル,テストコンテント"
