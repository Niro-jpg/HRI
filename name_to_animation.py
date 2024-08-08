from move import default_an, rasengan, spiritball, damage, come_with_me_if_you_want_to_live, space_thunder

def name_to_animation(name, battle):
   name = name.replace(' ', '_')
   anims = [default_an, rasengan, spiritball, space_thunder, come_with_me_if_you_want_to_live, damage]
   for a in anims:
      if a == eval(name):
         ani = a
   ani(battle)
#name_to_animation('space thunder')