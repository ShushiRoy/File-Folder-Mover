from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time


class Event(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename
            print('File Received')
            
            new_destination = folder_destination + "\\" + filename
            print('File is currently in starting folder') 
            
            os.rename(src, new_destination)
            print('File has been moved to destination folder')


folder_to_track = r"ENTER STARTING FOLDER PATH HERE"
folder_destination = r"ENTER DESTINATION FOLDER PATH HERE"
event_handler = Event()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
print('Starting up')
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
