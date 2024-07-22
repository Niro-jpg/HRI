from move import default_an, move_arm, arms_up

def index_to_animation(idx):

   ani = [default_an, move_arm, arms_up, 'move3', 'move4']
   ani[idx]()

index_to_animation(1)