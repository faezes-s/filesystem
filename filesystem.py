class  File:
    def __init__(self,filename):
        self.filename=filename
        self.data=[]
    def write(self,text):
        self.data=text.split('\n')
    def append(self,text):
        self.data += text.split('\n')
    def read(self):
        return '\n'.join(self.data)
    def edit_line(self,index,new_text):
        if 0 <= index < len(self.data):
            self.data[index]=new_text
        else:
            print("invalid line number")
    def delete_line(self,index):
        if 0<=index< len(self.data):
            self.data.pop(index)
        else:
            print("invalid line number")



class Directory:
    def __init__(self,name,parent=None):
        self.name=name
        self.parent=parent
        self.folders={}
        self.files={}
    def path(self):
        address=[]
        cwd=self
        while cwd is not None:
            address.append(cwd.name)
            cwd=cwd.parent
        return '/'+'/'.join(reversed(address[:-1]))




class FileSystem:
    def __init__(self):
        self.root=Directory("root")
        self.cwd=self.root
    def make_folder(self,name):
        if name not in self.cwd.folders:
            new_folder=Directory(name,self.cwd)
            self.cwd.folders[name]=new_folder
        else:
            print("folder is not found")
    def make_file(self,name):
        if name not in self.cwd.files:
            new_file=File(name)
            self.cwd.files[name]=new_file
        else:
            print("file is not found")

    def list_of_items(self):
        print("folders:")
        for folder in self.cwd.folders:
            print("[DIR]",folder)
        print("files:")
        for file in self.cwd.files:
            print(" ",file)
    def change_folder(self,name):
        if name=="..":
            if self.cwd.parent:
                self.cwd=self.cwd.parent
            else:
                print("they are in the root")
        elif name in self.cwd.folders:
             self.cwd=self.cwd.folders[name]
        else:
             print("folder is not found")
    def show_address(self):
        print(self.cwd.path())

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
        if name in self.cwd.files:
            del self.cwd.files[name]
        elif name in self.cwd.folders:
            del self.cwd.folders[name]
        else:
            print("folder or file is not found")
    def rename(self,old,new):
        if old in self.cwd.files:
            if new in self.cwd.files:
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
        if source in self.cwd.files:
            base=self.cwd.files[source]
            copied=File(destination)
            copied.data=base.data.copy()
            self.cwd.files[destination]=copied
        else:
            print("file is not found")
    def show_help(self):
        print("these are available commands:")
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
        folders_number=len(self.cwd.folders)
        print(f"number of files:{files_number}")
        print(f"number of folders:{folders_number}")
    def show_tree(self,folder=None,space=""):
        if folder is None:
            folder=self.cwd
        print(space + folder.name + "/")
        for child_folder in folder.folders.values():
            self.show_tree(child_folder,space+"   ")
        for file in folder.files:
            print(space+"    " + file)
    def edit_file_line(self,name,index,new_text):
        if name in self.cwd.files:
            self.cwd.files[name].edit_line(index,new_text)
        else:
            print("there is no file")
    def change_the_path(self,full_path):
        if full_path == "/":
            self.cwd=self.root
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
def main():
    system=FileSystem()
    while True:
        intry=input(f"{system.cwd.path()}$").strip()
        parts=intry.split()
        if not parts:
            continue
        request=parts[0]
        if request=="exit":
            break
        elif request=="mkdir" and len(parts)==2:
            system.make_folder(parts[1])
        elif request=="touch" and len(parts)==2:
            system.make_file(parts[1])
        elif request=="ls":
            system.list_of_items()
        elif request=="cd" and len(parts)==2:
            system.change_folder(parts[1])
        elif request=="pwd":
            system.show_address()
        elif request=="cat" and len(parts)==2:
            system.read_file(parts[1])
        elif request=="write" and len(parts)==2:
            print("enter the text ends with EOF")
            lines=[]
            while True:
                line=input()
                if line.strip()=="EOF":
                    break
                lines.append(line)
            system.append_file(parts[1],'\n'.join(lines))
        elif request=="editline" and len(parts)>=4:
            try:
                line_number=int(parts[2])
                new_text=' '.join(parts[3:])
                system.edit_file_line(parts[1],line_number,new_text)
            except:
                print("invalid line number")
        elif request=="deline" and len(parts)==3:
            try:
                line_number=int(parts[2])
                system.delete_file_line(parts[1],line_number)
            except:
                print("invalid line number")
        elif request=="rm" and len(parts)==2:
            system.remove(parts[1])
        elif request=="rename" and len(parts)==3:
            system.rename(parts[1],parts[2])
        elif request=="mv" and len(parts)==3:
            system.move(parts[1],parts[2])
        elif request=="cp" and len(parts)==3:
            system.copy(parts[1],parts[2])
        elif request=="help":
            system.show_help()
        elif request=="stat":
            system.show_stat()
        elif request=="tree":
            system.show_tree()
        elif request=="append" and len(parts)==2:
            print("enter the text end with EOF")
            lines=[]
            while True:
                line=input()
                if line.strip()=="EOF":
                    break
                lines.append(line)
            system.append_file(parts[1],'\n'.join(lines))
        elif request=="ct" and len(parts)==2:
             system.change_the_path(parts[1])
        else:
            print("invalid request")
if __name__=="__main__":
    main()

