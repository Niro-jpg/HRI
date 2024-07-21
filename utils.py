def move_name(attack):
    name = "miao"
    damage = 0
    if   attack == 1:
        #raggio cometa
        name = "raggio cometa"
    elif attack == 2:
        # fuoco fatuo
        name = "fuoco fatuo"
    elif attack == 3:
        # drago distorsione
        name = "drago distorsione"
    elif attack == 4:
        # roccia fonda
        name = "roccia fonda"
    elif attack == 5:
        #coleo trapano
        name = "coleo trapano"
    elif attack == 6:
        # gatgraffio
        name = "gatgraffio"
    elif attack == 7:
        name = "raggio cometa"
    elif attack == 8:
        name = "raggio cometa"
    elif attack == 9:
        name = "raggio cometa"
    elif attack == 10:
        name = "raggio cometa"
    else:
        print("Caso non valido.")
    return name