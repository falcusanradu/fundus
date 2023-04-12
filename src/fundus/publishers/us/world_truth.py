import datetime
from typing import Optional

from lxml.cssselect import CSSSelector

from src.fundus.parser import ArticleBody, BaseParser, attribute
from src.fundus.parser.utility import (
    extract_article_body_with_selector,
    generic_date_parsing,
)


class WorldTruthParser(BaseParser):
    _paragraph_selector = CSSSelector(".td-post-content > p")

    @attribute
    def body(self) -> ArticleBody:
        return extract_article_body_with_selector(
            self.precomputed.doc,
            paragraph_selector=self._paragraph_selector,
        )

    @attribute
    def publishing_date(self) -> Optional[datetime.datetime]:
        return generic_date_parsing(self.precomputed.meta.get("article:published_time"))

    @attribute
    def title(self) -> Optional[str]:
        return self.precomputed.meta.get("og:title")
