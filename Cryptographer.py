from tkinter import *
from tkinter import ttk
import pyperclip
import base64
import binary_code

main = Tk(className = "Шифры")
main.geometry('1000x600')
main.colormapwindows()


alphavit_ru = [ 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я' ]
alphavit_Ru = [ 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я' ]
alphavit_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphavit_En = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ciphers = ["Шифр Цезаря", "Атбаш ", "A1Z26 " , "А1Я33", "base64", "2-ичный код"]

header = Label(text="Шифры", font=("Arial", 23))

menu = Frame(main)

text = ""

def onClickChiper(event):
    cipher = int(str(event.widget)[-1])
    chepTk = Tk(className = "Шифровка - "+ciphers[cipher])
    chepTk.geometry('1000x600')
    chepTk.focus_set()
    global text


    labelToEntry = Label(chepTk,text="текст для шифровки:")
    labelToEntry.place(relx=0.5, y=162, anchor="c")

    entry = ttk.Entry(chepTk, cursor="hand2")
    entry.place(relx=0.5 , y=200 , anchor="c", width=200, height=35)
    entry.focus_set()
    Encryption = ttk.Label(chepTk, font=("Arial", 18))
    
    
    if cipher == 3 or cipher == 2:
        textA1Z26 = Label(chepTk, text="При шифровке A1Z26 и А1Я33 не поддерживают цифры и специальные символы",fg="#000",font=("Arial", 15))
        textA1Z26.place(relx=0.5,y=100,anchor="center")

    if cipher == 0:
        def validate_digit_input(new_value): 
            if new_value == "": 
                return True 
            elif new_value.isdigit(): 
                return True 
            else: 
                return False 
        validate_digit_command = chepTk.register(validate_digit_input) 
        entryROT = ttk.Entry(chepTk, cursor="hand2", validate="key", validatecommand=(validate_digit_command, '%P'))
        entryROT.place(relx=0.5 , y=100 , anchor="c", width=200, height=35)
        labelToEntryROT = Label(chepTk,text="сдвиг:")
        labelToEntryROT.place(relx=0.5, y=62, anchor="c")



    def encryption():
        isSimvol=0
        global text
        if cipher == 0:
            sdvig = int(entryROT.get())
            for i in range(len(str(entry.get()))):
                isSimvol = 0
                for g in range(len(alphavit_ru)):
                    if alphavit_ru[g] == str(entry.get())[i]:
                        if (g + sdvig) < 33:
                            text+= alphavit_ru[g + sdvig]
                            isSimvol=1
                        else:
                            text+= alphavit_ru[g + sdvig - 33]
                            isSimvol=1
                        break
                for g in range(len(alphavit_en)):
                     if alphavit_en[g] == str(entry.get())[i]:
                        if (g + sdvig) < 22:
                            text+= alphavit_en[g + sdvig ]
                            isSimvol=1
                        else:
                            text+= alphavit_en[g + sdvig - 26]
                            isSimvol=1
                        break
                for g in range(len(alphavit_Ru)):
                    if alphavit_Ru[g] == str(entry.get())[i]:
                        if (g + sdvig) < 33:
                            text+= alphavit_Ru[g + sdvig]
                            isSimvol=1
                        else:
                            text+= alphavit_Ru[g + sdvig - 33]
                            isSimvol=1
                        break
                for g in range(len(alphavit_En)):
                     if alphavit_En[g] == str(entry.get())[i]:
                        if (g + sdvig) < 22:
                            text+= alphavit_En[g + sdvig ]
                            isSimvol=1
                        else:
                            text+= alphavit_En[g + sdvig - 26]
                            isSimvol=1
                        break

                if isSimvol==0:
                    text+=str(entry.get())[i]


        if cipher == 1:
            for i in range(len(str(entry.get()))):
                isSimvol = 0
                for g in range(len(alphavit_ru)):
                    if alphavit_ru[g] == str(entry.get())[i]:
                        text+= alphavit_ru[(g + 1) * -1]
                        isSimvol = 1
                for g in range(len(alphavit_en)):
                    if alphavit_en[g] == str(entry.get())[i]:
                        text+= alphavit_en[(g + 1) * -1]
                        isSimvol = 1
                    break
                for g in range(len(alphavit_Ru)):
                    if alphavit_Ru[g] == str(entry.get())[i]:
                        text+= alphavit_Ru[(g + 1) * -1]
                        isSimvol = 1
                for g in range(len(alphavit_En)):
                    if alphavit_En[g] == str(entry.get())[i]:
                        text+= alphavit_En[(g + 1) * -1]
                        isSimvol = 1
                    break
                
                if isSimvol==0:
                    text+=str(entry.get())[i]

        if cipher == 2:
            for i in range(len(entry.get())):
                for g in range(len(alphavit_en)):
                    if alphavit_en[g] == entry.get()[i]:
                        text+=str(g+1)
                        text+="-"
                for g in range(len(alphavit_En)):
                    if alphavit_En[g] == entry.get()[i]:
                        text+=str(g+1)
                        text+="-"
                if entry.get()[i] == " "  or i == (len(entry.get()) - 1):
                    text=text[: -1]
                    text+=" "

        if cipher == 3:
            for i in range(len(entry.get())):
                for g in range(len(alphavit_ru)):
                    if alphavit_ru[g] == entry.get()[i]:
                        text+=str(g+1)
                        text+="-"
                for g in range(len(alphavit_Ru)):
                    if alphavit_Ru[g] == entry.get()[i]:
                        text+=str(g+1)
                        text+="-"
                if entry.get()[i] == " "  or i == (len(entry.get()) - 1):
                    text=text[: -1]
                    text+=" "

        if cipher == 4:
            base64Utf=str(entry.get()).encode("utf-8")
            text = base64.b64encode(base64Utf)
            text = str(text)[2:]
            text = str(text)[:-1]

        if cipher == 5:
            text = binary_code.text_to_bits(entry.get())
            
            
            

                

        Encryption["text"] = text
        Encryption.place( relx=0.5 , y=400 , anchor="c")
        text = ""





















    def UnEncryption():
        global text
        isSimvol=0
        if cipher == 0:
            sdvig = int(entryROT.get())
            for i in range(len(str(entry.get()))):
                isSimvol=0
                for g in range(len(alphavit_ru)):
                    if alphavit_ru[g] == str(entry.get())[i]:
                        text+= alphavit_ru[g - (sdvig)]
                        isSimvol=1
                for g in range(len(alphavit_en)):
                    if alphavit_en[g] == str(entry.get())[i]:
                        text+= alphavit_en[g - (sdvig)]
                        isSimvol=1
                for g in range(len(alphavit_Ru)):
                    if alphavit_Ru[g] == str(entry.get())[i]:
                        text+= alphavit_Ru[g - (sdvig)]
                        isSimvol=1
                for g in range(len(alphavit_En)):
                    if alphavit_En[g] == str(entry.get())[i]:
                        text+= alphavit_En[g - (sdvig)]
                        isSimvol=1
                     
                if isSimvol == 0:
                    text+=str(entry.get())[i] 
            Encryption["text"] = text
            Encryption.place( relx=0.5 , y=400 , anchor="c")
            text = ""

        if cipher == 1:
            for i in range(len(str(entry.get()))):
                isSimvol=0
                for g in range(len(alphavit_ru)):
                    if alphavit_ru[g] == str(entry.get())[i]:
                        text+= alphavit_ru[(g + 1) * -1]
                        isSimvol=1
                for g in range(len(alphavit_en)):
                    if alphavit_en[g] == str(entry.get())[i]:
                        text+= alphavit_en[(g + 1) * -1]
                        isSimvol=1
                for g in range(len(alphavit_Ru)):
                    if alphavit_Ru[g] == str(entry.get())[i]:
                        text+= alphavit_Ru[(g + 1) * -1]
                        isSimvol=1
                for g in range(len(alphavit_En)):
                    if alphavit_En[g] == str(entry.get())[i]:
                        text+= alphavit_En[(g + 1) * -1]
                        isSimvol=1


                if isSimvol==0:
                    text+=str(entry.get())[i]
            Encryption["text"] = text
            Encryption.place( relx=0.5 , y=400 , anchor="c")
            text = ""


        if cipher == 2:
            split = entry.get().split(" ")
            for i in range(len(split)):
                if split[i] =="":
                    split.pop(i)

            split2 = [split[0].split("-")]
            for i in range(1,len(split)):
                split2.append(split[i].split("-"))

            for i in range(len(split2)):
                for g in split2[i]:
                    text+=alphavit_en[int(g) - 1]
                text+=" "
            Encryption["text"] = text
            Encryption.place( relx=0.5 , y=400 , anchor="c")
            text = ""



        if cipher == 3:
            split = entry.get().split(" ")
            for i in range(len(split)):
                if split[i] =="":
                    split.pop(i)


            split2 = [split[0].split("-")]
            for i in range(1,len(split)):
                split2.append(split[i].split("-"))
            for i in range(len(split2)):
                for g in split2[i]:
                    text+=alphavit_ru[int(g) - 1]
                text+=" "
                Encryption["text"] = text
                Encryption.place( relx=0.5 , y=400 , anchor="c")
            text = ""

        if cipher == 4:
            base64Utf = str(entry.get()).encode("utf-8")
            base64Utf = base64.b64decode(base64Utf)
            text = base64Utf.decode("utf-8")
            Encryption["text"] = text
            Encryption.place( relx=0.5 , y=400 , anchor="c")
            text = ""


        if cipher == 5:
            text = binary_code.text_from_bits(entry.get())


            Encryption["text"] = text
            Encryption.place( relx=0.5 , y=400 , anchor="c")
            text = ""
        

    


    def Copy():
        if Encryption["text"] != "":
            pyperclip.copy(str(Encryption["text"]))





    Encryption.place( relx=0.5 , y=400 , anchor="c")
    btnUnEncryption = Button(chepTk, command=UnEncryption, text="Расшифровать", cursor="hand2")
    btnUnEncryption.place(relx=0.5 , y=250 , anchor="c", width=200, height=30)
    btnEncryption = Button(chepTk, command=encryption, text="Шифровать", cursor="hand2")
    btnEncryption.place(relx=0.5 , y=300 , anchor="c", width=200, height=30)
    btnCopy =  Button(chepTk, command=Copy, text="Copy", cursor="hand2")
    btnCopy.place(relx=0.5 , y= 350, anchor="c", width=200, height=30)




for r in range(0,len(ciphers)): menu.rowconfigure(index=r, weight=1)
for c in range(1): menu.columnconfigure(index=c, weight=1)
for r in range(0,len(ciphers)):
    btn = Button(menu , text=f"{ciphers[r]}" , font=("Arial", 11), name = str(r),cursor="hand2", )
    btn.grid(row=r, sticky=EW, padx=20, pady=5 , ipady=5)
    btn.bind('<Button-1>', onClickChiper)

menu.place(relx=0.5, y=250, width=200, anchor="c")
header.place(relx=0.5, y=50, width=400 , height= 40, anchor="c")

main.mainloop()