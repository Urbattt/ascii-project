from tkinter import* 

root= Tk()
root.geometry("400x400")
root.title("Ascii Encryption")

enter_word = Entry(root)
label_ascii = Label(root, text="name in ascii : ", bg="light yellow", fg="black")
label_encryption = Label(root, text="name in encryption : ", bg="light yellow", fg="black")

def asciiConverter(): 
    input_word = enter_word.get()
    
    for letter in input_word : 
        label_ascii["text"] += str(ord(letter))+ "  "
        ascii = int(ord(letter))+ "  "
        encrypted= ascii - 1 
        label_encryption["text"] += str(chr(encrypted))+ "  "
        
btn = Button(root, text="Display ascii code and encrypted value", command=asciiConverter)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label_ascii.place(relx=0.5, rely=0.6, anchor=CENTER)
label_encryption.place(relx=0.5, rely=0.7, anchor=CENTER)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()