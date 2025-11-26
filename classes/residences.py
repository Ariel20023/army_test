from symtable import Class



number_of_available_beds = 160

class Residences:
    def __init__(self,rooms = 10,soldiers_in_every_room = 8):
        self.rooms = rooms
        self.soldiers_in_every_room = soldiers_in_every_room


#---------------------------------------------------------------------------------------------
class Dorm(Residences):
    def __init__(self,rooms,soldiers_in_every_room,available_sleeping_beds = 80):
        super().__init__(rooms,soldiers_in_every_room)
        self.available_sleeping_beds = available_sleeping_beds


    def available_beds_in_this_home(self):
        return self.available_sleeping_beds


    def grab_a_bed(self):
        self.available_sleeping_beds -= 1



    def total_available_beds(self):
        global number_of_available_beds
        number_of_available_beds -=  self.available_sleeping_beds
        return  number_of_available_beds

#-------------------------------------------------------------------------------------------------
class Room(Dorm):
    def __init__(self,available_beds_in_the_room,rooms,soldiers_in_every_room,bedroom_number,available_sleeping_beds):
        super().__init__(rooms,soldiers_in_every_room,available_sleeping_beds)
        self.bedroom_number = bedroom_number
        self.available_beds_in_the_room = 8

    def available_beds_in_this_room(self):
        return self.available_beds_in_the_room






































