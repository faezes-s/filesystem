from file import File
from directory import Directory

class FileSystem:
    def __init__(self):
        self.root=Directory("root")#ساخت ریشه فایل سیستم
        self.cwd=self.root
    def make_folder(self,name):
        if name not in self.cwd.folders:#ساخت پوشه جدید
            new_folder=Directory(name,self.cwd)
            self.cwd.folders[name]=new_folder
        else:
            print("folder is not found")
    def make_file(self,name):
        if name not in self.cwd.files:#ساخت فایل جدید
            new_file=File(name)
            self.cwd.files[name]=new_file
        else:
            print("file is not found")

    def list_of_items(self):
        print("folders:")
        for folder in self.cwd.folders:#لیست فایل ها و پوشه های مسیری که توشیم
            print("[DIR]",folder)
        print("files:")
        for file in self.cwd.files:
            print(" ",file)
    def change_folder(self,name):
        if name=="..":
            if self.cwd.parent:#تغییر مسیر پوشه
                self.cwd=self.cwd.parent
            else:
                print("they are in the root")
        elif name in self.cwd.folders:
             self.cwd=self.cwd.folders[name]
        else:
             print("folder is not found")
    def show_address(self):
        print(self.cwd.path())#نمایش مسیری که توشیم

    def read_file(self,name):
        if name in self.cwd.files:
            print(self.cwd.files[name].read())
        else:
            print("file is not found")
    def write_in_file(self,name,text):
        if name in self.cwd.files:
            self.cwd.files[name].write(text)
        else:
            print("file is not found")
    def append_file(self,name,text):
        if name in self.cwd.files:
            self.cwd.files[name].append(text)
        else:
            print("file is not found")
    def edit_file_name(self,name,line,text):
        if name in self.cwd.files:
            try:
                self.cwd.files[name].edit_line(line,text)
            except:
                print("ERROR")
        else:
            print("file is not found")

    def delete_file_line(self,name,line):
        if name in self.cwd.files:
            try:
                self.cwd.files[name].delete_line(line)
            except:
                print("ERROR")
        else:
            print("file is not found")
    def remove(self,name):
        if name in self.cwd.files:#حذف فایل یا پوشه از مسیری که توشیم
            del self.cwd.files[name]
        elif name in self.cwd.folders:
            del self.cwd.folders[name]
        else:
            print("folder or file is not found")
    def rename(self,old,new):
        if old in self.cwd.files:
            if new in self.cwd.files:#تغییر نام پوشه یا فایل
                print("this file already exists")
            else:
                 self.cwd.files[new]=self.cwd.files.pop(old)
                 self.cwd.files[new].filename=new


        elif old in self.cwd.folders:
            if new in self.cwd.folders:
                print("this folder already exists")
            else:
                self.cwd.folders[new]=self.cwd.folders.pop(old)
                self.cwd.folders[new].name=new

        else:
            print("not found")


    def move(self,old,new):
        self.rename(old,new)
    def copy(self,source,destination):
        if source in self.cwd.files:#کپی کردن محتوای یه فایل به فایل دیگه
            base=self.cwd.files[source]
            copied=File(destination)
            copied.data=base.data.copy()
            self.cwd.files[destination]=copied
        else:
            print("file is not found")
    def show_help(self):
        print("these are available commands:")#راهنما
        print("mkdir : make a new folder")
        print("touch : make a new file")
        print("ls : available files and folders")
        print("cd : change the path")
        print("cd .. : return to the parent folder")
        print("pwd :  current address")
        print("write : write content ")
        print("append : add a new content")
        print("cat : read the content")
        print("editline : edit a particular line")
        print("deline : delete a particular line")
        print("rm : delete file/folder")
        print("rename: change the name")
        print("mv : move file/folder")
        print("cp : copy file")
        print("stat : the number of files/folders")
        print("tree : tree of current address")
        print("help : guide")
        print("exit")

    def show_stat(self):
        files_number=len(self.cwd.files)
        folders_number=len(self.cwd.folders)#تعداد فایل ها و پوشه ها
        print(f"number of files:{files_number}")
        print(f"number of folders:{folders_number}")
    def show_tree(self,folder=None,space=""):
        if folder is None:#نمایش درختی از مسیری که توشیم
            folder=self.cwd
        print(space + folder.name + "/")#پوشه ای که توشیم
        for child_folder in folder.folders.values():
            self.show_tree(child_folder,space+"   ")#پوشه های تو در تو
        for file in folder.files:
            print(space+"    " + file)
    def edit_file_line(self,name,index,new_text):
        if name in self.cwd.files:
            self.cwd.files[name].edit_line(index,new_text)
        else:
            print("there is no file")
    def change_the_path(self,full_path):
        if full_path == "/":
            self.cwd=self.root#مسیر کامل میدیم بهش
            self.address=["root"]
            return
        parts=[p for p in full_path.strip("/").split("/") if p]
        current=self.root
        new_path=["root"]
        for p in parts:
            if p in current.folders:
                current=current.folders[p]
                new_path.append(p)
            else:
                print("path is not found")
                return
        self.cwd=current
        self.address=new_path
