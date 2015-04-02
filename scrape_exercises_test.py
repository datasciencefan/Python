import bs4
import requests
import scrape_exercises
import sys
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        global leada_website_url
        global leada_main_req
        global leada_main_html
        global leada_soup

        leada_website_url = "https://www.teamleada.com/"
        leada_main_req = requests.get(leada_website_url)
        if leada_main_req.status_code == 200:
            leada_main_html = leada_main_req.text
        else:
            print "Leada Main Website Returned Code: %s. \nTry Again Later."
            sys.exit(1)
        leada_soup = bs4.BeautifulSoup(leada_main_html)

    def test_get_soup(self):
        self.assertEqual(len(scrape_exercises.get_soup_for_url(leada_website_url).html), len(leada_soup.html))

    def test_get_title(self):
        self.assertEqual(scrape_exercises.get_title(leada_website_url), "Online R/Python Tutorials and Projects | Leada")
        self.assertTrue(unicode("Yahoo") in scrape_exercises.get_title("https://www.yahoo.com"))
        self.assertEqual(scrape_exercises.get_title("https://www.google.com"), unicode("Google"))

    def test_get_img_count(self):
        self.assertEqual(scrape_exercises.get_img_count(leada_website_url + "data-year"), 7)

    def test_get_pledge_count(self):
        # Since the number if changing, we're setting a minimum (as of writing the test),
        # but also an anticipated near future max
        self.assertTrue( 2900 < scrape_exercises.get_pledge_count() < 3100)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
