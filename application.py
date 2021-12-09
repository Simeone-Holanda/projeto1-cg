from tkinter import *

from transformacoes import Transformar

master = Tk()

#Tamanho da tela padrao
screen_width = 1000
screen_height = 900

canvasSizeX = 900
canvasSizeY = 800

master.title('Projeto 1: Transformacoes')

master.geometry("%dx%d+0+0" % (screen_width, screen_height))  # largura, altura, dist esquerda + dist topo
master.wm_resizable(width=False, height=False)  # travando a tela na resolução definida

# colocando a img de fundo e especificando a posição dela na tela
canvas = Canvas(master, width=canvasSizeX, height=canvasSizeY, bg="white")
canvas.pack(side="bottom")

# colocar o pixel como imagem
img = PhotoImage(width=screen_width, height=screen_height)
canvas.create_image((screen_width / 2, screen_height / 2), image=img, state="normal")  # normal, disabled or hidden

# criando plano cartesiano

#Linha Horizontal
for i in range(canvasSizeX):
    img.put("black", (int(0 + i), int(canvasSizeY/2)))

#Linha vertical
for i in range(canvasSizeY):
    img.put("black", (int(canvasSizeX/2), int(0+i)))


# criando a caixinha q mostra as coordenadas
widget1 = Frame(master)
widget1.place(bordermode=OUTSIDE, height=20, width=300, x=50)
msg = Label(widget1, text=f"Coordenadas da tela X:{0} | Y: {0}")
msg["font"] = ("Verdana", "10", "italic", "bold")
msg.pack()

# Container para mostrar todas as coordenadas do plano
coordenadas_plano_cartesiano = Frame(master)
coordenadas_plano_cartesiano.place(bordermode=OUTSIDE, height=20, width=400, x=450)
msg_plano = Label(coordenadas_plano_cartesiano, text=f"Coordenadas do plano X:{0} | Y: {0}")
msg_plano["font"] = ("Verdana", "10", "italic", "bold")
msg_plano.pack()

# Container para mostrar os NDCs
coordenadas_ndc = Frame(master)
coordenadas_ndc.place(bordermode=OUTSIDE, height=20, width=400, y=70, x=20)
msg_ndc = Label(coordenadas_ndc, text=f"Coordenadas NDC NDCX:{0} | NDCY: {0}")
msg_ndc["font"] = ("Verdana", "10", "italic", "bold")
msg_ndc.pack(side="bottom")

# Container
coordenadas_dc = Frame(master)
coordenadas_dc.place(bordermode=OUTSIDE, height=20, width=300, x=500, y=70)
msg_dc = Label(coordenadas_dc, text=f"Coordenadas DC DCX:{0} | DCY: {0}")
msg_dc["font"] = ("Verdana", "10", "italic", "bold")
msg_dc.pack(side="bottom")


def button(event):
    """ Função responsável por mostrar as coordenadas e marca o pixel selecionado.Além de mostrar todos
        as transformoções em containers separados """

    transformar = Transformar()

    x = event.x
    y = event.y

    if (x > canvasSizeX):
        x = canvasSizeX
    elif (y > canvasSizeY):
        y = canvasSizeY
    elif (y < 0):
        y = 0
    elif (x < 0):
        x = 0

    x_plano = round(x - (canvasSizeX / 2) - 1) + 1
    y_plano = (round(((y - canvasSizeY / 2) - 1)) * -1) - 1

    ndcx = round(transformar.world_to_ndcx(x_plano, (canvasSizeX / 2)), 2)
    ndcy = round(transformar.world_to_ndcy(y_plano, (canvasSizeY / 2)), 2)

    dcx = transformar.ndcx_to_dcx(ndcx, canvasSizeX)
    dcy = transformar.ndcy_to_dcy(ndcy, canvasSizeY)

    msg.configure(text=f'Coordenadas da tela X:{x} | Y: {y}')
    msg_plano.configure(
        text=f'Coordenadas do plano X:{x_plano} | Y: {y_plano}')
    print(f'X:{x} | Y: {y}')

    msg_ndc.configure(text=f'Coordenadas NDC NDCX:{ndcx} | NDCY: {ndcy}')

    msg_dc.configure(text=f'Coordenadas DC DCX:{dcx} | DCY: {dcy}')

    data = (  # Definição do grupo de pixeis
        ("red", "red", "red", "red", "red"),
        ("red", "red", "red", "red", "red"),
        ("red", "red", "red", "red", "red"),
        ("red", "red", "red", "red", "red"),
        ("red", "red", "red", "red", "red"),
    )

    if (x - 2 < 0) or (y - 2 < 0):
        img.put(data, (x, y))

    else:
        img.put(data, (x - 2, y - 2))
        # Impressão do pixel


if __name__ == "__main__":
    canvas.bind('<Button>', button)
    master.mainloop()