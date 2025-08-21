from turtle import Turtle, Screen
import random

iniciou_corrida = False
tela = Screen()
tela.setup(width=500, height=400)
aposta = tela.textinput(title="Faça sua aposta", prompt="Que tartaruga vai ganhar? Digite a cor em inglês: ")
cores = ["red", "orange", "yellow", "green", "blue", "purple"]
posicoes_verticais = [-70, -40, -10, 20, 50, 80]
todas_tartarugas = []

# Create 6 turtles
for num_tartaruga in range(0, 6):
    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.penup()
    nova_tartaruga.color(cores[num_tartaruga])
    nova_tartaruga.goto(x=-230, y=posicoes_verticais[num_tartaruga])
    todas_tartarugas.append(nova_tartaruga)

if aposta:
    iniciou_corrida = True

while iniciou_corrida:
    for tartaruga in todas_tartarugas:
        # 230 is 250 - half the width of the turtle.
        if tartaruga.xcor() > 230:
            iniciou_corrida = False
            cor_ganhadora = tartaruga.pencolor()
            if cor_ganhadora == aposta:
                print(f"Ganhou! Tartaruga cor {cor_ganhadora} :)")
            else:
                print(f"Perdeu! A tartaruga {cor_ganhadora} é a vencedora!")

        # Make each turtle move a random amount.
        distancia_aleatoria = random.randint(0, 10)
        tartaruga.forward(distancia_aleatoria)

tela.exitonclick()
