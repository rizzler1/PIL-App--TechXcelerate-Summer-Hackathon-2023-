import tkinter as tk
from tkinter import ttk
from pathlib import Path
from PIL import Image,ImageTk
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from datetime import date

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0") 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = tk.Tk()
root.configure(bg="#c3ff84")
root.title("PIL App")
container = ttk.Frame(root)
canvas = tk.Canvas(container, height="700", width="1150", bg="#d6eccc")
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

scrollwindow = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        
canvas.configure(yscrollcommand=scrollbar.set)

canvas.create_text(
    32.0,
    0.0,
    anchor="nw",
    text="What is your full name?",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

canvas.create_text(
    32.0,
    177.0,
    anchor="nw",
    text="Type in your full address here",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

canvas.create_text(
    33.0,
    531.0,
    anchor="nw",
    text="What is the crime that was committed?",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

canvas.create_text(
    32.0,
    708.0,
    anchor="nw",
    text="To which High Court are you filing this PIL?",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

'''canvas.create_text(
    32.0,
    1081.0,
    anchor="nw",
    text="How did you find about this crime?",
    fill="#000000",
    font=("Consolas", 36 * -1)
)'''

canvas.create_text(
    33.0,
    1081.0,
    anchor="nw",
    text="What is the damage caused by the crime?",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

canvas.create_text(
    33.0,
    1415.0,
    anchor="nw",
    text="Have any representations been made on \nthis topic before? If not type none ",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

canvas.create_text(
    33.0,
    1610.0,
    anchor="nw",
    text="What's your job? ",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

canvas.create_text(
    32.0,
    1258.0,
    anchor="nw",
    text="How did you find out about this crime? \nWhat is the source of information?",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

canvas.create_text(
    32.0,
    875.0,
    anchor="nw",
    text="Write brief facts about the matter \non which this PIL is being filed",
    fill="#000000",
    font=("Consolas", 36 * -1)
)

canvas.create_text(
    33.0,
    354.0,
    anchor="nw",
    text="Who/What business are you filing this PIL against?",
    fill="#000000",
    font=("Consolas", 36 * -1)
)    


entry_image_1 = tk.PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    455.0,
    113.0,
    image=entry_image_1)

name = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 113, window= name)



entry_image_2 = tk.PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    456.0,
    290.0,
    image=entry_image_2
    
)
address = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 290, window= address)



entry_image_3 = tk.PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    456.0,
    467.0,
    image=entry_image_3
)   
enemy = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 467, window= enemy)



entry_image_4 = tk.PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    455.0,
    644.0,
    image=entry_image_4
)

crime = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 644, window= crime)



entry_image_5 = tk.PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    456.0,
    821.0,
    image=entry_image_5
)

place = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 821, window= place)



entry_image_6 = tk.PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    455.0,
    998.0,
    image=entry_image_6
)

explanation = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 998, window= explanation)



'''entry_image_7 = tk.PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    455.0,
    1194.0,
    image=entry_image_7
)

entry7 = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 1194, window= entry7)'''

entry_image_8 = tk.PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    456.0,
    1194.0,
    image=entry_image_8
)

damage = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 1194, window= damage)



entry_image_9 = tk.PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    455.0,
    1371.0,
    image=entry_image_9
)

info = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 1371, window= info)


entry_image_10 = tk.PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    455.0,
    1548.0,
    image=entry_image_10
)

representation = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 1548, window= representation)


entry_image_11 = tk.PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_10 = canvas.create_image(
    455.0,
    1725.0,
    image=entry_image_10
)

job = tk.Entry(canvas, bd= 2, relief="flat", width="45", font=('Consolas 24') )
canvas.create_window(455, 1725, window= job)




'''submit = tk.Button(canvas, text="Submit", font=('Consolas 24'), command= submitform(), relief="flat", bg="white")
canvas.create_window(525, 1850, window= submit)'''

submit_imagesource = Image.open(relative_to_assets("submitbutton2.png"))

resize = submit_imagesource.resize((276,100), Image.LANCZOS)

submit_image = ImageTk.PhotoImage(resize)

def submitform():

    template = DocxTemplate("template.docx")

    illegal = crime.get()

    context = {"name" : name.get(),
            "enemy" : enemy.get(),
            "address" : address.get(),
            "illegal" : illegal,
            "place" : place.get(),
            "purpose" : explanation.get(),
            "occupation" : job.get(),
            "sourceofinformation" : info.get(),
            "damage" : damage.get(),
            "representations" : representation.get()}

    template.render(context)
    template.save('output.docx')
    top = tk.Toplevel(root)
    top.geometry("200x50")
    top.title("Success!")
    tk.Label(top, text="File Created!", font=("Consolas 12")).pack(side="top")
    top.resizable(False, False)
    
    

'''submit_images = canvas.create_image(
    525.0,
    1850.0,
    image=submit_image)'''
    


submit = tk.Button(canvas, text="Submit", font=('Consolas 24'),image= submit_image, command= submitform, 
                   relief="flat", bg="white", borderwidth=0, activebackground="#d6eccc", background="#d6eccc" )
canvas.create_window(580, 1840, window= submit)

imageup = ImageTk.PhotoImage(Image.open(relative_to_assets("uptop.png")))

label1 = tk.Label(root, text="PIL App", font=("Consolas", 26), bg="#c3ff84")
label1.pack(side="top")

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
canvas.bind_all("<MouseWheel>", _on_mousewheel)

canvas.configure(scrollregion= canvas.bbox("all"))

container.pack()
canvas.pack(side="left", fill="both", expand=True,)
scrollbar.pack(side="right", fill="y")

root.resizable(False, False)

root.mainloop()