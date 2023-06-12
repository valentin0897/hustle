from typing import List
from states import  State

class Position:
    def __init__(self) -> None:
        self.lead_hand_left = State.FREE
        self.lead_hand_right = State.FREE
        self.lead_leg_left = State.FREE
        self.lead_leg_right = State.FREE
        self.follow_hand_left = State.FREE
        self.follow_hand_right = State.FREE
        self.follow_leg_left = State.FREE
        self.follow_leg_right = State.FREE
    
    def set_all(self, lead_hand_left, lead_hand_right,
                lead_leg_left, lead_leg_right,
                follow_hand_left, follow_hand_right,
                follow_leg_left, follow_leg_right):
        self.lead_hand_left    = lead_hand_left    
        self.lead_hand_right   = lead_hand_right    
        self.lead_leg_left     = lead_leg_left      
        self.lead_leg_right    = lead_leg_right     
        self.follow_hand_left  = follow_hand_left    
        self.follow_hand_right = follow_hand_right  
        self.follow_leg_left   = follow_leg_left   
        self.follow_leg_right  = follow_leg_right  

    def set_lead_hand_left    (self, new_state):
        self.lead_hand_left = new_state

    def set_lead_hand_right   (self, new_state):
        self.lead_hand_right = new_state

    def set_lead_leg_left(self, new_state):
        self.lead_leg_left = new_state

    def set_lead_leg_right(self, new_state):
        self.lead_leg_right = new_state

    def set_follow_hand_left(self, new_state):
        self.follow_hand_left = new_state

    def set_follow_hand_right(self, new_state):
        self.follow_hand_right = new_state

    def set_follow_leg_left(self, new_state):
        self.follow_leg_left = new_state

    def set_follow_leg_right(self, new_state):
        self.follow_leg_right = new_state



class Element:
    def __init__(self, order: List[Position]) -> None:
        self.order = order

