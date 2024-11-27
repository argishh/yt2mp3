import unittest
from url_validator import is_valid_youtube_url

class TestYouTubeUrlValidator(unittest.TestCase):
    def test_standard_youtube_url(self):
        """Test standard YouTube video URL format"""
        valid_urls = [
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'http://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'www.youtube.com/watch?v=dQw4w9WgXcQ',
            'youtube.com/watch?v=dQw4w9WgXcQ',
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s',
        ]
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_valid_youtube_url(url))
    
    def test_shortened_youtube_url(self):
        """Test shortened YouTube URL formats"""
        valid_urls = [
            'https://youtu.be/dQw4w9WgXcQ',
            'http://youtu.be/dQw4w9WgXcQ',
            'youtu.be/dQw4w9WgXcQ',
        ]
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_valid_youtube_url(url))
    
    def test_embedded_youtube_url(self):
        """Test embedded YouTube URL formats"""
        valid_urls = [
            'https://www.youtube.com/embed/dQw4w9WgXcQ',
            'http://www.youtube.com/embed/dQw4w9WgXcQ',
            'youtube.com/embed/dQw4w9WgXcQ',
        ]
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_valid_youtube_url(url))
    
    def test_invalid_youtube_url(self):
        """Test invalid URL formats"""
        invalid_urls = [
            'https://www.youtube.com',
            'https://www.youtube.com/channel/123',
            'https://www.youtube.com/user/username',
            'https://www.youtube.com/c/channelname',
            'https://vimeo.com/123456',
            'not a url',
            '',
            None,
            'https://www.youtube.com/watch?v=invalid',
            'https://www.youtube.com/watch?v=too_long_video_id',
            'https://www.youtube.com/playlist?list=someplaylist',
        ]
        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(is_valid_youtube_url(url))
    
    def test_url_with_additional_parameters(self):
        """Test YouTube URLs with additional parameters"""
        valid_urls = [
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be',
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=30s',
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=playlist_id',
        ]
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_valid_youtube_url(url))

if __name__ == '__main__':
    unittest.main()