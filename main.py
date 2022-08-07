#  Nyzheir Warner
# fix capitalization errors

def showinstructions():
    print('Welcome to Momos Curse')
    print('Collect 6 items to dispel Momos Curse or die trying.')
    print('Move commands: go North, go South, go East, go West')
    print('To Add to Inventory Type: get "Item Name"')


def playermove(player, directions, rooms):
    # allows us to modify global variable from inside function.
    current_room = player

    if directions in rooms[current_room]:  # room checker.
        current_room = rooms[current_room][directions]
    else:
        print('--------------------------')
        print("You cant go that direction.")
        return player  # returns the same room if nothing is in that direction

    return current_room  # returns the player position.


def playerstatus(current_room, inventory, rooms):
    print('--------------------------')
    print('You are in {}'.format(current_room))
    print('Inventory: {}'.format(inventory))
    if 'item' in rooms[current_room]:
        print('you see a {}'.format(rooms[current_room]['item']))
    print('--------------------------')


def playerinventory(current_room, inventory, move, rooms):
    if 'item' in rooms[current_room] and move[1] in rooms[current_room]['item']:
        inventory += [move[1]]
        print('{} obtained'.format(move[1]))
        del rooms[current_room]['item']
    elif move[1] not in inventory:
        print('Cannot get {}'.format(move[1]))
    else:
        print('You Already have a {}'.format(move[1]))


def main():
    inventory = []
    player = 'Entry Hall'
    showinstructions()

    rooms = {
        'Entry Hall': {'North': 'Shrine Room', 'East': 'East Wing Hallway', 'West': 'West Wing Hallway'},
        'West Wing Hallway': {'East': 'Entry Hall', 'North': 'Auditorium', 'West': 'Class A-1', 'South': 'Music Room'},
        'Class A-1': {'East': 'West Wing Hallway', 'item': 'Cellphone'},
        'Auditorium': {'South': 'West Wing Hallway', 'item': 'Bookbag'},
        'Music Room': {'North': 'West Wing Hallway', 'item': 'Violin'},
        'Shrine Room': {'South': 'Entry Hall', 'item': 'End Alter'},
        'East Wing Hallway': {'South': 'Cafeteria', 'North': 'Gymnasium', 'West': 'Entry Hall', 'East': 'Class B-1'},
        'Gymnasium': {'South': 'East Wing Hallway', 'item': 'Hair-Tie'},
        'Cafeteria': {'North': 'East Wing Hallway', 'item': 'Jacket'},
        'Class B-1': {'West': 'East Wing Hallway', 'item': 'Bracelet'}
    }

    while True:
        current_room = player

        if current_room == 'Shrine Room' and len(inventory) < 6:
            playerstatus(current_room, inventory, rooms)
            print("You see an alter and try to dispel Momo's curse but do not have enough of her items")
            print('Darkness slowly falls over you\n''YOU DIED!!!!')
            break
        if current_room == 'Shrine Room' and len(inventory) == 6:
            playerstatus(current_room, inventory, rooms)
            print("You see an alter and put all of Momo's belongings in it")
            print("You feel as if a weight has been lifted off of your shoulders")
            print("You have finally put Momo's spirit to rest\n""YOU WIN!!!")
            break

        playerstatus(current_room, inventory, rooms)

        players_move = input('Enter your move:\n')

        if 'go' in players_move or 'get' in players_move or 'exit' in players_move:  # input Validator

            move = players_move.split()  # splitting string

            if move[0] == 'go':
                player = playermove(player, move[1], rooms)  # assigns val to players move change rooms based on input.

            elif move[0] == 'get':
                playerinventory(current_room, inventory, move, rooms)  # calls the inventory function
            elif move[0] == 'exit':
                print('Thank You for playing have a nice day')

        else:
            print('Invalid Input')
            continue  # goes back to top of loop


main()
