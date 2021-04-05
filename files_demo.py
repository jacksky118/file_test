import os

# 获得单个文件的大小
files_dict = dict()
def getFileSize(file):
    if os.path.exists(file):
        size = os.path.getsize(file)
        files_dict[file] = size


# 列出目录下所有的文件和子目录的文件
def listFiles(path="."):   # 传入路劲默认为当前目录
    if not os.path.exists(path):
        print('path error')
        return None
    file = ''
    try:       # 文件处理会出错，一定要加保护
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            if os.path.isdir(filepath):
                print(filepath)
                listFiles(path=filepath)
            elif os.path.isfile(filepath):
                print(filepath)
                getFileSize(filepath)
    except TypeError:
        print(file)



def displayFilesSize(files=[], size_KB=False, size_MB=False):
    if size_KB:
        return str(round(sum(files)/1024, 2)) + 'K'
    if size_MB:
        return str(round(sum(files)/(1024*1024), 2)) + 'M'
    else:
        return str(round(sum(files),2)) + 'byte'


if __name__ == '__main__':
    my_python = r'E:\project_study'
    listFiles(my_python)
    all_files_size = displayFilesSize(files_dict.values(), size_MB=True)
    print('files num={}, size={}'.format(len(files_dict), all_files_size))
    if len(files_dict)>1:
        new_file_dict = list(zip(files_dict.values(), files_dict.keys()))
        print(max(new_file_dict))
        print(min(new_file_dict))