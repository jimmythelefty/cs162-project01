"""project01_classes.py - Classes and functions for Project 01. 

This program consists of the classes and functions used by the 
james_franklin_proj01.py program to create a basic "Smart Home."

James Franklin
LBCC ID: x00359202
CS 162 Spring 2024
Project #1 
"""

#beginning of class section

class House:
    '''Class with an aggregation of Room objects.'''
    def __init__(self, name):
        self._name = name


    def calculate_area(self, rooms):
        '''Calculates total area of the house.
        
            Arguments:
                rooms: list of Room class objects
            Returns:
                area_counter: Float
        '''
        area_counter = float(0)
        for room in rooms:
            area_counter += room.calculate_area()

        return area_counter
    

    def house_info(self, rooms):
        '''Prints __str__ method for each Room object.
        
            Arguments:
                rooms: list of Room class objects.
            Returns: None
        '''
        for room in rooms:
            print(room)


    def house_save(self, rooms):
        '''Saves the objects with current arguments. Each room object
           is saved as .txt file inside a parent folder with the house
           name.
           
            Arguments:
                rooms: list of Room class objects
            Returns: None
        '''
        from pathlib import Path

        folder_name = str(self._name).lower().strip()
        cwd = Path.cwd()

        if Path(f'{folder_name}').exists() == False:
            (cwd / folder_name).mkdir(parents=True)
        else:
            pass

        for room in rooms:
            room.save(f'{folder_name}')
        


class Room:
    '''Parent class for each type of room in a house.'''
    def __init__(self, name, length, width, temp):
        '''Initializes Room class.
        
            Arguments:
                name: String
                length: Float or Int
                width: Float or Int
                temp: Int
            Returns: None
        '''
        self._name = name
        self._length = length
        self._width = width
        self.temp = temp



class Bedroom(Room):
    '''Child of Room class. Expands parent class to describe bedrooms.'''
    def __init__(self, name, length, width, temp=72, 
                 door=False, light=False):
        '''Initializes Bedroom class.
        
            Arguments:
                name: String
                length: Float or Int
                width: Float or Int
                temp: Int
                door: Boolean
                light: Boolean
            Returns: None
        '''
        super().__init__(name, length, width, temp)
        self.door = door
        self.light = light


    def calculate_area(self):
        '''Calculates area of room (length x width).
        
            Arguments: None
            Returns:
                Area: Float
        '''
        return float(self._length * self._width)
    

    def room_temp(self, new_temp):
        '''Sets room temperature to a new temperature.
        
            Arguments:
                new_temp: Int
            Returns: None
        '''
        self.temp = int(new_temp)


    def lock_door(self):
        '''Changes Boolean value of the door lock.
            
            Arguments: None
            Returns: None
        '''
        if self.door is False:
            self.door = True
        else:
            self.door = False


    def light_switch(self):
        '''Changes Boolean value of the light switch.
            
            Arguments: None
            Returns: None
        '''
        if self.light is False:
            self.light = True
        else:
            self.light = False


    def __str__(self):       
        '''Defines the message printed when print(self) is called.
        
            Arguments: None
            Returns:
                result: String
        '''
        if self.door is True:
            door_str = 'locked'
        else:
            door_str = 'unlocked'

        if self.light is False:
            light_str = 'off'
        else:
            light_str = 'on'

        result = f"""
{self._name} is {self._length} ft long by {self._width} ft wide.
Total area is {(self._length * self._width)} square feet.
Room temperature is {self.temp} degrees Farenheit.
The door is {door_str} and the light is {light_str}.
"""
        return result


    def save(self, house_folder):
        '''Saves the current object arguments as a .txt file
           inside the house parent directory.
           
            Arguments:
                house_folder: string
            Returns: None
        '''
        from pathlib import Path

        file_name = str(self._name).replace(' ', '_').lower().strip()
        script_dir = Path(house_folder)
        save_path = script_dir / f'{file_name}.txt'

        with open(save_path, "w", encoding='utf-8') as output_file:
            output_file.write('Bedroom\n')
            output_file.write(f'{self._name}\n')
            output_file.write(f'{self._length}\n')
            output_file.write(f'{self._width}\n')
            output_file.write(f'{self.temp}\n')
            output_file.write(f'{self.door}\n')
            output_file.write(f'{self.light}\n')



