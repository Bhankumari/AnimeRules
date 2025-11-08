#!/usr/bin/env python3
"""
Update rules.json based on environment variables or schedule.
"""

import json
import os
import sys

def update_rules():
    """Update rules.json with subscription and rating values."""
    
    # Get values from environment variables
    subscription_str = os.environ.get('SUBSCRIPTION', 'true').lower()
    rating_str = os.environ.get('RATING', 'false').lower()
    
    # Convert string to boolean
    subscription = subscription_str == 'true'
    rating = rating_str == 'true'
    
    # Read current rules
    try:
        with open('rules.json', 'r') as f:
            rules = json.load(f)
    except FileNotFoundError:
        rules = {}
    except json.JSONDecodeError as e:
        print(f"Error reading rules.json: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Update values
    rules['subscription'] = subscription
    rules['rating'] = rating
    
    # Write back to file
    try:
        with open('rules.json', 'w') as f:
            json.dump(rules, f, indent=2)
            f.write('\n')  # Add newline at end of file
        print(f"Updated rules.json: subscription={subscription}, rating={rating}")
    except Exception as e:
        print(f"Error writing rules.json: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    update_rules()

