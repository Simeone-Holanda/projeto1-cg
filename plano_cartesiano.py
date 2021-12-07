from tkinter import *

master = Tk()

#captura tamanho da tela do usuário
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

master.title('Plano cartesiano')

master.geometry("%dx%d+0+0" %(screen_width,screen_height))  # largura, altura, dist esquerda + dist topo
master.wm_resizable(width=False, height=False)  # travando a tela na resolução definida


# colocando a img de fundo e especificando a posição dela na tela
canvas = Canvas(master, width=1920, height=1080, bg="white")
canvas.pack()
label_plano_cartesiano = Label(master)
label_plano_cartesiano.place(x=0, y=0)

#criando plano cartesiano
canvas.create_line(0,screen_height/2,screen_width,screen_height/2) #Linha horizontal
canvas.create_line(screen_width/2,0,screen_width/2,screen_height) #linha  vertical

# criando a caixinha q mostra as coordenadas
widget1 = Frame(canvas)
widget1.place(bordermode=OUTSIDE, height=50, width=400, x=250)
msg = Label(widget1, text=f"Coordenadas da tela X:{0} | Y: {0}")
msg["font"] = ("Verdana", "10", "italic", "bold")
msg.pack()

coordenadas_plano_cartesiano = Frame(canvas)
coordenadas_plano_cartesiano.place(bordermode=OUTSIDE, height=50, width=400, x=800)
msg_plano = Label(coordenadas_plano_cartesiano, text=f"Coordenadas do plano X:{0} | Y: {0}")
msg_plano["font"] = ("Verdana", "10", "italic", "bold")
msg_plano.pack()

def converter_plano_cartesiano(x,y):
    ...

def button(event):
    """ Função responsável por mostrar as coordenadas na tela e marca o pixel selecionado. """

    canvas.delete("pixelGroup")#Exclui caso exista o grupo de pixeis
    x = event.x
    y = event.y
    if x <= screen_width/2:
        print('x é negativo ou igual a 0!!')
        if y <= screen_height/2:
            print('y é positivo!!')
            msg.configure(text=f'X:{x} | Y: {y}')
            msg_plano.configure(text=f'X:{round(((screen_width/2)-x))*-1} | Y: {round(((screen_height/2)-y))}')
        else:
            print('y é negativo ou igual a 0 !!')
            msg.configure(text=f'X:{x} | Y: {y}')
            msg_plano.configure(text=f'X:{round(((screen_width/2)-x))*-1} | Y: {round((((screen_height/2)-y)))}')
    else:
        print('x é positivo!!')
        if y < screen_height/2:
            print('y é positivo!!')
            msg.configure(text=f'X:{x} | Y: {y}')
            msg_plano.configure(text=f'X:{round(((screen_width/2)-x))*-1} | Y: {round(((screen_height/2)-y))}')
        else:
            print('y é negativo!!')
            msg.configure(text=f'X:{x} | Y: {y}')
            msg_plano.configure(text=f'X:{round(((screen_width/2)-x))*-1} | Y: {round(((screen_height/2)-y))}')
    
    print(f'X:{x} | Y: {y}')
    canvas.create_rectangle(x, y, x+10, y+10, fill="red",tags="pixelGroup") #gera grupo de pixeis



master.bind('<Button>', button)
master.mainloop()
