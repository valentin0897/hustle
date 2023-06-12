from states import State, Role, Side, Weight

class Dancer:
    def __init__(self, role) -> None:
        self.role = role
        self.left_hand = Hand(Side.LEFT)
        self.right_hand = Hand(Side.RIGHT)
        self.left_leg = Leg(Side.LEFT, Weight.HALF)
        self.right_leg = Leg(Side.RIGHT, Weight.HALF)

    def __repr__(self) -> str:
        return f"\
Role: {self.role} \n\
Left Hand: {self.left_hand.state} \n\
Right Hand: {self.right_hand.state} \n\
Left Leg: {self.left_leg.state} \n\
Right Leg: {self.right_leg.state} \n"


class Hand:
    def __init__(self, side) -> None:
        self.side = side
        self.state = State.FREE

class Leg:
    def __init__(self, side, weight) -> None:
        self.side = side
        self.weight = weight
        self.state = State.FREE