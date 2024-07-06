import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
from tqdm import tqdm
import platform
import argparse

url = "https://www.amxmodx.org/downloads.php"

# Check GNU/Linux Distro
# Tested on Gentoo/Arch
def check_linux_distro():
    try:
        with open('/etc/os-release', 'r') as file:
            for line in file:
                if line.startswith('ID='):
                    _, dist_name = line.split('=')
                    dist_name = dist_name.strip().strip('"')
                    if dist_name == 'arch' or dist_name == 'gentoo':
                        return True
                    else:
                        return False
    except FileNotFoundError:
        return False

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='AMXXInit - Automate Initial setup of Counter-Strike 1.6 server environment')
    parser.add_argument('--path', type=str, default='.', help='Path to download files (default: current directory)')
    return parser.parse_args()

# Function to download
def download_file(url, filepath):
    print(f"Downloading {url} to {filepath}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024 * 1024  # 1 MB
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=filepath)
        
        with open(filepath, 'wb') as file:
            for data in response.iter_content(chunk_size=block_size):
                progress_bar.update(len(data))
                file.write(data)
            progress_bar.close()
            
        print(f"\nDownloaded {filepath}")
    else:
        print(f"Failed to download {url}")

# Main function
def main():
    if not check_linux_distro():
        print("In development, Only tested on Arch Linux, For now.")
        exit(1)

    # Make sure User eyes in Monitor, Not afk. Manually to press.
    input_text = (
        "Press any key to Continue."
    )

    user_input = input(input_text)

    # Parse command-line arguments
    args = parse_arguments()
    download_path = args.path

    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all <div> tags with the specified style containing the titles
        headers = soup.find_all("div", style="font-weight:bold;margin-bottom:0px;")
        
        titles_to_download = ["Counter-Strike Addon", "AMX Mod X Base"]

        for header in headers:
            title = header.text.strip()
            # Check if the current title is "Metamod"
            if title == "Metamod":
                # Find the <ul> containing the download links
                ul = header.find_next_sibling("ul")
                if ul:
                    # Find all <a> tags within <ul>
                    links = ul.find_all("a")
                    for link in links:
                        download_url = urllib.parse.urljoin(url, link.get("href"))
                        filename = os.path.basename(download_url)
                        # Download the file
                        download_file(download_url, os.path.join(download_path, filename))

            if title in titles_to_download:
                ul = header.find_next_sibling("ul")
                if ul:
                    # Find all <a> tags within <ul>
                    links = ul.find_all("a")
                    for link in links:
                        download_url = urllib.parse.urljoin(url, link.get("href"))
                        filename = os.path.basename(download_url)
                        
                        # Check if the title contains "Linux" in the link text
                        if "Linux" in link.text:
                            download_file(download_url, os.path.join(download_path, filename))

if __name__ == "__main__":
    main()