class Bathroom(Room):
    '''Child of Room class. Expands parent class to describe bathrooms.'''
    def __init__(self, name, length, width, temp=72, door=False, 
                 light=False, sink=False, shower=False, bath=False, 
                 toilet=False, sink_temp=50, shower_temp=50, bath_temp=50):
        '''Initializes Bedroom class.
        
            Arguments:
                name: String
                length: Float or Int
                width: Float or Int
                temp: Int
                door: Boolean
                light: Boolean
                sink: Boolean
                shower: Boolean
                bath: Boolean
                sink_temp: Int
                shower_temp: Int
                bath_temp: Int
            Returns: None
        '''
        super().__init__(name, length, width, temp)
        self.door = door
        self.light = light
        self.sink = sink
        self.shower = shower
        self.bath = bath
        self.toilet = toilet
        self.sink_temp = sink_temp
        self.shower_temp = shower_temp
        self.bath_temp = bath_temp


    def calculate_area(self):
        '''Calculates area of room (length x width).
        
            Arguments: None
            Returns:
                Area: Float
        '''
        return float(self._length * self._width)


    def room_temp(self, new_temp):
        '''Sets room temperature to a new temperature.
        
            Arguments:
                new_temp: Int
            Returns: None
        '''
        self.temp = int(new_temp)


    def lock_door(self):
        '''Changes Boolean value of the door lock.
            
            Arguments: None
            Returns: None
        '''
        if self.door is False:
            self.door = True
        else:
            self.door = False
    

    def light_switch(self):
        '''Changes Boolean value of the light switch.
            
            Arguments: None
            Returns: None
        '''
        if self.light is False:
            self.light = True
        else:
            self.light = False


    def use_sink(self):
        '''Changes Boolean value of the sink.
            
            Arguments: None
            Returns: None
        '''
        if self.sink is False:
            self.sink = True
        else:
            self.sink = False
    

    def use_shower(self):
        '''Changes Boolean value of the shower.
            
            Arguments: None
            Returns: None
        '''
        if self.shower is False:
            self.shower = True
        else:
            self.shower = False


    def use_bath(self):
        '''Changes Boolean value of the bath.
            
            Arguments: None
            Returns: None
        '''
        if self.bath is False:
            self.bath = True
        else:
            self.bath = False


    def use_toilet(self):
        '''Flushes toilet-Changes Boolean value to True for 5 seconds,
        then changes Boolean value back to False.
        
            Arguments: None
            Returns: None
        '''
        import time

        self.toilet = True
        time.sleep(5) 
        self.toilet = False


    def sink_temp_set(self, new_temp):
        '''Sets sink water to a new temperature.
        
            Arguments:
                new_temp: Int
            Returns: None
        '''
        self.sink_temp = int(new_temp)


    def shower_temp_set(self, new_temp):
        '''Sets shower water to a new temperature.
        
            Arguments:
                new_temp: Int
            Returns: None
        '''
        self.shower_temp = int(new_temp)


    def bath_temp_set(self, new_temp):
        '''Sets bath water to a new temperature.
        
            Arguments:
                new_temp: Int
            Returns: None
        '''
        self.bath_temp = int(new_temp)


    def __str__(self):       
        '''Defines the message printed when print(self) is called.
        
            Arguments: None
            Returns:
                result: String
        '''
        if self.door is True:
            door_str = 'locked'
        else:
            door_str = 'unlocked'

        if self.light is False:
            light_str = 'off'
        else:
            light_str = 'on'

        if self.sink is False:
            sink_str = 'off'
        else:
            sink_str = 'on'

        if self.shower is False:
            shower_str = 'off'
        else:
            shower_str = 'on'

        if self.bath is False:
            bath_str = 'off'
        else:
            bath_str = 'on'    

        result = f"""
{self._name} is {self._length} ft long by {self._width} ft wide.
Total area is {(self._length * self._width)} square feet.
Room temperature is {self.temp} degrees Farenheit.
The door is {door_str} and the light is {light_str}.
The sink is {sink_str}, with a water temp of {self.sink_temp} degrees Farenheit.
The shower is {shower_str}, with a water temp of {self.shower_temp} degrees Farenheit.
The bath is {bath_str}, with a water temp of {self.bath_temp} degrees Farenheit.
"""
        return result


    def save(self, house_folder):
        '''Saves the current object arguments as a .txt file
           inside the house parent directory.
           
            Arguments:
                house_folder: string
            Returns: None
        '''
        from pathlib import Path

        file_name = str(self._name).replace(' ', '_').lower().strip()
        script_dir = Path(house_folder)
        save_path = script_dir / f'{file_name}.txt'

        with open(save_path, "w", encoding='utf-8') as output_file:
            output_file.write('Bathroom\n')
            output_file.write(f'{self._name}\n')
            output_file.write(f'{self._length}\n')
            output_file.write(f'{self._width}\n')
            output_file.write(f'{self.temp}\n')
            output_file.write(f'{self.door}\n')
            output_file.write(f'{self.light}\n')
            output_file.write(f'{self.sink}\n')  
            output_file.write(f'{self.shower}\n')
            output_file.write(f'{self.bath}\n')
            output_file.write(f'{self.toilet}\n')
            output_file.write(f'{self.sink_temp}\n')
            output_file.write(f'{self.shower_temp}\n')
            output_file.write(f'{self.bath_temp}\n')

