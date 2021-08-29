from os import listdir
from os.path import isfile, join
from pathlib import Path




def list_downloaded_files(my_downloads):
    print('*' * 50)
    # print(len(my_downloads))
    for file in my_downloads:
        print(file)

if __name__ == '__main__':
    # Variables definition
    # Paths
    downloads_path = '/mnt/c/Users/herri/Downloads'
    my_downloads_path = Path(downloads_path)
    my_downloads = listdir(my_downloads_path)

    # list of extensions
    types_file_dic = {
        "documents": ['xlsx', 'pdf', 'docx', 'txt', 'pptx', 'csv', 'json', 'xml', 'accdb', 'md', 'iqy', 'epub'],
        "images": ['jpg', 'jpeg', 'png', 'svg', 'tiff', 'gif', 'bmp'],
        "modeling": ['bpm', 'pbix'],
        "multimedia": ['avi', 'mp4', 'mp3', 'mpeg'],
        "others": []
    }
    # documents = ['xlsx', 'pdf', 'docx', 'txt', 'pptx', 'csv', 'json', 'xml', 'accdb', 'md', 'iqy', 'epub']
    # images = ['jpg', 'jpeg', 'png', 'svg', 'tiff', 'gif', 'bmp']
    # multimedia = ['avi', 'mp4', 'mp3', 'mpeg']
    # modeling = ['bpm', 'pbix']
    # executables = ['exe']


    list_downloaded_files(my_downloads)

    # Methods called


