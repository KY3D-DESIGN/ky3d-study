import os
import tweepy
from dotenv import load_dotenv

class TwitterAPI:
    def __init__(self):
        """Initialize Twitter API connection using credentials from .env file"""
        load_dotenv()
        
        # Load API credentials from environment variables
        self.api_key = os.getenv("TWITTER_API_KEY")
        self.api_secret = os.getenv("TWITTER_API_SECRET")
        self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
        
        # Initialize API connection
        self.client = None
        self.api = None
        self._connect()
    
    def _connect(self):
        """Establish connection to Twitter API"""
        try:
            # Set up authentication
            auth = tweepy.OAuth1UserHandler(
                self.api_key, self.api_secret,
                self.access_token, self.access_token_secret
            )
            
            # Create API object
            self.api = tweepy.API(auth)
            
            # Create Client object (v2 API)
            self.client = tweepy.Client(
                bearer_token=self.bearer_token,
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret
            )
            
            print("Successfully connected to Twitter API")
        except Exception as e:
            print(f"Error connecting to Twitter API: {e}")
    
    def post_tweet(self, text):
        """Post a tweet with the given text"""
        try:
            # Using v2 API
            response = self.client.create_tweet(text=text)
            tweet_id = response.data['id']
            print(f"Tweet posted successfully! ID: {tweet_id}")
            return tweet_id
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return None
    
    def post_tweet_with_media(self, text, media_path):
        """Post a tweet with media attachment"""
        try:
            # Upload media using v1.1 API
            media = self.api.media_upload(media_path)
            
            # Post tweet with media using v2 API
            response = self.client.create_tweet(
                text=text,
                media_ids=[media.media_id]
            )
            tweet_id = response.data['id']
            print(f"Tweet with media posted successfully! ID: {tweet_id}")
            return tweet_id
        except Exception as e:
            print(f"Error posting tweet with media: {e}")
            return None
    
    def get_user_timeline(self, username, count=10):
        """Get recent tweets from a user's timeline"""
        try:
            user_id = self.client.get_user(username=username).data.id
            tweets = self.client.get_users_tweets(
                id=user_id,
                max_results=count
            )
            return tweets.data
        except Exception as e:
            print(f"Error getting user timeline: {e}")
            return []
    
    def search_tweets(self, query, count=10):
        """Search for tweets matching the query"""
        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=count
            )
            return tweets.data
        except Exception as e:
            print(f"Error searching tweets: {e}")
            return []
    
    def follow_user(self, username):
        """Follow a user by username"""
        try:
            user_id = self.client.get_user(username=username).data.id
            self.client.follow_user(user_id)
            print(f"Successfully followed user: {username}")
            return True
        except Exception as e:
            print(f"Error following user: {e}")
            return False
    
    def like_tweet(self, tweet_id):
        """Like a tweet by its ID"""
        try:
            self.client.like(tweet_id)
            print(f"Successfully liked tweet: {tweet_id}")
            return True
        except Exception as e:
            print(f"Error liking tweet: {e}")
            return False
    
    def retweet(self, tweet_id):
        """Retweet a tweet by its ID"""
        try:
            self.client.retweet(tweet_id)
            print(f"Successfully retweeted: {tweet_id}")
            return True
        except Exception as e:
            print(f"Error retweeting: {e}")
            return False
