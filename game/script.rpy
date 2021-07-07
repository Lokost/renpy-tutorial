# Definição de personagens

define l = Character('Lokost')

# Definição de imagens extras
image Logo:
    "logo.png"
    zoom .2 yalign .5 xalign .5

# Configurações da tela de apresentação
label splashscreen:
    show Logo with dissolve
    pause 1
    hide Logo with dissolve
    return
    

label main_menu:
    call screen main_menu with dissolve

# Aqui começa o joogo
label start:
    scene sala dia
    with fade
    show Lokost normal with dissolve
    l "Olá"
    l "Meu nome é Lokost"
    l "Prazer em te conhecer!"