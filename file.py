class  File:
    def __init__(self,filename):
        self.filename=filename
        self.data=[] #محتویات فایل
    def write(self,text):
        self.data=text.split('\n') #محتوای جدید جایگزین میکنه
    def append(self,text):
        self.data += text.split('\n')# محتوای جدید به اخر اضافه میکنه
    def read(self):
        return '\n'.join(self.data) #محتوا رو میخونه
    def edit_line(self,index,new_text):
        if 0 <= index < len(self.data):#ویرایش یه خط خاص
            self.data[index]=new_text
        else:
            print("invalid line number")
    def delete_line(self,index):
        if 0<=index< len(self.data):#حذف یه خط خاص
            self.data.pop(index)
        else:
            print("invalid line number")


