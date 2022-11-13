from unittest import TestCase
from reddit.parser import get_videos, check_video


class TestRedditParser(TestCase):
    def test_get_videos(self):
        """
        GIVEN an json string
        WHEN is getting the urls of videos
        THEN it should a list of urls of videos
        """
        mocked_json = "{\"data\": {\"children\": [{\"data\": {\"secure_media\": {\"reddit_video\": " \
                      "{\"fallback_url\": \"https://v.redd.it/gyh95hiqc0b11/DASH_9_6_M?source=fallback\"}}}},{}]}}"
        videos = get_videos(mocked_json)
        self.assertTrue(len(videos) == 1)

    def test_check_video_exists(self):
        """
        GIVEN a dictionary representation of a video from reddit
        WHEN is checking the dictionary
        THEN it should return true when the dictionary has a video
        """
        mocked_dictionary = {
            'data': {
                'secure_media': {
                    'reddit_video': {
                        'fallback_url': 'www.youtube.com'
                    }
                }
            }
        }
        self.assertTrue(check_video(mocked_dictionary))

    def test_check_video_when_dictionary_is_empty(self):
        """
        GIVEN a dictionary representation of a video from reddit
        WHEN is checking the dictionary
        THEN it should return false when the dictionary is empty
        """
        mocked_dictionary = {}
        self.assertFalse(check_video(mocked_dictionary))