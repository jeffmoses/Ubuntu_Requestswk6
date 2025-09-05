import os
import requests
from urllib.parse import urlparse, unquote

def download_image(url):
    """
    Downloads an image from a given URL and saves it to a local directory.

    Args:
        url (str): The URL of the image to download.
    """
    # Create the directory if it doesn't exist
    save_dir = "Fetched_Images"
    try:
        os.makedirs(save_dir, exist_ok=True)
        print(f"Directory '{save_dir}' is ready.")
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    # Extract filename from the URL
    try:
        parsed_url = urlparse(url)
        path = unquote(parsed_url.path)
        filename = os.path.basename(path)
        if not filename:
            # Generate a generic filename if the URL doesn't have one
            filename = f"image_{os.urandom(4).hex()}.jpg"
        
        filepath = os.path.join(save_dir, filename)
    except Exception as e:
        print(f"Error processing URL: {e}")
        return

    # Download the image
    try:
        print(f"Attempting to download image from: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Save the image in binary mode
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        
        print(f"Successfully downloaded and saved image as '{filepath}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """
    Main function to run the image fetching tool.
    """
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    image_url = input("Enter the URL of the image you want to download: ")
    download_image(image_url)

if __name__ == "__main__":
    main()