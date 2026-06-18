import requests
import colorama

colorama.init(autoreset=True)

def check_username(username):
    platforms = {
        "GitHub": "https://github.com/{}",
        "Twitter": "https://twitter.com/{}",
        "Instagram": "https://instagram.com/{}",
        "Reddit": "https://reddit.com/user/{}",
        "YouTube": "https://www.youtube.com/@{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "Medium": "https://medium.com/@{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "Vimeo": "https://vimeo.com/{}",
        "WordPress": "https://{}.wordpress.com",
        "Blogspot": "https://{}.blogspot.com",
        "Tumblr": "https://{}.tumblr.com",
        "StackOverflow": "https://stackoverflow.com/users/{}",
        "GitLab": "https://gitlab.com/{}",
        "HackerRank": "https://www.hackerrank.com/{}",
        "TryHackMe": "https://tryhackme.com/p/{}",
        "HackerOne": "https://hackerone.com/{}",
        "Chess.com": "https://www.chess.com/member/{}",
        "Lichess": "https://lichess.org/@/{}",
        "AskFM": "https://ask.fm/{}",
        "Bandcamp": "https://bandcamp.com/{}",
        "BitBucket": "https://bitbucket.org/{}/",
        "Facebook": "https://www.facebook.com/{}",
        "Imgur": "https://imgur.com/user/{}",
        "MyAnimeList": "https://myanimelist.net/profile/{}",
        "Pastebin": "https://pastebin.com/u/{}",
        "ProductHunt": "https://www.producthunt.com/@{}",
        "Quora": "https://www.quora.com/profile/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Eksi Sozluk": "https://eksisozluk.com/biri/{}",
        "R10": "https://www.r10.net/members/{}.html",
        "Technopat": "https://www.technopat.net/sosyal/uyeler/{}/",
        "Bionluk": "https://bionluk.com/{}",
        "SadeceOn": "https://www.sadeceon.com/{}",
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': '*/*'
    }

    session = requests.Session()
    session.headers.update(headers)

    print(colorama.Fore.YELLOW + f"\n[*] Scanning '{username}' on social media...\n")
    
    found_count = 0
    
    for name, url_format in platforms.items():
        target_url = url_format.format(username)

        try:
            response = session.get(target_url, timeout=8)
            
            if response.status_code == 200:
                print(colorama.Fore.GREEN + f"[+] {name}: Found → {target_url}")
                found_count += 1
            elif response.status_code == 404:
                pass  # Sessiz geç
            else:
                print(colorama.Fore.YELLOW + f"[?] {name}: Status {response.status_code}")
                
        except Exception as e:
            print(colorama.Fore.RED + f"[!] {name}: Error - {str(e)[:30]}...")
    
    print(colorama.Fore.CYAN + f"\n[*] Total found: {found_count} profiles")