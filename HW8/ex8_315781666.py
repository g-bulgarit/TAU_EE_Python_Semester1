''' Exercise #8. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################
class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:

    def  __init__(self, floor, number, guests, clean_level, rank, satisfaction = 1.0):
        self.floor = int(floor)
        self.number = int(number)
        self.guests = []
        # Convert guests to lowercase
        for name in guests:
            self.guests.append(name.lower())

        # Deal with cleanliness...
        if type(clean_level) != int:
            raise TypeError("Cleanliness level should be integer.")
        if clean_level < 1 or clean_level > 10:
            raise ValueError("Clean level is out of bounds.")
        self.clean_level = int(clean_level)

        self.can_be_cleaned = True

        # Deal with rank:
        if type(rank) != int:
            raise TypeError("Rank should be integer.")
        if rank < 1 or rank > 3:
            raise TypeError("Rank is out of bounds.")
        self.rank = int(rank)

        # Deal with satisfaction
        if type(satisfaction) != int and type(satisfaction) != float:
            raise  TypeError("Satisfaction should be int or float...")
        if satisfaction < 1.0 or satisfaction > 5.0:
            raise ValueError("Satisfaction is out of bounds.")
        self.satisfaction = float(satisfaction)

    def __repr__(self):
        # Huge format string...
        if len(self.guests) == 0:
            formatted_guests = "empty"
        else:
            formatted_guests = ", ".join(self.guests)
        output_str = f"floor: {self.floor}\n" \
                     f"number: {self.number}\n" \
                     f"guests: {formatted_guests}\n" \
                     f"clean_level: {self.clean_level}\n" \
                     f"rank: {self.rank}\n" \
                     f"satisfaction: {round(self.satisfaction,1)}"
        return output_str

    def is_occupied(self):
        return bool(len(self.guests))

    def can_clean(self):
        return self.can_be_cleaned

    def clean(self):
        if self.can_clean():
            self.clean_level = min(10,self.clean_level + self.rank)
        else:
            raise RoomError("Room cannot be cleaned")

    def better_than(self, other):
        if type(other) != Room:
            raise TypeError("Incorrect room type")
        return ((self.rank,
                 self.floor,
                 self.clean_level) > (other.rank,
                                      other.floor,
                                      other.clean_level))

    def check_in(self, guests):
        if len(self.guests) != 0:
            raise RoomError("Cannot check-in new guests to an occupied room")
        for guest in guests:
            self.guests.append(guest.lower())
        self.satisfaction = 1.0

    def check_out(self):
        if len(self.guests) == 0:
            raise RoomError("Cannot check-out an empty room")
        self.guests = []

    def move_to(self, other):
        if len(self.guests) == 0:
            raise RoomError("Cannot move guests from an empty room")
        if len(other.guests) != 0:
            # Occupied...
            raise RoomError("Cannot move guests to an occupied room")
        else:
            # Move the dudessss
            for guest in self.guests:
                other.guests.append(guest)

            # Check if the other room is better!
            if (self.rank,
                self.floor,
                self.clean_level) < (other.rank,
                                      other.floor,
                                      other.clean_level):
                # Raise satisfaction
                other.satisfaction = min(5.0, self.satisfaction + 1.0)
            # Erase guests from self
            self.guests = []

#########################################
# Question 2 - do not delete this comment
#########################################
class BudgetRoom(Room):
    def  __init__(self, floor, number, guests, clean_level,
                  rank=1, satisfaction=1.0, clean_stock=0):
        super().__init__(floor ,number, guests, clean_level, rank, satisfaction)
        self.clean_stock = clean_stock


    def __repr__(self):
        output_str = super().__repr__() + "\n"
        addition = f"type: BudgetRoom\n" \
                   f"clean_stock: {self.clean_level}"
        output_str += addition
        return output_str

    def is_occupied(self):
        return super().is_occupied()

    def can_clean(self):
        if self.clean_stock > 0:
            self.can_be_cleaned = True
        else:
            self.can_be_cleaned = False
        return self.can_be_cleaned

    def clean(self):
        self.can_clean()
        super().clean()
        self.clean_stock -= 1

    def better_than(self, other):
        return super().better_than(other)

    def check_in(self, guests):
        super().clean()
        if len(self.guests) == 0:
            self.clean_stock = 0

    def check_out(self):
        super().check_out()

    def move_to(self, other):
        super().move_to(other)
        if type(other) == BudgetRoom:
            other.clean_stock = self.clean_stock
    # Replace this comment with your methods' implementation

    def grant_clean(self):
        if len(self.guests) == 0:
            raise RoomError("Cannot grant an empty room")
        self.clean_stock += 1
        self.satisfaction = min(5.0, self.satisfaction + 0.5)

    def grant_snack(self):
        # Looks like another mistake in the pdf...
        if len(self.guests) == 0:
            raise RoomError("Cannot grant an empty room")
        self.satisfaction = min(5.0, self.satisfaction + 0.8)
        self.clean_level = min(5.0, self.satisfaction + 0.8)



class LegacyRoom(Room):
    def  __init__(self, floor, number, guests,
                  clean_level, rank=2, satisfaction=1.0,
                  minibar_drinks = 2, minibar_snacks = 2):
        super().__init__(floor, number, guests, clean_level, rank, satisfaction)
        self.minibar_drinks = minibar_drinks
        self.minibar_snacks = minibar_snacks


    def __repr__(self):
        output_str = super().__repr__() + "\n"
        addition = f"type: LegacyRoom\n" \
                   f"minibar_drinks: {self.minibar_drinks}" \
                   f"minibar_snacks: {self.minibar_snacks}"
        output_str += addition
        return output_str

    def is_occupied(self):
        return super().is_occupied()

    def can_clean(self):
        return True

    def clean(self):
        super().clean()

    def better_than(self, other):
        super().better_than(other)

    def check_in(self, guests):
        super().check_in(guests)
        self.minibar_snacks = 2
        self.minibar_drinks = 2

    def check_out(self):
        super().check_out()

    def move_to(self, other):
        super().move_to(other)

    def add_drinks(self, quantity):
        self.minibar_drinks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.2 * quantity)

    def add_snacks(self, quantity):
        self.minibar_snacks += quantity
        self.satisfaction += min(5.0, self.satisfaction + 0.3 * quantity)
        self.clean_level = max(1, self.clean_level - 1)

#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = str(name)
        self.rooms = list(rooms)
        self.num_budget_rooms = 0
        self.num_legacy_rooms = 0
        self.num_occupied_rooms = 0

        for room in rooms:
            if room.is_occupied():
                self.num_occupied_rooms += 1
            if type(room) == BudgetRoom:
                self.num_budget_rooms += 1
            if type(room) == LegacyRoom:
                self.num_legacy_rooms += 1
        self.num_other_rooms = len(rooms) - self.num_legacy_rooms - self.num_budget_rooms


    def __repr__(self):
        output = f"{self.name} hotel has:\n" \
                 f"{self.num_budget_rooms} BudgetRooms" \
                 f"{self.num_legacy_rooms} LegacyRooms" \
                 f"{self.num_other_rooms} other room types" \
                 f"{self.num_occupied_rooms} occupied rooms"
    def check_in(self, guests, rank):
        pass # replace this with your implementation

    def check_out(self, guest):
        pass # replace this with your implementation

    def upgrade(self, guest):
        pass # replace this with your implementation

h = Hotel("Best",[BudgetRoom(15, 140, [], 5), BudgetRoom(1, 2,["Liat"], 7)])
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