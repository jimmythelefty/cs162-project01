
from proj01_classes import House, Room, Bathroom, Bedroom
import pytest


def test_house_creation():
    house = House('Anon')
    assert house._name == 'Anon'


def test_room_creation():
    room = Room('Basic Room', 15, 15, 72)
    assert room._name == 'Basic Room'
    assert room._length == 15
    assert room._width == 15
    assert room.temp == 72
    

def test_bathroom_creation():
    bathroom = Bathroom('Main Bathroom', 8, 6)

    assert bathroom._name == 'Main Bathroom'
    assert bathroom._length == 8
    assert bathroom._width == 6
    assert bathroom.temp == 72
    assert bathroom.door == False
    assert bathroom.light == False
    assert bathroom.sink == False
    assert bathroom.shower == False
    assert bathroom.bath == False
    assert bathroom.toilet == False
    assert bathroom.sink_temp == 50
    assert bathroom.shower_temp == 50
    assert bathroom.bath_temp == 50


def test_bathroom_controls():
    bathroom = Bathroom('Main Bathroom', 8, 6)
    bathroom.room_temp(65)
    bathroom.lock_door()
    bathroom.light_switch()
    bathroom.sink = True
    bathroom.shower = True
    bathroom.bath = True
    bathroom.use_toilet()
    bathroom.sink_temp_set(85)
    bathroom.shower_temp_set(85)
    bathroom.bath_temp_set(85)

    assert bathroom.temp == 65
    assert bathroom.door == True
    assert bathroom.light == True
    assert bathroom.sink == True
    assert bathroom.shower == True
    assert bathroom.bath == True
    assert bathroom.toilet == False
    assert bathroom.sink_temp == 85
    assert bathroom.shower_temp == 85
    assert bathroom.bath_temp == 85


def test_bedroom_creation():
    bedroom = Bedroom('Main Bedroom', 12, 10)

    assert bedroom._name == 'Main Bedroom'
    assert bedroom._length == 12
    assert bedroom._width == 10
    assert bedroom.temp == 72
    assert bedroom.door == False
    assert bedroom.light == False


def test_bedroom_controls():
    bedroom = Bedroom('Main Bedroom', 12, 10)
    bedroom.room_temp(65)
    bedroom.lock_door()
    bedroom.light_switch()

    assert bedroom.temp == 65
    assert bedroom.door == True
    assert bedroom.light == True




