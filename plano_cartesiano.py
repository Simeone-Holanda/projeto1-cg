from tkinter import *

master = Tk()

master.title('Plano cartesiano')

master.geometry("318x320+0+0")# largura, altura, dist esquerda + dist topo
master.wm_resizable(width=False, height=False) # travando a tela na resolução definida

#importando img
img = PhotoImage(file="plano_cartesiano.jpg")

#colocando a img de fundo e especificando a posição dela na tela
label_plano_cartesiano = Label(master, image=img)
label_plano_cartesiano.place(x=0,y=0)

# criando a caixinha q mostra as coordenadas
widget1 = Frame(master) 
widget1.pack()
msg = Label(widget1, text=f"Coordenadas da tela X:{0} | Y: {0}")
msg["font"] = ("Verdana", "10", "italic", "bold")
msg.pack()


def button(event):
    """ Função responsável por mostrar as coordenadas na tela e no console. """
    x = event.x
    y = event.y
    msg.configure(text=f'X:{x} | Y: {y}')
    print(f'X:{x} | Y: {y}')

master.bind('<Button>', button)
master.mainloop()