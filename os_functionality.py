#!/usr/bin/env python3


import os 
import shutil
from datetime import datetime, timedelta


LOG_DIR = os.path.expanduser("~/test_logs")
ARCHIVE_DIR = os.path.expanduser("~/log_archive")
TEMP_DIR = os.path.expanduser("~/temp_files")
DAYS_OLD = 7 #files older than 7 days old will be archived



def archive_old_files(src_dir, dest_dir, days_old):
    now = datetime.now()
    count = 0 

    #ensure archive folders are actually there
    os.makedirs(dest_dir, exist_ok = True)

    for filename in os.listdir(src_dir):
        file_path = os.path.join(src_dir, filename)
        if os.path.isfile(file_path):
            mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if now - mtime > timedelta(days=days_old):
                shutil.move(file_path, os.path.join(dest_dir, filename))
                count += 1
    return count 

def delete_temp_files(temp_dir):
    count = 0 
    if not os.path.exists(temp_dir):
        return count 
    
    for filename in os.path.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            count += 1 
    return count 
    
archived = archive_old_files(LOG_DIR, ARCHIVE_DIR, DAYS_OLD)
deleted = delete_temp_files(TEMP_DIR)

print(f"Archived {archived} old log to files to {ARCHIVE_DIR}")
print(f"Deleted {deleted} temp files from {TEMP_DIR}")


