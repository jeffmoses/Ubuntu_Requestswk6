# Ubuntu_Requests

<h1>How the Script Works
</h1>
<p>The script is a Python program designed to download an image from a URL and save it to a local directory named Fetched_Images. It uses several libraries to perform this task reliably.
</p>
<h2>1. Library Imports
</h2>
<p>os: This library handles interactions with the operating system, specifically for creating directories and managing file paths.
requests: The primary library for making HTTP requests, used here to download the image from the internet.
urllib.parse: This is used to break down the provided URL into its components, which helps in extracting the correct filename.
</p>
<h2>
2. Core Function: download_image(url)
</h2>
<p>
This function contains the main logic. It takes a URL as its argument and performs the following steps:
Directory Management: It first attempts to create a directory named Fetched_Images. The os.makedirs(..., exist_ok=True) command is used to ensure the program doesn't crash if the directory already exists.
Filename Extraction: The script analyzes the URL to find a suitable filename. It uses urlparse() to get the file path and os.path.basename() to extract the filename from the end of the path. unquote() is also used to handle special characters that might be in the URL. If a filename can't be found, a unique, generic one is generated to prevent errors.
Image Download:
It uses requests.get() to initiate the download. The stream=True option is set to download the image in small chunks, which is more memory-efficient for large files.
Error Handling: The critical line response.raise_for_status() automatically checks the HTTP response code. If the code indicates an error (e.g., a 404 "Not Found" error), it raises a requests.exceptions.RequestException, which is caught by the script's error-handling block.
Saving the File:
The script opens a file in the Fetched_Images directory using write binary mode ('wb'). This is crucial for images to prevent data corruption during the save process.
The downloaded content is then written to this file in chunks, ensuring the entire image is saved correctly.
</p>
<h2>
3. Error Handling
</h2>
<p>
The script is wrapped in try...except blocks to handle a variety of potential issues, including:
Network Errors: Problems with the internet connection or the server (e.g., requests.exceptions.RequestException).
File System Errors: Issues with creating the directory or saving the file (IOError).
URL Processing Errors: Problems with parsing a malformed or invalid URL.
</p>
