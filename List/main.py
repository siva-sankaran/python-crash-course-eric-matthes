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

# 3-8. Seeing the World:
def seeing_the_world():
    locations = ['Srilanka', 'China', 'London', 'New York', 'Japan']
    print(locations)
    print('Sorted list without modifying the original List')
    print(sorted(locations))
    print('Let us see the original list')
    print(locations)
    print('sort the list in reverse alphabetical order without modifying')
    print(sorted(locations, reverse=True))
    print('Again let us see the original list ')
    print(locations)

    locations.reverse()
    print(locations)
    locations.reverse()

    print('Original list reversed back again so now it is in original order')
    print(locations)

    locations.sort()
    print('original list is sorted i.e. modified')
    print(locations)

    locations.sort(reverse=True)
    print(locations)

# 3-9. Dinner Guests
    #Done in 3-7 exercise

# 3-10. Every Function
def use_every_function():
    rivers = ['Thamirabharani', 'vaigai', 'Kaveri', 'Paalaaru', 'Krishna', 'Godavari', 'Ganga']
    print(len(rivers))
    print(rivers[1].title())
    print(rivers[-1])
    rivers[1] = 'Vaigai'
    print(rivers)

    rivers.append('Narmada')

    mountains = []
    mountains.append('Pothigai')
    mountains.append('Ponmudi')
    mountains.append('Nilagiri')
    mountains.append('Himalaya')

    print(mountains)

    mountains.insert(2, 'Javvadhu')
    print(mountains)

    del mountains[1]

    print(mountains)

    any_position_popped = mountains.pop(2)
    print(any_position_popped)

    mountains.remove('Javvadhu')

    print(mountains)

    books_to_read = ['venmurasu', 'kadal', 'saayaavanam', 'wolf totem']
    books_to_read.sort()
    print(books_to_read)

    books_to_read.sort(reverse=True)
    print(books_to_read)

    want_to_learn = ['writing', 'speaking', 'software architecture', 'cooking', 'psychology']
    print(sorted(want_to_learn))

    want_to_learn.reverse()

    print(want_to_learn)

# 3-11. Intentional Error
#     print(want_to_learn[-6])
    print(want_to_learn[-5])
    print(len(want_to_learn))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    use_every_function()

