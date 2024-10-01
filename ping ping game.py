import random

def get_player_names():
    # This function collects player names until 'done' is entered
    players = []
    while True:
        name = input("Enter player name (or type 'done' when all names are entered): ")
        if name.lower() == 'done':
            break
        players.append(name)  # Append the name as entered to the list
    return players

def play_match(player1, player2):
    # This function asks for the winner between two players
    print(f"Match: {player1} vs {player2}")
    while True:
        winner_input = input(f"Enter the winner ({player1} or {player2}): ")
        # Compare lowercased input to handle case insensitivity
        if winner_input.strip().lower() == player1.lower():
            return player1
        elif winner_input.strip().lower() == player2.lower():
            return player2
        else:
            print("Invalid winner, please enter one of the two player names exactly as shown.")

def tournament(players):
    # This function controls the tournament logic
    round_number = 1
    while len(players) > 1:
        random.shuffle(players)
        winners = []
        print(f"\nRound {round_number}:")
        # Match players in pairs
        for i in range(0, len(players) - 1, 2):
            winner = play_match(players[i], players[i+1])
            winners.append(winner)
        # Handle odd number of players
        if len(players) % 2 == 1:
            winners.append(players[-1])
            print(f"{players[-1]} advances automatically.")
        players = winners
        round_number += 1
    return players[0]

def main():
    # Main function to start the tournament
    players = get_player_names()
    if len(players) < 2:
        print("Not enough players for a tournament!")
        return
    
    winner = tournament(players)
    print(f"\nThe ultimate winner of the tournament is: {winner}")

if __name__ == '__main__':
    main()