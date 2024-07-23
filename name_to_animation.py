from move import default_an, rasengan, spiritball, damage

def name_to_animation(name):

   anims = [default_an, rasengan, spiritball, 'move3', 'move4', damage]
   for a in anims:
      if a == eval(name):
         ani = a
   ani()
name_to_animation('damage')