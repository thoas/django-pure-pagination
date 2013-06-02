from django.core.paginator import InvalidPage


class PageNotAnInteger(InvalidPage):
    pass


class EmptyPage(InvalidPage):
    pass
