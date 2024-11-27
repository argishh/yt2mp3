import re

def is_valid_youtube_url(URL:str) -> bool:
    """Checks if the entered url is a valid YouTube video link

    Args:
        URL (str): url to be validated
        
    Returns:
        bool: True if the URL is a valid YouTube video URL, False otherwise
    """
    
    if not URL or not isinstance(URL, str):
        return False
    
    URL = URL.strip()   # remove any whitespace
    
    youtube_url_pattern = (
        r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/)?'
        r'([a-zA-Z0-9_-]{11})'  # Exactly 11 characters for video ID
        r'([&?][^&\s]*)?$'  # Optional query parameters
    )
    
    invalid_patterns = [
        r'/channel/',
        r'/user/',
        r'/playlist',
        r'/c/'
    ]
    
    
    # Check if any invalid patterns are in the URL
    for pattern in invalid_patterns:
        if re.search(pattern, URL):
            return False
    
    check = re.match(youtube_url_pattern, URL)
    return bool(check)
