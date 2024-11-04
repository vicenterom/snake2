import turtle
import time
import random

posponer = 0.1

score = 0
hig_score = 0

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width = 600, heigth = 600)
wn.tracer(0)

#Cabeza de serpiente
cabeza = turtle.Turlte()
cabeza.speed(0)
