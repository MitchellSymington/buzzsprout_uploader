
# Buzzsprout Podcast Batch Uploader

This script automates uploading multiple podcast episodes to Buzzsprout using their API.

---

## 📂 Folder Structure

- `buzzsprout_upload_parsing.py` → main script
- `.env` → environment config file
- `episodes/` → put your .mp3 files here
- `episodes/uploaded/` → where uploaded files will be moved
- `upload_log.txt` → log file with upload history

---

## 🧾 File Naming Format

Each `.mp3` file must follow this format:
```
title_part.description_part.mp3
```

Example:
```
episode_0001_teaser.description_of_episode.mp3
```

Will become:
- **Title**: `Episode 0001 teaser`
- **Description**: `Description of episode`

---

## ✅ Requirements

- Python 3
- Install dependencies:
```
pip install requests python-dotenv
```

---

## 💻 How to Use

1. Place all your `.mp3` files in the `episodes/` folder
2. Edit `.env` with your Buzzsprout token and podcast ID
3. Run the script:
```
python buzzsprout_upload_parsing.py
```

Each episode will be:
- Uploaded to Buzzsprout
- Moved to `episodes/uploaded/`
- Logged in `upload_log.txt`

---

## 🔒 Notes

- Be sure your API token has the correct permissions
- Only files with `.mp3` extension will be processed
- Errors are logged with timestamps

---

Created to save time and simplify podcast publishing.
