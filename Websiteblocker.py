from tkinter import *
host_path=r"C:\Windows\System32\drivers\etc\hosts" 
ip_address='127.0.0.1'

def block():
    ws_list=en1.get(1.0,END)
    ws=list(ws_list.split(","))
    with open(host_path, 'r+') as host_file:
        file=host_file.read()
        for w in ws:
            if w in file:
                Label(root,text="Already Blocked!",font=('Arial,bold',15),bg='#515151',fg='White').place(x=100,y=160)
                pass
            else:
                host_file.write(ip_address + " " + w + '\n')
                Label(root,text="Website is Blocked",font=('Arial,bold',15),bg='#515151',fg='White').place(x=90,y=160)

def unblock():
    ws_list = en1.get(1.0, END)
    ws = list(ws_list.split(","))
    with open(host_path, 'r+') as host_file:
        lines = host_file.readlines()
        host_file.seek(0)
        for line in lines:
            if not any(w in line for w in ws):
                host_file.write(line)
        host_file.truncate()
    Label(root, text="Website is Unblocked", font=('Arial,bold', 15), bg='#515151', fg='White').place(x=90, y=160)


root=Tk()
root.geometry("350x250")
root.resizable(False,False)
root.title("Website Blocker")
root.config(bg='#D3D3D3')
lb1=Label(root,text="Website Blocker",font=('Arial,bold',20),bg='#8B8B7A',fg='White',width=30)
lb1.pack(pady=10)
lb2=Label(root,text="Enter the Website",font=('Arial,bold',15),bg='#D3D3D3')
lb2.pack()
en1=Text(root,font=('Arial,bold',15),relief=SOLID,width=30,height=2)
en1.pack()
btn1=Button(root,text="Block",font=('Arial,bold',15),bg='#8B8B7A',fg='White',padx=10,command=block)
btn1.place(x=80,y=200)
btn2=Button(root,text="Unblock",font=('Arial,bold',15),bg='#8B8B7A',fg='White',padx=2,command=unblock)
btn2.place(x=180,y=200)


root.mainloop()
