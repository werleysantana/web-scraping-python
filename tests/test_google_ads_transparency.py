import unittest
from scraper.google_ads_transparency import get_ads_for_domains, extract_ad_info

class TestGoogleAdsTransparency(unittest.TestCase):

    def test_get_ads_for_domains(self):
        domains = ["creatify.ai"]
        ads = get_ads_for_domains(domains)
        self.assertIsInstance(ads, list)
        self.assertGreater(len(ads), 0, "A lista de anúncios não deve estar vazia")

    def test_extract_ad_info(self):
        mock_video_element = """
        <div class="ad-info">
            <div class="title">Test Video</div>
            <div class="channel-name">Test Channel</div>
            <a class="video-link" href="https://www.youtube.com/watch?v=J41q6Zljjn8">Video Link</a>
        </div>
        """
        from bs4 import BeautifulSoup
        video_element = BeautifulSoup(mock_video_element, 'html.parser').find("div", class_="ad-info")
        ad_info = extract_ad_info(video_element)
        self.assertIsNotNone(ad_info)
        self.assertEqual(ad_info['title'], "Creatify AI - How to create a video ad with the help of AI in just a few clicks")
        self.assertEqual(ad_info['channel'], "Creatify AI")
        self.assertEqual(ad_info['video_url'], "https://www.youtube.com/watch?v=J41q6Zljjn8")

if __name__ == "__main__":
    unittest.main()