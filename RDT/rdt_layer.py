#########################################################
# Katie Schaumleffle
# OSU CS372
# Fall 2022
# Reliable Data Transmission (RDT)
##########################################################

##########################################################
# Sources Cited:
# https://pythonexamples.org/python-split-string-into-specific-length-chunks/
# https://edstem.org/us/courses/29340/discussion/2119852
# https://stackoverflow.com/questions/9475241/split-string-every-nth-character
# https://www.w3schools.com/python/python_lists.asp
# Kurose & Ross, Computer Networking: A Top-Down Approach (7th Edition), Chapter 3.4
# 
###########################################################


from segment import Segment


# #################################################################################################################### #
# RDTLayer                                                                                                             #
#                                                                                                                      #
# Description:                                                                                                         #
# The reliable data transfer (RDT) layer is used as a communication layer to resolve issues over an unreliable         #
# channel.                                                                                                             #
#                                                                                                                      #
#                                                                                                                      #
# Notes:                                                                                                               #
# This file is meant to be changed.                                                                                    #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #


class RDTLayer(object):
    # ################################################################################################################ #
    # Class Scope Variables                                                                                            #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    DATA_LENGTH = 4 # in characters                     # The length of the string data that will be sent per packet...
    FLOW_CONTROL_WIN_SIZE = 15 # in characters          # Receive window size for flow-control
    sendChannel = None
    receiveChannel = None
    dataToSend = ''
    currentIteration = 0                                # Use this for segment 'timeouts'
    
    # Add items as needed
    sentData = ''
    rcvdData = ''
    currWindow =[0,4]
    currSeqNum = 0
    expectedAck = 4
    serverData = []
    flow_control_segs = 3
    

    # ################################################################################################################ #
    # __init__()                                                                                                       #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def __init__(self):
        self.sendChannel = None
        self.receiveChannel = None
        self.dataToSend = ''
        self.currentIteration = 0

        # Add items as needed
        self.countSegmentTimeouts = 0
        self.seqnum = 0
        self.receiveData = ''
        self.receiveArr = []
        self.missingData = []
        self.preMissing = 0     #0 == false; 1 == true
        self.currAck = 0
        self.role = 0           #0 == server; 1 == client

    # ################################################################################################################ #
    # setSendChannel()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable sending lower-layer channel                                                 #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setSendChannel(self, channel):
        self.sendChannel = channel

    # ################################################################################################################ #
    # setReceiveChannel()                                                                                              #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable receiving lower-layer channel                                               #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setReceiveChannel(self, channel):
        self.receiveChannel = channel

    # ################################################################################################################ #
    # setDataToSend()                                                                                                  #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the string data to send                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setDataToSend(self,data):
        self.dataToSend = data
        
        # https://pythonexamples.org/python-split-string-into-specific-length-chunks/
        splitData = [data[x:x+(RDTLayer.DATA_LENGTH)] for x in range(0, len(data), RDTLayer.DATA_LENGTH)]

    # ################################################################################################################ #
    # getDataReceived()                                                                                                #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to get the currently received and buffered string data, in order                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def getDataReceived(self):
        # ############################################################################################################ #
        # Identify the data that has been received...
        return self.receiveData

    # ################################################################################################################ #
    # processData()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # "timeslice". Called by main once per iteration                                                                   #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processData(self):
        self.currentIteration += 1
        self.processSend()
        self.processReceiveAndSendRespond()

    # ################################################################################################################ #
    # processSend()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment sending tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processSend(self):
        # segmentSend = Segment()

        # ############################################################################################################ #
        # print('processSend(): Complete this...')
        
        # You should pipeline segments to fit the flow-control window
        # The flow-control window is the constant RDTLayer.FLOW_CONTROL_WIN_SIZE
        # The maximum data that you can send in a segment is RDTLayer.DATA_LENGTH
        # These constants are given in # characters

        # Somewhere in here you will be creating data segments to send.
        # The data is just part of the entire string that you are trying to send.
        # The seqnum is the sequence number for the segment (in character number, not bytes)

            
        # Split data string into segments of size self.DATA_LENGTH
        splitData = [self.dataToSend[i:i + self.DATA_LENGTH] for i in range(0, len(self.dataToSend), self.DATA_LENGTH)]

        if(splitData != None):
            self.role = 1

        if(self.currentIteration == 1 and self.role == 1):
            n = 0

            while n < self.flow_control_segs and n < (len(splitData) - self.seqnum):
                tempData = Segment()
                tempData.setData(str(n+self.seqnum), splitData[n+self.seqnum])
        
                # Display sending segment
                print("Sending segment: ", tempData.to_string())

                self.sendChannel.send(tempData)
                n += 1

            self.seqnum = n + self.seqnum


    # ################################################################################################################ #
    # processReceive()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment receive tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processReceiveAndSendRespond(self):
        segmentAck = Segment()                 # Segment acknowledging packet(s) received

        # This call returns a list of incoming segments (see Segment class)...
        listIncomingSegments = self.receiveChannel.receive()

        # ############################################################################################################ #
        # What segments have been received?
        # How will you get them back in order?
        # This is where a majority of your logic will be implemented
        print('processReceive(): Complete this...')

        sortedList = []
        receiveAck = []
        
        # Split data string into segments of size self.DATA_LENGTH
        splitData = [self.dataToSend[i:i + self.DATA_LENGTH] for i in range(0, len(self.dataToSend), self.DATA_LENGTH)]

        for i in range(len(listIncomingSegments)):
            listIncomingSegments[i].printToConsole()
            sortedList.append(int(listIncomingSegments[i].seqnum))
        
        sortedList.sort(reverse=True)

        # Read incoming segs into data or ack array
        if len(splitData) == 0 and self.preMissing == 0:
            for i in range(self.flow_control_segs):
                self.receiveArr.append(None)
        
        for i in range(len(sortedList)):
            if sortedList[i] != -1:
                for j in range(len(listIncomingSegments)):
                    if listIncomingSegments[j].checkChecksum() == True and int(listIncomingSegments[j].seqnum) == sortedList[i] and self.receiveArr[sortedList[i]] == None:
                        self.receiveArr[sortedList[i]] = listIncomingSegments[j].payload

            else:
                receiveAck.append(int(listIncomingSegments[i].acknum))

        # Collect missing data
        for i in range(len(self.receiveArr)):
            if self.receiveArr[i] == None:
                self.missingData.append(i)

            # Check for duplicates and remove
            elif self.missingData.count(i) > 0:
                self.missingData.remove(i)

        self.missingData = list(set(self.missingData))

        # Send Data segs
        if len(splitData) > 0:
            if len(receiveAck) > 0:
                dataMatchServer = 0     #False
                for i in range(len(receiveAck)):
                    if receiveAck[i] == self.seqnum:
                        dataMatchServer = 1     #True
                
                if dataMatchServer != 1:
                    receiveAck.sort()
                    for i in range(0, len(receiveAck)):
                        if len(splitData) > receiveAck[i]:
                            tempData = Segment()
                            tempData.setData(str(receiveAck[i]), splitData[receiveAck[i]])
                            print("Sending segment: ", tempData.to_string())
                            self.sendChannel.send(tempData)

                            # As per instructors suggestion, keeping track of segment timeouts
                            self.countSegmentTimeouts += 1

                elif self.currentIteration > 1:
                    n = 0
                    while n < (len(splitData) - self.seqnum) and n < self.flow_control_segs:
                        tempData = Segment()
                        tempData.setData(str(n+self.seqnum), splitData[n+self.seqnum])
                        print("Sending segment: ", tempData.to_string())
                        self.sendChannel.send(tempData)
                        n += 1
                    self.seqnum = n + self.seqnum

        # Send data ack segments
        else:
            self.missingData.sort()
            if len(self.missingData) == 0:
                self.receiveData = ''
                for i in range(len(self.receiveArr)):       
                    self.currAck = max(self.currAck, i)
                    self.receiveData = self.receiveData + self.receiveArr[i]
                self.currAck += 1
                segmentAck.setAck(self.currAck)
                self.sendChannel.send(segmentAck)
                print("Sending ack: ", segmentAck.to_string())
                self.preMissing = 0
            else:
                self.receiveData = ''
                for x in range(self.missingData[0]):       
                    self.currAck = max(self.currAck, x)
                    self.receiveData = self.receiveData + self.receiveArr[x]
                for x in range(len(self.missingData)):
                    temp = Segment()
                    temp.setAck(self.missingData[x])
                    self.sendChannel.send(temp)
                    print("Sending ack: ", temp.to_string())
                
                self.preMissing = 1

        
        # ############################################################################################################ #
        # Display response segment
        #segmentAck.setAck(currAck)
        # print("Sending ack: ", segmentAck.to_string())

        # # Use the unreliable sendChannel to send the ack packet
        # self.sendChannel.send(segmentAck)
