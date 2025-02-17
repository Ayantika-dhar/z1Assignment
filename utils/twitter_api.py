import tweepy
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

def get_twitter_api():
    """Authenticate with Twitter API and return the API client."""
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

def post_images_to_twitter(image_paths, status="Here are my resized images!"):
    """Post multiple images to Twitter."""
    api = get_twitter_api()
    media_ids = [api.media_upload(img).media_id for img in image_paths]
    api.update_status(status=status, media_ids=media_ids)

