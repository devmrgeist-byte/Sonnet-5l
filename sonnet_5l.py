# Sonnet-5L - Instagram Username Availability Checker
# Author: Mr Geist
# A sophisticated tool for checking 5-letter Instagram username availability

import webbrowser
import requests 
import random
import datetime
import sys 
import time

# Color Palette - Aesthetic & Professional with Gradient Effects
class Colors:
    # Vibrant Gradient Colors
    RED = '\033[1;38;2;255;95;95m'        # Vibrant Red
    ORANGE = '\033[1;38;2;255;159;28m'    # Warm Orange
    GREEN = '\033[1;38;2;120;220;120m'    # Fresh Green
    BLUE = '\033[1;38;2;100;180;255m'     # Sky Blue
    PURPLE = '\033[1;38;2;180;120;255m'   # Soft Purple
    CYAN = '\033[1;38;2;80;220;220m'      # Electric Cyan
    PINK = '\033[1;38;2;255;120;200m'     # Bright Pink
    GOLD = '\033[1;38;2;255;200;50m'      # Shimmering Gold
    WHITE = '\033[1;38;2;240;240;240m'    # Clean White
    GRAY = '\033[1;38;2;160;160;160m'     # Medium Gray
    YELLOW = '\033[1;38;2;255;255;100m'   # Bright Yellow
    LIME = '\033[1;38;2;180;255;100m'     # Lime Green
    RESET = '\033[0m'

# Emoji Collection
class Emojis:
    SUCCESS = "✨"
    ERROR = "💥"
    WARNING = "⚠️"
    INFO = "💡"
    SEARCH = "🔍"
    FOUND = "🎯"
    LOCK = "🔒"
    UNLOCK = "🔓"
    FIRE = "🔥"
    STAR = "⭐"
    HEART = "💖"
    ROCKET = "🚀"
    GHOST = "👻"
    MAGIC = "🎩"
    CROWN = "👑"
    ZAP = "⚡"
    SPARKLES = "🌟"
    TADA = "🎉"
    COMPASS = "🧭"
    HOURGLASS = "⏳"
    CLOCK = "⏰"
    GEM = "💎"

