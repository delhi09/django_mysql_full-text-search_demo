from django.test import TransactionTestCase

from .factories import NovelFactory
from app import queries


class TestSearchNovel(TransactionTestCase):
    @classmethod
    def setUp(cls):
        NovelFactory(
            author_name="夏目漱石",
            title="草枕",
            search_text="草枕,山路を登りながら、こう考えた。",
        )
        NovelFactory(
            author_name="森鴎外",
            title="舞姫",
            search_text="舞姫,石炭をば早はや積み果てつ。",
        )

    def test_it(self):
        novels = queries.search_novel(author_name="夏目漱石", keyword="山路")
        self.assertEqual(len(novels), 1)
        self.assertEqual(novels[0].author_name, "夏目漱石")
        self.assertEqual(novels[0].title, "草枕")

    def test_author_name_and_keyword_mismatched(self):
        novels = queries.search_novel(author_name="夏目漱石", keyword="石炭")
        self.assertEqual(len(novels), 0)

    def test_author_name_empty(self):
        novels = queries.search_novel(keyword="草枕")
        self.assertEqual(len(novels), 1)
        self.assertEqual(novels[0].author_name, "夏目漱石")
        self.assertEqual(novels[0].title, "草枕")

    def test_keyword_empty(self):
        novels = queries.search_novel(author_name="夏目漱石")
        self.assertEqual(len(novels), 1)
        self.assertEqual(novels[0].author_name, "夏目漱石")
        self.assertEqual(novels[0].title, "草枕")

    def test_author_name_and_keyword_empty(self):
        novels = queries.search_novel()
        self.assertEqual(len(novels), 2)
        self.assertEqual(novels[0].author_name, "森鴎外")
        self.assertEqual(novels[0].title, "舞姫")
        self.assertEqual(novels[1].author_name, "夏目漱石")
        self.assertEqual(novels[1].title, "草枕")
