import random as rd


def game(computer, you):

    if computer == you:
        return None

    elif computer == 'R':
        if you == 'S':
            return False
        elif you == 'P':
            return True

    elif computer == 'P':
        if you == 'R':
            return False
        elif you == 'S':
            return True

    elif computer == 'S':
        if you == 'P':
            return False
        elif you == 'R':
            return True


while True:
    random_No = rd.randint(1, 3)

    if random_No == 1:
        computer = 'R'
    elif random_No == 2:
        computer = 'P'
    elif random_No == 3:
        computer = 'S'

    print("\n\t<<-- Rock Paper Scissor -->>\n")
    print("Choose Rock(R), Paper(P) or Scissor(S)")
    you = input("Your turn: ")
    g = game(computer, you)

    print(f"\nComputer: {computer}")
    print(f"You: {you}")

    if g == None:
        print("\nIt's a tie!")
    elif g:
        print("\nYou Win!")
    else:
        print("\nYou Lose!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("\nThanks for playing!")
