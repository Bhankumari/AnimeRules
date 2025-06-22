#!/usr/bin/env python3
"""
Update rules.json based on USA time schedule:
- 9 AM to 10 PM USA time: rating=false, subscription=true
- 10 PM to 9 AM USA time: rating=true, subscription=false
"""

import json
import pytz
from datetime import datetime

def get_usa_time():
    """Get current time in USA Eastern timezone"""
    usa_tz = pytz.timezone('US/Eastern')
    return datetime.now(usa_tz)

def should_be_active_hours(current_time):
    """
    Check if current time is within active hours (9 AM - 10 PM USA time)
    Returns True if within active hours, False otherwise
    """
    hour = current_time.hour
    return 9 <= hour < 22  # 9 AM to 10 PM (22:00)

def update_rules():
    """Update rules.json based on current USA time"""
    
    # Get current USA time
    usa_time = get_usa_time()
    print(f"Current USA Eastern time: {usa_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    
    # Determine if we're in active hours
    is_active_hours = should_be_active_hours(usa_time)
    print(f"Is active hours (9 AM - 10 PM): {is_active_hours}")
    
    # Set rules based on time
    if is_active_hours:
        # 9 AM to 10 PM: rating false, subscription true
        new_rating = False
        new_subscription = True
        print("Setting: rating=false, subscription=true (active hours)")
    else:
        # 10 PM to 9 AM: rating true, subscription false
        new_rating = True
        new_subscription = False
        print("Setting: rating=true, subscription=false (inactive hours)")
    
    # Read current rules
    try:
        with open('rules.json', 'r') as f:
            rules = json.load(f)
    except FileNotFoundError:
        print("rules.json not found, creating new file")
        rules = {}
    except json.JSONDecodeError:
        print("Invalid JSON in rules.json, creating new structure")
        rules = {}
    
    # Check if update is needed
    current_rating = rules.get('rating')
    current_subscription = rules.get('subscription')
    
    if current_rating == new_rating and current_subscription == new_subscription:
        print("No update needed - rules are already correct")
        return
    
    # Update rules
    rules['rating'] = new_rating
    rules['subscription'] = new_subscription
    
    # Write updated rules
    with open('rules.json', 'w') as f:
        json.dump(rules, f, indent=2)
    
    print(f"Updated rules.json: rating={new_rating}, subscription={new_subscription}")

if __name__ == "__main__":
    update_rules() 