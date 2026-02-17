from importlib.resources.readers import remove_duplicates


def print_each_item_of_list():
    friends_names = ['Kumar', 'Ram', 'Suraj', 'Aundy' ]
    print(friends_names[0])
    print(friends_names[1])
    print(friends_names[2])
    print(friends_names[3])

def print_each_item_of_list_with_greeting():
    friends_names = ['Kumar', 'Ram', 'Suraj', 'Aundy']
    print(f"Hello, {friends_names[0]}!")
    print(f"Hello, {friends_names[1]}!")
    print(f"Hello, {friends_names[2]}!")
    print(f"Hello, {friends_names[3]}!")

def print_transport():
    mode_of_transport = ['motorcycle', 'bicycle', 'boat', 'ship', 'train']
    print(f"I want to own a {mode_of_transport[0]}")
    print(f"I want to own a {mode_of_transport[1]}")
    print(f"I want to own a {mode_of_transport[2]}")
    print(f"I want to own a {mode_of_transport[3]}")
    print(f"I want to own a {mode_of_transport[4]}")

#3-3 Guest List
def invite_to_dinner():
    guests = [ 'Jeyamohan', 'Sankaran Pillai', 'Sivagurunatha Pillai']
    for guest in guests:
        print(f'Dear {guest.title()}, I like to talk, eat and have nice time with you. Please dine with me.')
## 3-5 Changing Guest List

    print(f'{guests[0]} is not available.')
    guests[0] = "Gauri"

    for guest in guests:
        print(f'Dear {guest.title()}, I like to talk, eat and have nice time with you. Please dine with me.')

# 3-6 More Guests
    print("Hi all, Found a new larger dinner Table. So I will cancel this and send you another invite")
    guests.insert(0, "Jeyamohan")
    guests.insert(int(len(guests)/2), "Gandhi")
    guests.append("Amma")

    for guest in guests:
        print(f'Dear {guest.title()}, I like to talk, eat and have nice time with you. Please dine with me.')

# 3-7. Shrinking Guest List
    print(f'remaining persons are : {guests}')
    print(f'Sorry {len(guests)} folks, I can only invite 2 persons')
    removed_guest = guests.pop()
    print(f'I am sorry {removed_guest}, I can\'t invite you for the dinner')
    removed_guest = guests.pop()
    print(f'I am sorry {removed_guest}, I can\'t invite you for the dinner')
    removed_guest = guests.pop()
    print(f'I am sorry {removed_guest}, I can\'t invite you for the dinner')
    removed_guest = guests.pop()
    print(f'I am sorry {removed_guest}, I can\'t invite you for the dinner')

    print(f'Hi {guests[0]}, you are still invited.')
    print(f'Hi {guests[1]}, you are still invited.')

    del guests[1]
    del guests[0]

    print(f'remaining persons are : {guests}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    invite_to_dinner()

