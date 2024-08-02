import unittest
from database.data_storage import store_data_in_db
from database.mongo_client import get_mongo_client, get_database

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = get_mongo_client()
        cls.db = get_database(cls.client, "scraping_python_test")
        cls.collection = cls.db["youtube_ads_test"]
        cls.collection.delete_many({})

    @classmethod
    def tearDownClass(cls):
        cls.collection.delete_many({})
        cls.client.close()

    def test_store_data_in_db(self):
        data = {
            "title": "How to easily create video ads for your Shopify products with AI",
            "channel_title": "Creatify AI",
            "duration": "PT53S",
            "views": 24641,
            "likes": 113,
            "thumbnail": "https://i.ytimg.com/vi/J41q6Zljjn8/hqdefault.jpg",
            "is_shorts": False,
            "published_at": "2023-11-27T20:24:28Z",
            "video_url": "https://www.youtube.com/watch?v=J41q6Zljjn8",
            "transcript": "welcome to creatify I'll be your guide in crafting your own short form video ad let's dive in first begin by inputting your product URL let our Advanced system automatically extract the relevant data product visuals and key details then Define the video format that aligns with your needs and choose your language preference next frame your narrative Channel your own creativity with the DIY option or choose one of the AI generated scripts for design pick an aesthetic matching your brand Essence choose in voice and avatar for your audience finetune or make changes using the edit function note lip sync may change until the video is fully rendered to wrap up simply click on render in moments creatify delivers a tailored compelling video ad for you that's it with creatify short video ads are just a few clicks away now let's make one for your [Music] product"
        }
        store_data_in_db(data)
        result = self.collection.find_one({"video_url": "https://www.youtube.com/watch?v=J41q6Zljjn8"})
        self.assertIsNotNone(result)
        self.assertEqual(result["title"], data["title"])

if __name__ == "__main__":
    unittest.main()