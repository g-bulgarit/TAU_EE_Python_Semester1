''' Exercise #8. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################
class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:
    # Not required but I'm used to doing it like this...
    floor = None
    number = None
    guests = []
    clean_level = None
    rank = None
    satisfaction = None

    def  __init__(self, floor, number, guests, clean_level, rank, satisfaction = 1.0):
        self.floor = int(floor)
        self.number = int(number)

        # Convert guests to lowercase
        for name in guests:
            self.guests.append(name.lower())

        # Deal with cleanliness...
        if type(clean_level) != int:
            raise TypeError("Cleanliness level should be integer.")
        if clean_level < 1 or clean_level > 10:
            raise ValueError("Clean level is out of bounds.")
        self.clean_level = int(clean_level)

        # Deal with rank:
        if type(rank) != int:
            raise TypeError("Rank should be integer.")
        if rank < 1 or rank > 3:
            raise TypeError("Rank is out of bounds.")
        self.rank = int(rank)

        # Deal with satisfaction
        if type(satisfaction) != int or type(satisfaction) != float:
            raise  TypeError("Satisfaction should be int or float...")
        if satisfaction < 1 or satisfaction > 5:
            raise ValueError("Satisfaction is out of bounds.")
        self.satisfaction = float(satisfaction)

    def __repr__(self):
        pass # replace this with your implementation

    def is_occupied(self):
        pass # replace this with your implementation

    def can_clean(self):
        pass # replace this with your implementation

    def clean(self):
        pass # replace this with your implementation

    def better_than(self, other):
        pass # replace this with your implementation

    def check_in(self, guests):
        pass # replace this with your implementation

    def check_out(self):
        pass # replace this with your implementation
    
    def move_to(self, other):
        pass # replace this with your implementation

#########################################
# Question 2 - do not delete this comment
#########################################
class BudgetRoom(Room):
    def  __init__(self, floor, number, guests, clean_level,\
                  rank=1, satisfaction=1.0, clean_stock=0):
        pass # replace this with your implementation

    def __repr__(self):
        pass # replace this with your implementation


    # Replace this comment with your methods' implementation


class LegacyRoom(Room):
    def  __init__(self, floor, number, guests, clean_level,\
                  rank=2, satisfaction=1.0,\
                  minibar_drinks = 2, minibar_snacks = 2):
        pass # replace this with your implementation

    def __repr__(self):
        pass # replace this with your implementation


    # Replace this comment with your methods' implementation

   
#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        pass # replace this with your implementation
            
    def __repr__(self):
        pass # replace this with your implementation
                      
    def check_in(self, guests, rank):
        pass # replace this with your implementation

    def check_out(self, guest):
        pass # replace this with your implementation

    def upgrade(self, guest):
        pass # replace this with your implementation

#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    rooms = [BudgetRoom(15, 140, [], 5), LegacyRoom(12, 101, ["Ronen", "Shir"], 6),\
             BudgetRoom(1, 2, ["Liat"], 7), Room(2, 23, [], 6, 3)]
    h = Hotel("Dan",rooms)
    test_sep = '\n------------------'
    print ('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print ('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep,  sep="")
    print ('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print ('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
    print ('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
    print ('PRINT h:\n', h, test_sep, sep="")
    print ('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print ('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print ('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print ('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print ('PRINT h:\n', h, test_sep, sep="")


#########################################
# Main code - do not delete this comment
# You can add more validation cases below
#########################################

##test_hotel() 
## After you are done implenting all classes and methods, you may comment-in the call to test_hotel() and compare the results with the content of test_hotel_output.txt