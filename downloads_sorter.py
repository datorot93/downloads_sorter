from os import listdir
from os.path import isfile, join
from pathlib import Path




def move_files(my_downloads, file_type_dic, my_downloads_path):
    """ Move each file to its corresponding folder, depending of its type"""
    
    for file in my_downloads:
        if len(file.split(".")) > 1 or file.split(".")[0] not in ['documents', 'images', 'modeling', 'multimedia', 'others']:
            file_extension = file.split('.')[-1]
            origin_path = my_downloads_path / file
            if file_extension in file_type_dic.values():
                for file_types in file_type_dic:
                    destination_path = my_downloads_path / file_types / file
                    if file.split('.')[-1] in file_type_dic[file_types]:
                        Path(origin_path).rename(destination_path)
            else:
                destination_path = my_downloads_path / "others" 
                Path(my_downloads_path / file).rename(destination_path / file)


def create_destination_folders(downloads_path, types_file_dic):
    """ Create, if not exist, the destination folders to storage my downloaded files """
    for folder in types_file_dic:
        if not Path(downloads_path + '/' + folder).exists():
            Path(downloads_path + '/' + folder).mkdir()
        else:
            continue

if __name__ == '__main__':
    # Variables definition
    # Paths
    downloads_path = 'c:/Users/herri/Downloads'
    my_downloads_path = Path(downloads_path)
    my_downloads = listdir(my_downloads_path)
    print(my_downloads_path)
    # list of extensions
    file_type_dic = {
        "documents": ['xlsx', 'pdf', 'docx', 'txt', 'pptx', 'csv', 'json', 'xml', 'accdb', 'md', 'iqy', 'epub', 'xlsm', 'xlsb', 'xls'],
        "images": ['jpg', 'jpeg', 'png', 'svg', 'tiff', 'gif', 'bmp'],
        "modeling": ['bpm', 'pbix'],
        "multimedia": ['avi', 'mp4', 'mp3', 'mpeg'],
        "others": []   
    }

    # Methods called
    create_destination_folders(downloads_path, file_type_dic)
    move_files(my_downloads, file_type_dic, my_downloads_path)
