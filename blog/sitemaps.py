from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from taggit.models import Tag
from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated


# New class for Tag URLs
class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6  # Slightly lower priority than main posts

    def items(self):
        # Returns all tags that are currently associated with at least one post
        return Tag.objects.all()

    def location(self, obj):
        # Build the URL using the name defined in blog/urls.py
        # Since your URL uses a namespace ('blog'), prefix it here
        return reverse("blog:post_list_by_tag", args=[obj.slug])
