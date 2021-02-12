# Definição de personagens
define l = Character("Lokost")

# imagens
image logo:
    "logo.png"
    zoom .2 xalign .5 yalign .5


# Aqui começa o jogo
label splashscreen:
    show logo
    pause 2
    return

label start:
    scene Quarto dia_pcon
    show Lokost Normal1
    l "Olá mundo"
