"""
Content generator for Twitter/X bot.
This module provides functions to generate content for tweets.
"""
import random
import datetime

# Sample content categories - customize these based on your needs
TECH_TIPS = [
    "Remember to back up your code regularly! #CodeTip #DevLife",
    "Learning a new programming language? Start with small projects to build confidence. #CodingAdvice",
    "Keyboard shortcuts save time. Learn the ones for your favorite IDE. #ProductivityTip",
    "Code reviews aren't just for catching bugs—they're for knowledge sharing too! #TeamDevelopment",
    "Regular expressions are powerful but use them wisely. #RegEx #DeveloperTips"
]

PORTFOLIO_HIGHLIGHTS = [
    "Check out my latest web development project: [Insert link] #WebDev #Portfolio",
    "Just launched a new responsive design for a client! See it here: [Insert link] #WebDesign",
    "Proud to share my latest app development case study: [Insert link] #AppDev #CaseStudy",
    "New blog post about my development process: [Insert link] #DevBlog #BehindTheScenes",
    "Recently completed a challenging e-commerce project: [Insert link] #ECommerce #Portfolio"
]

PRINTING_CONTENT = [
    "3D printing tip: Always level your bed before starting a new print! #3DPrinting #MakerTips",
    "Check out this amazing 3D printed prototype I just finished: [Insert link] #3DPrinting #ProductDesign",
    "New filament review on my blog: [Insert link] #3DPrinting #FilamentReview",
    "Time-lapse of my latest 3D printing project: [Insert link] #3DPrinting #TimeLapse",
    "Just added new 3D printed products to my store! Check them out: [Insert link] #3DPrinting #ECommerce"
]

PROMOTIONAL_CONTENT = [
    "Limited time offer on my freelance services! DM for details. #FreelanceDev #SpecialOffer",
    "Need a custom 3D printed solution? I'm taking new clients this month! #3DPrinting #CustomDesign",
    "Use code 'TWITTER10' for 10% off your first order in my online store! #Discount #LimitedOffer",
    "Now booking development projects for next month. Spots filling fast! #HireMe #FreelanceDev",
    "Flash sale on all 3D printed items in my store this weekend! #Sale #3DPrinting"
]

def get_random_tweet(category=None):
    """
    Get a random tweet from either a specific category or any category.
    
    Args:
        category (str, optional): Category to select from. Defaults to None (random category).
    
    Returns:
        str: A randomly selected tweet content.
    """
    if category == "tech":
        return random.choice(TECH_TIPS)
    elif category == "portfolio":
        return random.choice(PORTFOLIO_HIGHLIGHTS)
    elif category == "printing":
        return random.choice(PRINTING_CONTENT)
    elif category == "promo":
        return random.choice(PROMOTIONAL_CONTENT)
    else:
        # Choose a random category
        all_content = TECH_TIPS + PORTFOLIO_HIGHLIGHTS + PRINTING_CONTENT + PROMOTIONAL_CONTENT
        return random.choice(all_content)

def get_scheduled_content():
    """
    Get content based on the day of the week for scheduled posting.
    
    Returns:
        str: Content appropriate for the current day.
    """
    today = datetime.datetime.now().weekday()
    
    # Monday: Tech tips
    if today == 0:
        return random.choice(TECH_TIPS)
    # Tuesday & Thursday: Portfolio highlights
    elif today in [1, 3]:
        return random.choice(PORTFOLIO_HIGHLIGHTS)
    # Wednesday: 3D Printing content
    elif today == 2:
        return random.choice(PRINTING_CONTENT)
    # Friday: Promotional content
    elif today == 4:
        return random.choice(PROMOTIONAL_CONTENT)
    # Weekend: Mix of everything
    else:
        return get_random_tweet()

def generate_trending_hashtags():
    """
    Generate a list of sample trending hashtags related to tech and 3D printing.
    In a real implementation, this would fetch actual trending hashtags.
    
    Returns:
        list: Sample trending hashtags.
    """
    hashtags = [
        "#TechTuesday", "#WebDevelopment", "#CodeLife", "#3DPrinting", 
        "#MakerMovement", "#FreelanceDeveloper", "#ECommerce", 
        "#DigitalCreator", "#CodeNewbie", "#TechInnovation"
    ]
    return random.sample(hashtags, 3)  # Return 3 random hashtags
