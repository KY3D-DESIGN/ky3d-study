import os
import time
from src.bot import TwitterBot

if __name__ == "__main__":
    print("Starting Twitter/X Bot...")
    
    # Initialize the bot
    bot = TwitterBot()
    
    try:
        # Run the bot's main loop
        bot.run()
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Bot shutdown complete.")
