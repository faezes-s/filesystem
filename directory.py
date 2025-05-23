class Directory:
    def __init__(self,name,parent=None):
        self.name=name
        self.parent=parent
        self.folders={}#پوشه های این دایرکتوری
        self.files={}#فایل های  این دایرکتوری
    def path(self):
        address=[]
        cwd=self
        while cwd is not None:
            address.append(cwd.name)
            cwd=cwd.parent
        return '/'+'/'.join(reversed(address[:-1]))#مسیر کامل دایرکتوری


