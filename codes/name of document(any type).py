def name_of_document(path):
    s1=path[::-1]           # reversing the string
    for i in range(len(s1)):
        if s1[i]==".":
            a=i             # index of "." in reversed string
        if s1[i]=="/":
            b=i             # index of first "/" in reversed string        
            break
    return path[len(path)-b:len(path)-(a+1)]   #slicing of original string in the range of "/" and "."
path='C:/Users/AMAN SHAKYA/Desktop/New Microsoft Word Document.docx'
print(name_of_document(path))
