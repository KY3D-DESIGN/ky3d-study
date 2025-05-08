# Twitter/X Bot

A simple Twitter/X bot that can automate posting tweets, retweeting, following users, and more using the Twitter API v2.

## Features

- Post tweets automatically on a schedule
- Retweet content based on hashtags
- Follow users based on criteria
- Like tweets based on keywords
- Reply to mentions

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a Twitter Developer account and create a project to get API credentials
4. Copy `.env.example` to `.env` and fill in your Twitter API credentials
5. Customize the bot behavior in `src/bot.py`
6. Run the bot:
   ```
   python src/bot.py
   ```

## Configuration

You'll need to obtain the following credentials from the Twitter Developer Portal:

- API Key
- API Key Secret
- Access Token
- Access Token Secret
- Bearer Token (for v2 API)

## Usage Examples

### Posting a Tweet

```python
# Post a simple tweet
bot.tweet("Hello, Twitter! This is my automated bot.")

# Post a tweet with media
bot.tweet_with_media("Check out this image!", "path/to/image.jpg")
```

### Searching and Interacting

```python
# Search for tweets with a specific hashtag and retweet them
bot.search_and_retweet("#python", count=5)

# Like tweets containing specific keywords
bot.search_and_like("machine learning", count=10)
```

## Scheduling

The bot uses the `schedule` library to run tasks at specific times:

```python
# Tweet every day at 9:00 AM
schedule.every().day.at("09:00").do(lambda: bot.tweet("Good morning, Twitter!"))

# Retweet #python tweets every 4 hours
schedule.every(4).hours.do(lambda: bot.search_and_retweet("#python", count=3))
```

## Disclaimer

Using automated bots on Twitter must comply with Twitter's Terms of Service and Developer Agreement. Make sure your bot:

- Doesn't spam or abuse the API
- Respects rate limits
- Doesn't engage in prohibited behavior

## License

MIT