#end of class section

#beginning of user interface functions

def load_house(house):
    '''Loads the .txt files inside the 'house' directory'''
    import os
    from pathlib import Path

    room_list = []
    for dirName, subDirList, fileList in os.walk(house):
        i = 0
        for file in fileList: #iterates through parent folder for each text file
            cwd = Path.cwd()
            file_path = cwd / house / file
            with open(file_path, "r", encoding='utf-8') as input_file:
                lines = input_file.readlines()
                if lines[0] == 'Bathroom\n':
                    #recreating a Bathroom class using lines from text file as arguments
                    room = Bathroom(f'{lines[1].strip()}', float(lines[2]), 
                                    float(lines[3]), int(lines[4]), bool(lines[5]), 
                                    bool(lines[6]), bool(lines[7]), bool(lines[8]), 
                                    bool(lines[9]), bool(lines[10]), int(lines[11]),
                                    int(lines[12]), int(lines[13]))
                    room_list.append(room) #adds class object to room_list

                if lines[0] == 'Bedroom\n':
                    #recreating a Bedroom class using lines from text file as arguments
                    room = Bedroom(f'{lines[1].strip()}', float(lines[2]), 
                                   float(lines[3]), int(lines[4]), 
                                   bool(lines[5]), bool(lines[6]))
                    room_list.append(room) #adds class object to room_list

    return room_list



def get_house_info(room_list, house):
    '''Prints the house.house_info() method,
    then offers an option to exit program or return to menu.
    
        Arguments:
            room_list: list of Room class instances
            house: House class instance
        Returns: None
    '''
    print(house.house_info(room_list))
    while True:
        try:
            user_continue = input('Do you need anything else? (y/n): ').lower().strip()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                house.house_save(room_list)
                print('Thank you, goodbye!')
                quit()
            else: #catches user input not 'y' or 'n'
                print('Please enter y or n.')
        except ValueError: #catches user input errors
            print('Please enter y or n.')


def house_area(room_list, house):
    '''Prints the house.calculate_area() method,
    then offers an option to exit program or return to menu.
    
        Arguments:
            room_list: list of Room class instances
            house: House class instance
        Returns: None
    '''   
    print(f' The house is {house.calculate_area(room_list)} square feet.')
    while True:
        try:
            user_continue = input('Do you need anything else? (y/n): ').lower().strip()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                print('Thank you, goodbye!')
                house.house_save(room_list)
                quit()
            else: #catches user input not 'y' or 'n'
                print('Please enter y or n.')
        except ValueError: #catches user input errors
            print('Please enter y or n.')


def get_room_info(room, house, room_list):
    '''Prints the room's __str__ method,
    then offers an option to exit program or return to menu.
    
        Arguments:
            room: Room class instance
        Returns: None
    '''
    print(room)
    while True:
        try:
            user_continue = input('Do you need anything else? (y/n): ').lower().strip()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                print('Thank you, goodbye!')
                house.house_save(room_list)
                quit()
            else: #catches user input not 'y' or 'n'
                print('Please enter y or n.')
        except ValueError: #catches user input errors
            print('Please enter y or n.')


def change_temp(room, house, room_list):
    '''Changes room's temperature,
    then offers an option to exit program or return to menu.
    
        Arguments:
            room: Room class instance
        Returns: None
    '''
    while True:
        try:
            new_temp = int(input('Enter a new temperature (60-80): '))
            if 60 <= new_temp <= 80:
                room.room_temp(new_temp)
                while True:
                    try:
                        user_continue = input('Do you need anything else? (y/n): ').lower().strip()
                        if user_continue == 'y':
                            break
                        elif user_continue == 'n':
                            print('Thank you, goodbye!')
                            house.house_save(room_list)
                            quit()
                        else: #catches user input not 'y' or 'n'
                            print('Please enter y or n.')
                    except ValueError: #catches user input errors
                        print('Please enter y or n.')
                break
            else: #catches integer inputs outside of the 60-80 range
                print('Please enter an integer from 60 to 80.')
        except ValueError: #catches non-integer user inputs
            print('Please enter an integer from 60 to 80.')


