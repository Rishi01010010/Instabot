# 📸 InstaBot: Automate Your Instagram Posts 📸

Welcome to *InstaBot*, a powerful automation tool designed to simplify posting images on Instagram. This project combines a Python-based Selenium script (`instabot.py`) for browser automation with a Node.js server (`server.js`) to handle image uploads via a web interface. Whether you're a content creator or a social media manager, InstaBot streamlines the process of posting images, saving you time and effort.

## 🔍 Project Overview

Manually posting images on Instagram can be tedious, especially for frequent uploads. *InstaBot* automates this process by logging into your Instagram account, uploading an image, and posting it—all with minimal user intervention. The system uses Selenium with Firefox for browser automation and a Node.js server with Express to handle image uploads through a web interface, making it both user-friendly and efficient.

### ✨ Key Features:

- *Automated Posting:* Upload and post images to Instagram programmatically.
- *Web Interface:* Simple frontend to upload images and trigger posts.
- *Headless Support:* Options for both headful and headless browser modes.
- *Error Handling:* Robust handling of Instagram popups (e.g., "Save Login Info," "Notifications").
- *Temporary File Management:* Securely handles uploaded images with cleanup.

## 🚀 Getting Started

### 1. *Prerequisites:*
- **Python 3.x** and **Node.js** (with npm) installed on your system.
- **Firefox browser** installed (path: `C:/Program Files/Mozilla Firefox/firefox.exe`).
- **GeckoDriver** (automatically installed via `webdriver_manager`).
- Required Python libraries: `selenium`, `webdriver_manager`.
- Required Node.js packages: `express`, `multer`.

### 2. *Setting Up:*

- Clone the repository (if hosted on GitHub):
  ```bash
  git clone https://github.com/your-username/InstaBot.git
  cd InstaBot
  ```

- Install Python dependencies:
  ```bash
  pip install selenium webdriver_manager
  ```

- Install Node.js dependencies:
  ```bash
  npm install
  ```

- Update credentials in `instabot.py`:
  - Replace `username` and `password` with your Instagram credentials:
    ```python
    username = 'your_username'
    password = 'your_password'
    ```

- Ensure Firefox is installed at the specified path in `instabot.py`.

### 3. *Running the System:*

#### Option 1: Using the Web Interface (Recommended)
- Start the Node.js server:
  ```bash
  node server.js
  ```
- Open a web browser and navigate to `http://localhost:3000`.
- Upload an image using the form on `public/index.html`.
- The server will trigger `instabot.py` to post the image to Instagram.

#### Option 2: Running the Python Script Directly
- Run the Python script with an image path:
  ```bash
  python instabot.py path/to/your/image.jpg
  ```
- Example:
  ```bash
  python instabot.py image_to_post/gan.png
  ```

### 4. *Sample Output:*
- **Web Interface Success:**
  ```
  Photo posted successfully!
  ```
- **Python Script Logs:**
  ```
  Clicked 'Not Now' on Save Login Info popup
  Clicked 'Not Now' on notifications popup
  Clicked 'Create' button in the navbar
  Clicked 'Post' button in the navbar
  Uploaded image from /path/to/image.jpg
  Clicked 'Next' button after entering caption
  Clicked 'Next' button after the first 'Next'
  Clicked 'Share' button to post the image
  Post has been shared successfully!
  ```

## 💾 Directory Structure

```
InstaBot/
│
├── geckodriver.log              # Log file for GeckoDriver
├── import time.txt              # Miscellaneous file (possibly a script fragment)
├── InstaBot - Head.py           # Headful version of the bot
├── InstaBot - Headless.py       # Headless version of the bot
├── instabot.py                  # Main Python script for Instagram automation
├── package-lock.json            # npm dependency lock file
├── package.json                 # Project dependencies and scripts
├── README.md                    # Project documentation
├── server.js                    # Node.js server for handling uploads
│
├── config/                      # Configuration and log files
│   ├── blacklist.txt            # List of blacklisted users
│   ├── comments.txt             # Predefined comments
│   ├── followed.txt             # List of followed users
│   ├── friends.txt              # List of friends
│   ├── risheek_r_.checkpoint    # Checkpoint file for user risheek_r_
│   ├── risheek_r__uuid_and_cookie.json # UUID and cookie data for user
│   ├── skipped.txt              # List of skipped actions
│   ├── unfollowed.txt           # List of unfollowed users
│   ├── whitelist.txt            # List of whitelisted users
│   │
│   └── log/                     # Log files for bot activity
│       ├── instabot_1289106819728.log # Log file
│       ├── instabot_1760352537232.log # Log file
│       └── ...                  # Additional log files
│
├── image_to_post/               # Directory for images to post
│   └── gan.png                  # Sample image
│
├── new/                         # Development/experimental files
│   ├── index.html               # Experimental HTML file
│   ├── index_old_old.html       # Older version of index.html
│   ├── InstaBot - Headless.py   # Headless bot script
│   ├── instabot.py              # Copy of main script
│   ├── script.js                # Experimental JavaScript
│   ├── server.js                # Experimental server script
│   └── styles.css               # Experimental CSS
│
├── public/                      # Frontend assets
│   ├── index.html               # Main web interface
│   └── script.js                # JavaScript for frontend
│
└── uploads/                     # Temporary storage for uploaded images
    ├── 1e543e393e533be44529eda1f1575327 # Uploaded image
    ├── 30ae6fc98cfa9f016ff71d4d6425d07d # Uploaded image
    └── ...                          # Additional uploaded images
```

### 📝 Code Explanation

1. **instabot.py**:
   - Uses Selenium with Firefox to automate Instagram login and posting.
   - Handles popups ("Save Login Info," "Notifications") and navigates through Instagram’s UI to upload and post an image.
   - Supports command-line arguments for specifying the image path.

2. **server.js**:
   - Sets up a Node.js server with Express to handle image uploads via a web interface.
   - Uses `multer` to process uploaded files and `child_process` to spawn the `instabot.py` script.
   - Manages temporary files in the system’s temp directory, ensuring cleanup after processing.

3. **public/index.html & script.js**:
   - Provides a simple web interface for uploading images.
   - Sends the uploaded image to the server via a POST request to `/upload`.

## 🌐 System Design

- **Frontend:** HTML and JavaScript (`public/index.html`, `script.js`) for image uploads.
- **Backend:** Node.js with Express (`server.js`) to handle uploads and trigger the Python script.
- **Automation:** Python with Selenium (`instabot.py`) to interact with Instagram’s UI.
- **Temporary Storage:** Uses the system’s temp directory for handling uploaded images.

## 🛠️ How It Works

1. *Upload Image:* Use the web interface to upload an image.
2. *Server Processing:* The Node.js server saves the image temporarily and triggers `instabot.py`.
3. *Instagram Automation:* The Python script logs into Instagram, navigates to the post creation page, uploads the image, and shares it.
4. *Cleanup:* The server deletes the temporary file after processing.

## 🎯 Project Intent

*InstaBot* aims to automate Instagram posting, making it easier for users to share content without manual intervention. It’s ideal for social media managers, influencers, or anyone looking to streamline their posting workflow.

## 🔧 Customization

Enhance the project with these ideas:
- *Caption Support:* Uncomment and modify the caption section in `instabot.py` to add custom captions.
- *Headless Mode:* Use `InstaBot - Headless.py` for running in headless mode (no browser UI).
- *Scheduling:* Add a scheduling feature to post images at specific times.
- *Error Reporting:* Improve error handling with detailed user feedback.
