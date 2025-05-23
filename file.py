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


