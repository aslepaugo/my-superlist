import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mario heard about application to create list of urgent tasks
        # Mario decided to view on it
        self.browser.get("http://localhost:8000")

        # Mario sees list of ToDo stuff
        self.assertIn("To-Do", self.browser.title)
        self.fail('Finish test!')

        # And he can add additional item
        # He writes "To buy stickers" (he likes stickers)
        # When he clicks Enter page reloads and now he can see
        # 1: To buy stickers

        # New item could be added
        # Mario writes "To stick sticker on a board"
        # Page rerefses and there are 2 items

        # Mario sees that his list has unique link
        # Thre is info about it

        # Mario decided to visit this unique link
        # List is still there

        # Well done, now Mario can go to sleep


if __name__ == '__main__':
    unittest.main()