def lock_door(room, house, room_list):
    '''Changes door lock Boolean value,
    then offers an option to exit program or return to menu.
    
        Arguments:
            room: Room class instance
        Returns: None
    '''
    room.lock_door()
    while True:
        try:
            user_continue = input('Do you need anything else? (y/n): ').lower().strip()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                print('Thank you, goodbye!')
                house.house_save(room_list)
                quit()
            else: #catches user input not 'y' or 'n'
                print('Please enter y or n.')
        except ValueError: #catches user input errors
            print('Please enter y or n.')


def light_switch(room, house, room_list):
    '''Changes light switch Boolean value,
    then offers an option to exit program or return to menu.
    
        Arguments:
            room: Room class instance
        Returns: None
    '''
    room.light_switch()
    while True:
        try:
            user_continue = input('Do you need anything else? (y/n): ').lower().strip()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                print('Thank you, goodbye!')
                house.house_save(room_list)
                quit()
            else: #catches user input not 'y' or 'n'
                print('Please enter y or n.')
        except ValueError: #catches user input errors
            print('Please enter y or n.')


def faucet(bathroom, house, room_list):
    '''Changes sink Boolean value. If sink is being turned on, then the
    self.sink_temp_set(new_temp) method will be called to set the water
    temperature. Finally, the function offers an option to exit program 
    or return to menu.
    
        Arguments:
            bathroom: Bathroom class instance
        Returns: None
    '''
    if bathroom.sink == True:
        bathroom.use_sink()
    else:
        bathroom.use_sink()
        while True:
            try:
                water_temp = int(input('Set water temperature (50-130): '))
                if 50 <= water_temp <= 130:
                    bathroom.sink_temp_set(water_temp)
                    break
                else: #catches integer inputs outside of the 50-130 range
                    print('Please enter an integer from 50 to 130')
            except ValueError: #catches non-integer user inputs
                print('Please enter an integer from 50 to 130')

    while True:
        try:
            user_continue = input('Do you need anything else? (y/n): ').lower().strip()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                print('Thank you, goodbye!')
                house.house_save(room_list)
                quit()
            else: #catches user input not 'y' or 'n'
                print('Please enter y or n.')
        except ValueError: #catches user input errors
            print('Please enter y or n.')


def shower(bathroom, house, room_list):
    '''Changes shower Boolean value. If shower is being turned on, then the
    self.shower_temp_set(new_temp) method will be called to set the water
    temperature. Finally, the function offers an option to exit program 
    or return to menu.
    
        Arguments:
            bathroom: Bathroom class instance
        Returns: None
    '''
    if bathroom.shower == True:
        bathroom.use_shower()
    else:
        bathroom.use_shower()
        while True:
            try:
                water_temp = int(input('Set water temperature (50-130): '))
                if 50 <= water_temp <= 130:
                    bathroom.shower_temp_set(water_temp)
                    break
                else: #catches integer inputs outside of the 50-130 range
                    print('Please enter an integer from 50 to 130')
            except ValueError: #catches non-integer user inputs
                print('Please enter an integer from 50 to 130')

    while True:
        try:
            user_continue = input('Do you need anything else? (y/n): ').lower().strip()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                print('Thank you, goodbye!')
                house.house_save(room_list)
                quit()
            else: #catches user input not 'y' or 'n'
                print('Please enter y or n.')
        except ValueError: #catches user input errors
            print('Please enter y or n.')

def bath(bathroom, house, room_list):
    '''Changes bath Boolean value. If bath is being turned on, then the
    self.bath_temp_set(new_temp) method will be called to set the water
    temperature. Finally, the function offers an option to exit program 
    or return to menu.
    
        Arguments:
            bathroom: Bathroom class instance
        Returns: None
    '''   
    if bathroom.bath == True:
        bathroom.use_bath()
    else:
        bathroom.use_bath()
        while True:
            try:
                water_temp = int(input('Set water temperature (50-130): '))
                if 50 <= water_temp <= 130:
                    bathroom.bath_temp_set(water_temp)
                    break
                else: #catches integer inputs outside of the 50-130 range
                    print('Please enter an integer from 50 to 130')
            except ValueError: #catches non-integer user inputs
                print('Please enter an integer from 50 to 130')

    while True:
        try:
            user_continue = input('Do you need anything else? (y/n): ').lower().strip()
            if user_continue == 'y':
                break
            elif user_continue == 'n':
                print('Thank you, goodbye!')
                house.house_save(room_list)
                quit()
            else: #catches user input not 'y' or 'n'
                print('Please enter y or n.')
        except ValueError: #catches user input errors
            print('Please enter y or n.')


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

