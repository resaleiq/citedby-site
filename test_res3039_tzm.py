import glob, re, unittest


class TzmLink(unittest.TestCase):
    def test_limit_link_inherits_message_colour(self):
        pages = glob.glob("public/landing*.html") + glob.glob("public/**/free-ai-visibility-check.html", recursive=True)
        self.assertEqual(len(pages), 10)
        for p in pages:
            h = open(p, encoding="utf-8").read()
            self.assertIn("#tzm a{color:inherit;text-decoration:underline}", h, p)
            self.assertIn(".tzm{color:#FFD2D6", h, p)


if __name__ == "__main__":
    unittest.main()
