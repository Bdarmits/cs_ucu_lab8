from urllib.request import urlopen
import time

class WebPage:
    def __init__(self, url):
        self._time = time.time()
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content or (time.time()-self._time) >= 86400:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content