# Banner Art with Author Credit
def display_banner():
    banner = f"""
{Colors.PURPLE}╔════════════════════════════════════════════════════════════════════╗
{Colors.PURPLE}║{Colors.CYAN}    ███████ ██████  ███    ██ ███    ██ ███████ ████████ {Colors.PINK}   {Emojis.GEM} {Colors.PURPLE}║
{Colors.PURPLE}║{Colors.CYAN}    ██      ██   ██ ████   ██ ████   ██ ██         ██    {Colors.PINK}   {Emojis.MAGIC} {Colors.PURPLE}║
{Colors.PURPLE}║{Colors.CYAN}    ███████ ██████  ██ ██  ██ ██ ██  ██ █████      ██    {Colors.PINK}   {Emojis.CROWN} {Colors.PURPLE}║
{Colors.PURPLE}║{Colors.CYAN}         ██ ██   ██ ██  ██ ██ ██  ██ ██ ██         ██    {Colors.PINK}   {Emojis.ZAP} {Colors.PURPLE}║
{Colors.PURPLE}║{Colors.CYAN}    ███████ ██   ██ ██   ████ ██   ████ ███████    ██    {Colors.PINK}   {Emojis.SPARKLES} {Colors.PURPLE}║
{Colors.PURPLE}║{Colors.GOLD}             5-Letter Username Scanner {Emojis.ROCKET}              {Colors.PURPLE}║
{Colors.PURPLE}║{Colors.PINK}                 Author: {Colors.CYAN}Mr Geist {Emojis.GHOST} {Colors.PINK}                        {Colors.PURPLE}║
{Colors.PURPLE}╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

# Character sets for username generation
insta_chars = "1234567890qwertyuiopasdfghjklzxcvbnm"
all_chars = "qwertyuiopasdfghjkzxcvbnm"

#------------------------- Sonnet-5L Core Engine ---------------------------#
def check_instagram_username(user):
    """
    Check availability of 5-letter Instagram username
    Returns: Boolean (True if available, False if taken)
    """
    url = requests.post(
        'https://www.instagram.com/accounts/web_create_ajax/attempt/',
        headers = {
            'Host': 'www.instagram.com',
            'content-length': '85',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'sec-ch-ua-mobile': '?0',
            'x-instagram-ajax': '81f3a3c9dfe2',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'x-asbd-id': '198387',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
            'x-csrftoken': 'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
            'sec-ch-ua-platform': '"Linux"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IQ,en;q=0.9',
            'cookie': 'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv; mid=YtsQ1gABAAEszHB5wT9VqccwQIUL; ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425; ig_nrcb=1'
        },
        data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false'
    )
    
    # Check response for username availability
    if '{"message":"feedback_required","spam":true,' in url.text:
        print(f"{Colors.GRAY}[{Colors.RED}{Emojis.ERROR}{Colors.GRAY}] {Colors.RED}RATE LIMITED {Emojis.LOCK}{Colors.GRAY} : {Colors.WHITE}{user} {Colors.RED}(Try again later){Colors.RESET}")
        return False
    elif '"errors": {"username":' in url.text or '"code": "username_is_taken"' in url.text:
        print(f"{Colors.GRAY}[{Colors.ORANGE}{Emojis.WARNING}{Colors.GRAY}] {Colors.ORANGE}UNAVAILABLE {Emojis.LOCK}{Colors.GRAY} : {Colors.WHITE}{user}{Colors.RESET}")
        return False
    else:
        print(f"{Colors.GRAY}[{Colors.GREEN}{Emojis.SUCCESS}{Colors.GRAY}] {Colors.LIME}AVAILABLE! {Emojis.UNLOCK}{Colors.GRAY}   : {Colors.CYAN}{user} {Colors.YELLOW}{Emojis.STAR}{Emojis.FIRE}{Emojis.HEART}{Colors.RESET}")
        return True

def generate_5l_usernames():
    """
    Generate random 5-letter username combinations
    Returns: Generator of username strings
    """
    while True:
        v1 = str(''.join((random.choice(insta_chars) for i in range(1))))
        v2 = str(''.join((random.choice(insta_chars) for i in range(1))))
        v3 = str(''.join((random.choice(insta_chars) for i in range(1))))
        v4 = str(''.join((random.choice(insta_chars) for i in range(1))))
        v5 = str(''.join((random.choice(all_chars) for i in range(1))))
        
        # Create variations with the letter in different positions
        user1 = (v5 + v1 + v2 + v3 + v4)  # Letter at start
        user2 = (v1 + v5 + v2 + v3 + v4)  # Letter in position 2
        user3 = (v1 + v2 + v5 + v3 + v4)  # Letter in position 3  
        user4 = (v1 + v2 + v3 + v5 + v4)  # Letter in position 4
        
        username_variations = (user1, user2, user3, user4)
        username = random.choice(username_variations)
        yield username

def print_separator():
    """Print colorful separator"""
    separators = [
        f"{Colors.PURPLE}✦{Colors.CYAN}•{Colors.PINK}✧{Colors.BLUE}•{Colors.GREEN}✦{Colors.YELLOW}•{Colors.ORANGE}✧{Colors.RED}•{Colors.PURPLE}✦",
        f"{Colors.CYAN}♡{Colors.PINK}〜{Colors.PURPLE}♡{Colors.BLUE}〜{Colors.GREEN}♡{Colors.YELLOW}〜{Colors.ORANGE}♡{Colors.RED}〜{Colors.CYAN}♡",
        f"{Colors.GOLD}⚡{Colors.PURPLE}➜{Colors.CYAN}⚡{Colors.PINK}➜{Colors.BLUE}⚡{Colors.GREEN}➜{Colors.YELLOW}⚡{Colors.ORANGE}➜{Colors.RED}⚡"
    ]
    print(random.choice(separators))

def main():
    """Main execution function"""
    display_banner()
    
    print(f"{Colors.GOLD}{Emojis.ROCKET} {Colors.YELLOW}Initializing Sonnet-5L Scanner... {Emojis.ZAP}{Colors.RESET}")
    print(f"{Colors.CYAN}{Emojis.CLOCK} {Colors.WHITE}Started at: {Colors.PINK}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
    print(f"{Colors.BLUE}{Emojis.SEARCH} {Colors.WHITE}Scanning 5-letter username patterns...{Colors.RESET}")
    print(f"{Colors.GREEN}{Emojis.COMPASS} {Colors.WHITE}Powered by: {Colors.CYAN}Mr Geist {Emojis.GHOST}{Colors.RESET}")
    print_separator()
    
    try:
        username_generator = generate_5l_usernames()
        available_count = 0
        scan_count = 0
        
        while True:
            username = next(username_generator)
            scan_count += 1
            
            if check_instagram_username(username):
                available_count += 1
                print(f"{Colors.GOLD}{Emojis.TADA} {Colors.LIME}Found {available_count} available username(s)! {Emojis.SPARKLES}{Colors.RESET}")
                print_separator()
            
            # Show progress every 10 scans
            if scan_count % 10 == 0:
                print(f"{Colors.PURPLE}{Emojis.HOURGLASS} {Colors.WHITE}Scanned: {Colors.CYAN}{scan_count} {Colors.WHITE}usernames | {Colors.GREEN}Found: {Colors.LIME}{available_count} {Colors.WHITE}available {Emojis.GEM}{Colors.RESET}")
                print_separator()
                
            time.sleep(0.5)  # Rate limiting
                
    except KeyboardInterrupt:
        print_separator()
        print(f"{Colors.GREEN}{Emojis.SUCCESS} {Colors.LIME}Scan completed successfully! {Emojis.TADA}{Colors.RESET}")
        print(f"{Colors.BLUE}{Emojis.GEM} {Colors.CYAN}Total scanned: {Colors.WHITE}{scan_count} {Colors.CYAN}usernames{Colors.RESET}")
        print(f"{Colors.GOLD}{Emojis.STAR} {Colors.YELLOW}Available found: {Colors.LIME}{available_count} {Colors.YELLOW}premium names{Colors.RESET}")
        print(f"{Colors.PINK}{Emojis.HEART} {Colors.PURPLE}Thank you for using Sonnet-5L by Mr Geist! {Emojis.GHOST}{Colors.RESET}")
        print_separator()
        sys.exit(0)

if __name__ == "__main__":
    main()
