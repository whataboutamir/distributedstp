# This defines a Switch that can can send and receive spanning tree 
# messages to converge on a final loop free forwarding topology.  This
# class is a child class (specialization) of the StpSwitch class.

from Message import *
from StpSwitch import *

class Switch(StpSwitch):

    def __init__(self, idNum, topolink, neighbors):    
        # Invoke the super class constructor, which makes available to this object the following members:
        # -self.switchID                   (the ID number of this switch object)
        # -self.links                      (the list of switch IDs connected to this switch object)
        super(Switch, self).__init__(idNum, topolink, neighbors)
                
        # Data structure to keep track of this switch's view of the spanning tree.
        self.root = self.switchID
        self.distance = 0
        self.activeLinks = []
        self.switchThrough = self.switchID

    def send_initial_messages(self):
        # Create and send initial messages from this switch.
        for neighbour in self.links:
            msg = Message(self.root, self.distance, self.switchID, neighbour, False) 
            self.send_message(msg)

        return
        
    def process_message(self, message):
        # If the message has a lower claimedRoot, then: 
        #   update root, distance, activeLinks, and switchThrough and update neighbours.
        if message.root < self.root:
            self.root = message.root
            self.distance = message.distance + 1
            if self.activeLinks and self.switchThrough in self.activeLinks:
                self.activeLinks.remove(self.switchThrough)
            self.switchThrough = message.origin
            self.activeLinks.append(self.switchThrough)
            self.update_neighbours()
        # If the message has the same root but a shorter distance, then: 
        #   update distance, activeLinks, and switchThrough and update neighbours.
        elif message.root == self.root and (message.distance + 1) < self.distance:
            self.distance = message.distance + 1
            if self.activeLinks and self.switchThrough in self.activeLinks:
                self.activeLinks.remove(self.switchThrough)
            self.switchThrough = message.origin
            self.activeLinks.append(self.switchThrough)
            self.update_neighbours()
        # Tie breaker: if there are two paths of equal distance to the same root, then: 
        #   this switch should choose the path through the neighbour with the lowest ID.
        elif message.root == self.root and (message.distance + 1) == self.distance and message.origin < self.switchThrough:
            if self.activeLinks and self.switchThrough in self.activeLinks:
                self.activeLinks.remove(self.switchThrough)
            self.switchThrough = message.origin
            self.activeLinks.append(self.switchThrough)
            self.update_neighbours()
        
        # If the message has pathThrough = True but this switch doesn't have the message origin in its activeLinks, then:
        #   add it.
        if message.pathThrough == True and message.origin not in self.activeLinks:
            self.activeLinks.append(message.origin)
        # If the message has pathThrough = False but this switch does have the message origin in its activeLinks, then:
        #    remove it.
        elif message.pathThrough == False and (message.origin in self.activeLinks and message.origin != self.switchThrough):
            self.activeLinks.remove(message.origin)

        # Clean up activeLinks
        if self.activeLinks:
            self.activeLinks = list(set(self.activeLinks))
            self.activeLinks.sort()
        
        return
        
    def update_neighbours(self):
        # Update neighbours.
        for neighbour in self.links:
            pathThrough = False
            if neighbour == self.switchThrough:
                pathThrough = True
            msg = Message(self.root, self.distance, self.switchID, neighbour, pathThrough)
            self.send_message(msg)
            
    def generate_logstring(self):
        # Generate logstring for this switch.

        logstring = ""

        for activeLink in self.activeLinks:
            logitem = str(self.switchID) + " - " + str(activeLink)
            if activeLink == self.activeLinks[-1]:
                pass
            else:
                logitem += ", "
            logstring += logitem
        
        return logstring