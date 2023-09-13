from django.test import SimpleTestCase
from django.urls import reverse, resolve
from locations.views import add_location, map_page, search_page, show_full_map


class TestsUrls(SimpleTestCase):
    def test_add_location_url_works(self):
        url = reverse('add_location')
        self.assertEquals(resolve(url).func, add_location)

    def test_map_page_url_works(self):
        url = reverse('map_page')
        self.assertEquals(resolve(url).func, map_page)

    def test_search_url_works(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search_page)

    def test_full_map_url_works(self):
        url = reverse('map')
        self.assertEquals(resolve(url).func, show_full_map)

