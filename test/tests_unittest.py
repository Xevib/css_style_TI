import unittest
from tinycss.css21 import CSS21Parser

class TestCSS(unittest.TestCase):

    def setUp(self):
        self.filename = 'put your mapcss file here.mapcss'

    def test_css(self):
        f_mapcss = open(self.filename)
        css = f_mapcss.read()
        f_mapcss.close()
        #css = ''
        stylesheet = CSS21Parser().parse_stylesheet(css)
        if stylesheet.errors:
           for error in stylesheet.errors:
               print error
        self.assertTrue(len(stylesheet.errors)==0)


if __name__ == '__main__':
    unittest.main()
