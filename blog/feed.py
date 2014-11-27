from django.contrib.syndication.views import Feed
from .models import Entry

class LatestPosts(Feed):
    title = "BLog | Camilo"
    link = "/feed/"
    description = "Latest blog post in camilogonzalez.net"

    def items(self):
        return Entry.objects.published()[:5]
