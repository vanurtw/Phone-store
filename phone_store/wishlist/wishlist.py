from django.conf import settings


class Wishlist:
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID, None)
        if not wishlist:
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {}
        self.wishlist = wishlist

    def add(self, id):
        if id not in self.wishlist:
            self.wishlist[id] = id
            self.save()

    def clear(self):
        del self.session[settings.WISHLIST_SESSION_ID]
        self.session.modified = True

    def save(self):
        self.session[settings.WISHLIST_SESSION_ID] = self.wishlist
        self.session.modified = True
