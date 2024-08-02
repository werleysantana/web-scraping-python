import unittest
from scraper.youtube_scraper import extract_video_id, get_youtube_video_details

class TestYouTubeScraper(unittest.TestCase):

    def test_extract_video_id(self):
        video_url = "https://www.youtube.com/watch?v=J41q6Zljjn8"
        video_id = extract_video_id(video_url)
        self.assertEqual(video_id, "dQw4w9WgXcQ")

    def test_get_youtube_video_details(self):
        video_url = "https://www.youtube.com/watch?v=J41q6Zljjn8"
        details = get_youtube_video_details(video_url)
        self.assertIn("title", details)
        self.assertIn("channel_title", details)
        self.assertIn("duration", details)
        self.assertIn("views", details)

if __name__ == "__main__":
    unittest.main()