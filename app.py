#a list whit paper, rock and scissors
import random
import os
jugada = ["piedra", "papel", "tijera"]
#the user choose a option between the list
def user():
    user = input("Elige una opcion: piedra, papel o tijera: ")
    if user == "piedra":
        print("Has elegido piedra")
    elif user == "papel":
        print("Has elegido papel")
    elif user == "tijera":
        print("Has elegido tijera")
    else:
        print("No has elegido una opcion correcta")
    return user
#the computer choose a option between the list
def computer():
    computer = random.choice(jugada)
    if computer == "piedra":
        print("La computadora ha elegido piedra")
    elif computer == "papel":
        print("La computadora ha elegido papel")
    elif computer == "tijera":
        print("La computadora ha elegido tijera")
    return computer
#Both options are compared to see who wins and who loses, paper beats rock, rock beats scissors and scissors beats paper
def compare(user, computer):
    if user == computer:
        return "Empate"
    elif user == "piedra":
        if computer == "tijera":
            return "Ganaste"
        else:
            return "Perdiste"
    elif user == "papel":
        if computer == "piedra":
            return "Ganaste"
        else:
            return "Perdiste"
    elif user == "tijera":
        if computer == "papel":
            return "Ganaste"
        else:
            return "Perdiste"
#The game is played until the user or the computer wins 3 times
def game():
    user_score = 0
    computer_score = 0
    while user_score < 3 and computer_score < 3:
        user_input = user()
        computer_input = computer()
        result = compare(user_input, computer_input)
        print(result)
        if result == "Ganaste":
            user_score += 1
        elif result == "Perdiste":
            computer_score += 1
        print("Tu: {} Computadora: {}".format(user_score, computer_score))
    if user_score == 3:
        print("Has ganado")
    elif computer_score == 3:
        print("Has perdido")
#choose if you want to play again
def main():
    game()
    while True:
        play_again = input("¿Quieres jugar otra vez? (y/n): ")
        if play_again == "y":
            game()
        else:
            break
#if the player dont want to play again the game ends and 
if __name__ == '__main__':
    main()
