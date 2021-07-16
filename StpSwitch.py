# This defines a Spanning Tree Switch that serves as a Parent class to the switch class.
# It abstracts details of sending messages and verifying topologies.

from Message import *
        	          
class StpSwitch(object):

    def __init__(self, idNum, topolink, neighbors):
    # switchID = id of the switch (lowest value determines root switch and breaks ties)
    # topology = backlink to the Topology class. Used for sending messages.
    #   as follows: self.topology.send_message(message)
    # links = a list of the switch IDs linked to this switch.
        self.switchID = idNum
        self.topology = topolink
        self.links = neighbors

    # Invoked at initialization of topology of switches
    def verify_neighbors(self):
        for neighbor in self.links:
            if self.switchID not in self.topology.switches[neighbor].links:
                raise Exception(str(neighbor) + " does not have link to " + str(self.switchID))

    def send_message(self, message):
        self.topology.send_message(message)