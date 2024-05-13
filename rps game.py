import random

done = False
wins = 0
losses = 0
ties = 0


names = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}

while not done:
    choice = input('Choose your next move (R, P, S) (Q to Quit):')
    cpu_choice = random.choice(['R', 'P', 'S'])
    if choice == cpu_choice:
        print("It's a tie! You both chose {names[choice]}")
        ties+=1
    elif choice == 'R':
        if cpu_choice == 'p':
            print(f"CPU wins! You chose {names[choice]}, CPU chose {names[cpu_choice]}")
            losses+=1
        else:
            print(f"You win! You chose {names[choice]}, CPU chose {names[cpu_choice]}")
            wins+=1
    elif choice == 'P':
        if cpu_choice == 'S':
            print(f"CPU wins! You chose {names[choice]}, CPU chose {names[cpu_choice]}")
            losses+=1
        else:
            print(f"You win! You chose {names[choice]}, CPU chose {names[cpu_choice]}")
            wins+=1
    elif choice == 'S':
        if cpu_choice == 'R':
            print(f"CPU wins! You chose {names[choice]}, CPU chose {names[cpu_choice]}")
            losses+=1
        else:
            print(f"You win! You chose {names[choice]}, CPU chose {names[cpu_choice]}")
            wins+=1
    elif choice== 'Q':
        done = True
    else:
        print('Invalid Command')

    print(f'Current Status {wins} Wins, {losses} Losses, {ties} ties')
        
        
        
