import os
import shutil
from PIL import Image
#function to check if current file is a image or not
def isimage(file):
    try:
        img = Image.open(file)
        img.close()
        return True
    except:
        return False
def organise_file(parent_folder, destination_folder):
    #iterate all the files present the parent_folder
    for file in os.listdir(parent_folder):

        source_path = os.path.join(parent_folder, file)
        #checking if source_path is file. It should not be the folder
        if os.path.isfile(source_path):
            #get file extension
            _, file_extension = os.path.splitext(file)
            file_extension = file_extension.lower()
            #ignore the hidden files and folder 
            #In linux system as well as windows system hidden file starts with "."
            if file.startswith('.'):
                continue
            #Dividing the files according to there category using their extension
            if isimage(source_path):
                destination = os.path.join(destination_folder, "Images")
            elif file_extension in ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx']:
                destination = os.path.join(destination_folder, "Documents")
            elif file_extension in ['.mp4', '.mkv', '.avi', '.mov']:
                destination = os.path.join(destination_folder, "Videos")
            elif file_extension in ['.mp3', '.mid', '.acc']:
                destination = os.path.join(destination_folder, "Audios")
            elif file_extension in ['.zip', '.rar', '.war']:
                destination = os.path.join(destination_folder, "Zipped_file")
            else:
                destination = os.path.join(destination_folder, "Others")

            os.makedirs(destination, exist_ok= True)
            destination_path = os.path.join(destination, file)

            if not os.path.exists(destination_path):
                shutil.move(source_path, destination_path)
                print(f"Moved {file} to {destination}")
            else :
                print(f"{file} already exist")
if __name__ == "__main__":
    #Give the absolute path for the download_directory and destination_directory
    download_directory = r"C:\Users\Prath\OneDrive\Desktop\Projects\organise_download_python script\source"
    destination_directory = r"C:\Users\Prath\OneDrive\Desktop\Projects\organise_download_python script\destination"

    #Call Organise file function to organise the folder and files present in download_directory
    organise_file(download_directory, destination_directory)
