
import os
import shutil
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
API_TOKEN = os.getenv("BUZZSPROUT_API_TOKEN")
PODCAST_ID = os.getenv("BUZZSPROUT_PODCAST_ID")
EPISODE_DIR = os.getenv("EPISODE_DIR", "./episodes")
UPLOADED_DIR = os.path.join(EPISODE_DIR, "uploaded")
LOG_FILE = "upload_log.txt"

# Ensure uploaded directory exists
os.makedirs(UPLOADED_DIR, exist_ok=True)

def format_text(text):
    """Replace underscores with spaces and capitalize."""
    return text.replace('_', ' ').strip().capitalize()

def parse_filename(filename):
    """
    Parses the filename to extract title and description.
    Format: title_part.description_part.mp3
    """
    base = os.path.splitext(filename)[0]
    if '.' in base:
        title_part, description_part = base.split('.', 1)
    else:
        title_part = base
        description_part = 'Auto-generated description'
    return format_text(title_part), format_text(description_part)

def log_result(message):
    """Append a message to the log file with timestamp."""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now().isoformat()}] {message}\n")

def upload_file(file_path, title, description):
    """Upload a single MP3 file to Buzzsprout."""
    headers = {
        "Authorization": f"Token {API_TOKEN}"
    }

    with open(file_path, 'rb') as audio_file:
        upload_url = f"https://www.buzzsprout.com/api/{PODCAST_ID}/episodes"
        files = {"audio_file": audio_file}
        data = {"title": title, "description": description}

        print(f"⏳ Uploading: {title}")
        response = requests.post(upload_url, headers=headers, files=files, data=data)

        if response.status_code == 201:
            print(f"✅ Success: {title}")
            log_result(f"✅ Uploaded: {title} | {description}")
            # Move the file to the 'uploaded' folder
            shutil.move(file_path, os.path.join(UPLOADED_DIR, os.path.basename(file_path)))
        else:
            print(f"❌ Failed: {title} - {response.status_code}")
            log_result(f"❌ Failed: {title} | Status Code: {response.status_code} | {response.text}")

def upload_all_podcasts():
    """Scan the directory and upload all .mp3 files."""
    if not os.path.isdir(EPISODE_DIR):
        print(f"❌ Directory not found: {EPISODE_DIR}")
        return

    for filename in os.listdir(EPISODE_DIR):
        file_path = os.path.join(EPISODE_DIR, filename)
        if filename.endswith(".mp3") and os.path.isfile(file_path):
            title, description = parse_filename(filename)
            upload_file(file_path, title, description)

if __name__ == "__main__":
    upload_all_podcasts()
