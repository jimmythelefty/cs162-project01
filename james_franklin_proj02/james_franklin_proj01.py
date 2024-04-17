"""james_franklin_project01.py - Smart home program using OOP aggregation. 

This program uses Object Oriented Programming to implement a basic Smart Home
program. The "House" class uses aggregation of the Room class instances to calculate
the total area of the house, as well as provide the status of all the rooms.
The Bedroom and Bathroom classes inherit and expand the Room class.
There is a user interface program to allow the user to use the various methods
for the classes.

James Franklin
LBCC ID: x00359202
CS 162 Spring 2024
Project #1 
"""

from proj01_classes import *

def main():

#user interface to load existing house or create new one

    i = 0
    while True:
        if i == 1:
            break
        else:
            existing_house = input('Load existing house? (y/n): ').lower().strip()
            if existing_house == 'y':
                while True:
                    #loading an existing house
                    try:
                        folder_name = input('What is the name of the house?: ').lower().strip()
                        room_list = load_house(folder_name)
                        #recreating objects with saved arguments           
                        bathroom01 = room_list[0]
                        bedroom01 = room_list[1]
                        house = House(folder_name)
                        i += 1
                        break
                    except IndexError: #catches nonexistent houses
                        print('That house does not exist')
                        go_back = input('Do you need to create a new house instead? (y/n): ').lower().strip()
                        if go_back == 'y':
                            break
                        else:
                            continue

            elif existing_house == 'n':
                new_house = input('Create a new house? (y/n): ').lower().strip()
                if new_house == 'y':
                    #creating a new house
                    folder_name = input('What is the name of the house?: ').lower().strip()

                    bath_name = input('What is the bathroom name?: ') #setting bathroom name argument
                    while True:
                        try: #setting bathroom length argument
                            bath_length = float(input('What is the length of the bathroom? (ft): '))
                            if bath_length > 0:
                                break
                            else: #catches non positive numbers
                                print('Length must be a positive number')
                        except ValueError: #catches non integer or float values
                            print('Length must be a positive number')
                    while True:
                        try: #setting bathroom width argument
                            bath_width = float(input('What is the width of the bathroom? (ft): '))
                            if bath_width > 0:
                                break
                            else: #catches non positive numbers
                                print('Width must be a positive number')
                        except ValueError: #catches non integer or float values
                            print('Width must be a positive number')

                    bed_name = input('What is the bedroom name?: ') #setting bedroom name argument
                    while True:
                        try: #setting bedroom length argument
                            bed_length = float(input('What is the length of the bedroom? (ft): '))
                            if bed_length > 0:
                                break
                            else: #catches non positive numbers
                                print('Length must be a positive number')
                        except ValueError: #catches non integer or float values
                            print('Length must be a positive number')
                    while True:
                        try: #setting bedroom width argument
                            bed_width = float(input('What is the width of the bedroom? (ft): '))
                            if bed_width > 0:
                                break
                            else: #catches non positive numbers
                                print('Width must be a positive number')
                        except ValueError: #catches non integer or float values
                            print('Width must be a positive number')

                    #creating objects with arguments established above
                    bathroom01 = Bathroom(bath_name, bath_length, bath_width)
                    bedroom01 = Bedroom(bed_name, bed_length, bed_width)
                    room_list = [bathroom01, bedroom01]
                    house = House(folder_name)
                    break 
                else:
                    continue           
            else:
                print('Please enter y or n')


    while True:
        #main menu
        print("""
1. Get entire house information
2. Get total house area
3. Change Bedroom settings
4. Change Bathroom settings
5. Exit program
""")
        try:
            user_main = int(input('Enter your selection (1-5): '))

            if user_main == 1:
                get_house_info(room_list, house)
            
            if user_main == 2:
                house_area(room_list, house)

            elif user_main == 3:
                while True:
                    #bedroom menu
                    print("""
1. Get room information
2. Change room temperature
3. Lock/unlock the door
4. Turn on/off the light
5. Return to main menu
""")
                    try:
                        user_choice = int(input('Enter your selection (1-5): '))
                        if user_choice == 1:
                            get_room_info(bedroom01, house, room_list)
                        elif user_choice == 2:
                            change_temp(bedroom01, house, room_list)
                        elif user_choice == 3:
                            lock_door(bedroom01, house, room_list)
                        elif user_choice == 4:
                            light_switch(bedroom01, house, room_list)
                        elif user_choice == 5:
                            break
                        else: #catches user inputs outside of the 1-5 range
                            print('Please enter an integer from 1 to 5.')
                    except ValueError: #catches non-integer user inputs
                        print('Please enter an integer from 1 to 5.')
                
            elif user_main == 4:
                while True:
                    #bathroom menu
                    print("""
1. Get room information
2. Change room temperature
3. Lock/unlock the door
4. Turn on/off the light
5. Turn on/off faucet
6. Turn on/off shower
7. Turn on/off bath
8. Return to main menu
""")
                    try:
                        user_choice = int(input('Enter your selection (1-8): '))
                        if user_choice == 1:
                            get_room_info(bathroom01, house, room_list)
                        elif user_choice == 2:
                            change_temp(bathroom01, house, room_list)
                        elif user_choice == 3:
                            lock_door(bathroom01, house, room_list)
                        elif user_choice == 4:
                            light_switch(bathroom01, house, room_list)
                        elif user_choice == 5:
                            faucet(bathroom01, house, room_list)
                        elif user_choice == 6:
                            shower(bathroom01, house, room_list)
                        elif user_choice == 7:
                            bath(bathroom01, house, room_list)
                        elif user_choice == 8:
                            break
                        else: #catches user inputs outside of the 1-8 range
                            print('Please enter an integer from 1 to 8.')
                    except ValueError: #catches non-integer user inputs
                        print('Please enter an integer from 1 to 8.')

            elif user_main == 5: #exits program
                print('Thank you, goodbye!')
                house.house_save(room_list)
                quit()
        
            else: #catches user inputs outside of the 1-5 range
                print('Please enter an integer from 1 to 5.')

        except ValueError: #catches non-integer user inputs
            print('Please enter an integer from 1 to 5.')

main()