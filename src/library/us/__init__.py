from src.library.collection.base_objects import PublisherEnum, PublisherSpec

from .ap_news import APNewsParser
from .fox_news import FoxNewsParser
from .free_beacon import FreeBeaconParser


class US(PublisherEnum):
    APNews = PublisherSpec(
        domain="https://apnews.com/",
        sitemaps=["https://apnews.com/sitemap/sitemaps/sitemap_index.xml"],
        news_map="https://apnews.com/sitemap/google-news-sitemap/sitemap_index.xml",
        parser=APNewsParser,
    )

    FoxNews = PublisherSpec(
        domain="https://foxnews.com/",
        sitemaps=[" https://www.foxnews.com/sitemap.xml"],
        news_map="https://www.foxnews.com/sitemap.xml?type=news",
        parser=FoxNewsParser,
    )
    FreeBeacon = PublisherSpec(
        domain="https://freebeacon.com/",
        news_map="https://freebeacon.com/post_google_news.xml",
        parser=FreeBeaconParser,
    )
