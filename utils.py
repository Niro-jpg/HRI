def move_name(index):

    name = 'punching combo'
    if index == 1:
        name = 'punching combo'
    elif index == 2:
        name = 'dragon fist'
    elif index == 3:
        name = 'kamehameha'
    elif index == 4:
        name = 'spiritball'
    elif index == 5:
        name = 'shuriken'
    elif index == 6:
        name = '100 hits'
    elif index == 7:
        name = 'multiplication technique combo'
    elif index == 8:
        name = 'rasengan'
    elif index == 9:
        name = 'iron fist'
    elif index == 10:
        name = 'high caliber gun'
    elif index == 11:
        name = 'shotgun'
    elif index == 12:
        name = 'come with me if you want to live'
    elif index == 13:
        name = 'space sword'
    elif index == 14:
        name = 'space strike'
    elif index == 15:
        name = 'space alabard'
    elif index == 16:
        name = 'space thunder'
    elif index == 17:
        name = 'sd'
    elif index == 31:
        name = 'damage'
    else:
        name = "rasengan"
    
    return name

def animation_name(index):

    name = 'default_an'
    if index == 1:
        name = 'default_an'
        #name = 'punching combo'
    elif index == 2:
        name = 'default_an'
        #name = 'dragon fist'
    elif index == 3:
        name = 'default_an'
        #name = 'kamehameha'
    elif index == 4:
        name = 'spiritball'
    elif index == 5:
        name = 'default_an'
        #name = 'shuriken'
    elif index == 6:
        name = 'default_an'
        #name = '100 hits'
    elif index == 7:
        name = 'default_an'
        #name = 'multiplication technique combo'
    elif index == 8:
        name = 'default_an'
        #name = 'rasengan'
    elif index == 9:
        name = 'default_an'
        #name = 'iron fist'
    elif index == 10:
        name = 'default_an'
        #name = 'high caliber gun'
    elif index == 11:
        name = 'default_an'
        #name = 'shotgun'
    elif index == 12:
        name = 'come with me if you want to live'
    elif index == 13:
        name = 'default_an'
        #name = 'sd'
    elif index == 14:
        name = 'default_an'
        #name = '100 hits'
    elif index == 15:
        name = 'default_an'
        #name = 'multiplication technique combo'
    elif index == 16:
        name = 'space_thunder'
    elif index == 17:
        name = 'default_an'
        #name = 'sd'
    elif index == 31:
        name = 'default_an'
        #name = 'damage'
    else:
        name = 'default_an'
    
    return name

def is_convertible_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_super_move(index):
    super_moves_list = [4,8,12,16]
    if (index in super_moves_list):
        return True
    else:
        return False