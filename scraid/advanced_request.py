from scrapy import Request
from fake_useragent import UserAgent

# ----------------------------------------------------------


class AdvancedRequest(Request):
    """
        AdvancedRequest is a subclass of scrapy.Request that sets a random User-Agent header for each request,
        using the fake-useragent package, to avoid being blocked by websites that detect and block spiders.
    """

    def __init__(self, *args, **kwargs):
        headers = {'User-Agent': UserAgent().random}
        kwargs.setdefault('headers', headers)
        super().__init__(*args, **kwargs)
