# There is a house with 4 levels. In that house there is an elevator. You can program this elevator to go up or down, depending on what button the user touches inside the elevator.

# Valid levels must be only these numbers: 0,1,2,3

# Valid buttons must be only these strings: '0','1','2','3'

# Possible return values are these numbers: -3,-2,-1,0,1,2,3

# If the elevator is on the ground floor(0th level) and the user touches button '2' the elevator must go 2 levels up, so our function must return 2.

# If the elevator is on the 3rd level and the user touches button '0' the elevator must go 3 levels down, so our function must return -3.

# If the elevator is on the 2nd level, and the user touches button '2' the elevator must remain on the same level, so we return 0.

# We cannot endanger the lives of our passengers, so if we get erronous inputs, our elevator must remain on the same level. So for example:

# goto(2,'4') must return 0, because there is no button '4' in the elevator.
# goto(4,'0') must return 0, because there is no level 4.
# goto(3,undefined) must return 0.
# goto(undefined,'2') must return 0.
# goto([],'2') must return 0 because the type of the input level is array instead of a number.
# goto(3,{}) must return 0 because the type of the input button is object instead of a string.

#abstraction for controlling device
class Panel:

    #panel has only device as input
    def __init__(self, lift):
        self.lift = lift
    #panel should validate input info
    def validate_input(self, level_to_go):
        return isinstance(self.lift.current_level, int) and isinstance(level_to_go, str) and 0 <= self.lift.current_level < self.lift.floors_number and 0 <= int(level_to_go) < self.lift.floors_number
    #path to needed level 
    def goto(self, level_to_go):
            return self.lift.goto(level_to_go) if self.validate_input(level_to_go) else 0

#device
class Lift:
    #lift has number of floors and current floor(maybe current floor has to be 0 in constructor, and then to be set)
    def __init__(self, floors_number, current_level):
        self.floors_number = floors_number
        self.current_level = current_level
    #lift working only with valid info and setting desired level to his current
    def goto(self, level_to_go):
        dif, self.current_level = int(level_to_go) - self.current_level, level_to_go
        return dif

FLOORS_NUMBER = 4

def goto(current_level, level_to_go):
    lift = Lift(FLOORS_NUMBER, current_level)
    lift_panel = Panel(lift)
    return lift_panel.goto(level_to_go)


print(goto(1,'2'))
print(goto(3,'0'))
print(goto(2,'1'))
print(goto(4,'1'))
print(goto([],'1'))


        
        
        
# int(level_to_go) - int(current_level) self.validate_input(current_level, level_to_go) else 0