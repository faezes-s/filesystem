from filesystem import FileSystem



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

