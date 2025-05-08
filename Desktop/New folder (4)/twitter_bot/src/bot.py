import os
import time
import random
import tweepy
import schedule
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

class TwitterBot:
    def __init__(self):
        """Initialize the Twitter bot with API credentials"""
        # Authenticate with Twitter API
        self.client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=API_KEY, 
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN, 
            access_token_secret=ACCESS_SECRET
        )
        print("Twitter bot initialized!")
        
    def post_tweet(self, content):
        """Post a tweet with the given content"""
        try:
            response = self.client.create_tweet(text=content)
            print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
            return response
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return None
    
    def retweet(self, tweet_id):
        """Retweet a tweet with the given ID"""
        try:
            response = self.client.retweet(tweet_id)
            print(f"Retweet successful! ID: {response.data['id']}")
            return response
        except Exception as e:
            print(f"Error retweeting: {e}")
            return None
    
    def like_tweet(self, tweet_id):
        """Like a tweet with the given ID"""
        try:
            response = self.client.like(tweet_id)
            print(f"Tweet liked successfully!")
            return response
        except Exception as e:
            print(f"Error liking tweet: {e}")
            return None
    
    def search_tweets(self, query, max_results=10):
        """Search for tweets matching the query"""
        try:
            tweets = self.client.search_recent_tweets(
                query=query, 
                max_results=max_results
            )
            if tweets.data:
                print(f"Found {len(tweets.data)} tweets matching query: '{query}'")
                return tweets.data
            else:
                print(f"No tweets found matching query: '{query}'")
                return []
        except Exception as e:
            print(f"Error searching tweets: {e}")
            return []
    
    def follow_user(self, user_id):
        """Follow a user with the given ID"""
        try:
            response = self.client.follow_user(user_id)
            print(f"Successfully followed user {user_id}")
            return response
        except Exception as e:
            print(f"Error following user: {e}")
            return None
    
    def get_user_by_username(self, username):
        """Get a user by their username"""
        try:
            user = self.client.get_user(username=username)
            return user.data
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

# Example scheduled tasks
def schedule_tweets(bot):
    """Set up scheduled tasks for the bot"""
    # Example tweet content
    tweets = [
        "Check out my latest 3D printing projects! #3DPrinting #Tech",
        "New portfolio items added to my website! #WebDev #Freelance",
        "Looking for custom 3D printing services? Contact me today! #3DPrinting #CustomDesign",
        "Freelance developer available for hire - specializing in web development and 3D printing integration",
        "Just launched a new e-commerce feature on my website! #WebDevelopment #ECommerce"
    ]
    
    # Schedule a daily tweet at a random time
    def job():
        tweet = random.choice(tweets)
        bot.post_tweet(tweet)
    
    # Schedule tweets at different times
    schedule.every().day.at("10:00").do(job)
    schedule.every().day.at("15:30").do(job)
    schedule.every().day.at("19:45").do(job)
    
    print("Tweet schedule set up!")

def run_bot():
    """Main function to run the Twitter bot"""
    # Check if environment variables are set
    if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET, BEARER_TOKEN]):
        print("Error: Twitter API credentials not found in .env file")
        print("Please create a .env file with your Twitter API credentials")
        return
    
    # Initialize the bot
    bot = TwitterBot()
    
    # Set up scheduled tasks
    schedule_tweets(bot)
    
    # Run the bot continuously
    print("Bot is running. Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Bot stopped by user.")

if __name__ == "__main__":
    run_bot()
