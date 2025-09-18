import random 

def monty_hall_game(switch_doors):
  doors = ['car'] + ['goat'] * 2
  random.shuffle(doors) # shuffle inplace
  
  initial_choice = random.choice(range(len(doors)))
  
  if switch_doors:
    doors_revelaed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
    door_revelaed = random.choice(doors_revelaed)
    final_choice = [i for i in range(3) if i != initial_choice and i != door_revelaed][0]
  else:
    final_choice = initial_choice
  
  return doors[final_choice] == 'car'

def simpulate_game(num_games):
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(num_games)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])
    
    return num_wins_without_switching / num_games * 100, num_wins_with_switching / num_games * 100


if __name__ == '__main__':
  num_games = 10000
  win_percent_without_switching, win_percentage_with_switching = simpulate_game(num_games)
  print(f'winning prcentage without switching doors: {win_percent_without_switching}%')
  print(f'winning prcentage with switching doors: {win_percentage_with_switching}%')