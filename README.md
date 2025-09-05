# Ubuntu_Requests

**How the Script Works**

    Imports: It imports the necessary libraries: os for interacting with the file system, requests for making HTTP requests, and urlparse and unquote from urllib.parse to handle URL string manipulation.

    Function download_image(url): This function contains the core logic. It takes a URL as an argument.

    Directory Creation: **os.makedirs(save_dir, exist_ok=True)** creates the Fetched_Images directory. The exist_ok=True argument prevents the script from raising an error if the directory already exists.

    Filename Extraction: urlparse(url) breaks down the URL into components. os.path.basename() extracts the final part of the path, which is usually the filename. unquote() is used to handle URL-encoded characters (like spaces) in the filename. If no filename is found, a unique one is generated using os.urandom().

    Downloading:

        requests.get(url, stream=True) initiates the download. Using stream=True allows the script to download the image in chunks, which is more memory-efficient for large files.

        response.raise_for_status() is a crucial line that automatically checks if the HTTP response status code indicates an error (e.g., 404 Not Found, 500 Server Error). If it does, it raises a RequestException.

    Saving the File: with open(filepath, 'wb') as file: opens the file in write binary mode ('wb'). This is essential for images and other non-text files to prevent data corruption. The for loop then writes the downloaded content in small chunks to the file.

    Error Handling: The try...except blocks gracefully handle potential issues, such as network errors (requests.exceptions.RequestException), file system problems (IOError), or invalid URLs.

This script provides a robust and user-friendly way to download and manage images from the web.
