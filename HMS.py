''' Hostel Management System '''
class Student:
    def __init__(self,stud_id,course):
        self.stud_id=stud_id 
        self.course=course 
    def display(self):
        print(f"Details of student are: \n Student ID:{self.stud_id} \n Course:{self.course}.")
    def demands_room(self,hostel,room):
        hostel.checks_availability(room)

class Room:
    def __init__(self,room_no):
        self.room_no=room_no 
        self.rooms=True
        self.room_available=None 
    def display(self):
        print(f"The room no. is:{self.room_no}.")
    def details(self):
        if self.rooms==True:
            self.room_available=True 
        else:
            self.room_available=False


class Hostel:
    def __init__(self,hostel_name,total_rooms):
        self.hostel_name=hostel_name 
        self.total_rooms=total_rooms 
    def display(self):
        print(f"Hostel Details are: \n Name of Hostel:{self.hostel_name} \n Total rooms:{self.total_rooms}.")
    def checks_availability(self,room):
        room.details()
        if room.room_available==True:
            print("Room is available!")
            self.allocate_room(room)
        else:
            print("Room is not available!")

    def allocate_room(self,room):
        print(f"{room.room_no} is yours.")

s1=Student("S12","Bca")
s2=Student("S22","Btech")
s1.display()
s2.display()
r1=Room(213)
r2=Room(214)
r1.display()
r2.display()
h1=Hostel("Prayag",220)
h2=Hostel("Marco",240)
h1.display()
h2.display()
s1.demands_room(h1,r1)
