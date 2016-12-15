#Multiprocessing Remote Process
##Python program to run a process in the background within its own IPython kernel.
##Author: Derek Wilson
##Modified: 11 Dec 2016
####This python module will start a Python process in the background while allowing 
###users to monitor the process status and intecede (if necessary) in any of the 
###calculations or procedure.  Opening the process within the Ipython console allows 
###users to access resources otherwise hidden from view and detached from user's control.  

from multiprocessing import Process, Value, Array
from threading import Thread


class remoteProc():
    """The remoteProc class contains the shared Python variables as well
    as its own parameters and the "complicated" function requiring
    running in the background as its own process.  The main process can access 
    the multiprocessing variables of num, arr and keepLooping.  Users can control 
    the loop running in a thread by setting the value to 0.  

    """
    t1=None #held for thread
    x =1
    y =1
    infoData="This is data"
    keepLooping=True
    num=None
    arr=None

    def __init__(self,
                 num=Value('d', 0.0),
                 arr= Array('f', range(10)),
                 keepLooping=Value('i', 1)):
        """
        Instantiate the class setting the default variables.  
        Set  keepLooping to 0 to kill the loops.
        """
        self.num=num
        self.arr=arr
        self.keepLooping=keepLooping
    
    def doComplicatedStuff(self):
        """
        The arbitrary function or procedure to run in the background.  
        import anything here and control the loop by setting the keepLooping 
        value to 0.  Also watch the num variable increment by one each time.
        """
        import time
        while self.keepLooping.value>0:
            self.x=self.x+1
            self.y=self.y+2
            self.num.value+=1
            time.sleep(0.5)

    def startThread(self):
        """
        Run the function as a thread to allow users to interact with the class
        parameters independantly in Ipython.
        """
        t1=Thread(target=self.doComplicatedStuff, args=())
        t1.start()
        self.t1=t1
        
    

def launchIPythonProcess(num,arr,keepLooping):
    """
    Call the remoteProc function and start the thread.  Finally call Ipython to run the 
    class functions in a thread in the background
    """
    import IPython
    rP1=remoteProc(num,arr,keepLooping)
    rP1.startThread()
    IPython.embed_kernel()
    return rP1


def main():
    """
    Main test script to instantiate the shared variables, call the remote process and 
    run the process in the background.  Users can then access this remote process by
    opening its kernel in Ipython
    """
    num = Value('d', 0.0)
    arr = Array('f', range(10))
    keepLooping=Value('i', 1)##set the initial shared parameters

    #start the kernel in its own process so that the main process can proceed without delay.
    p1=Process(target=launchIPythonProcess, args=(num,arr,keepLooping,))
    p1.start()
    ##in the example loop, watch the value increment for num.value
    #1
    #2
    #3.....
    #
    
    p1.pid##get the process id.  users can access this process in Ipython as follows.
    ##ipython console --existing kernel-<your-pid-above>.json

    ##in the ipython console access the remote process variables
    #rP1.num.value
    #rP1.arr[:]
    #rP1.keepLooping.value

    ##you can even set and share these values
    ##rP1.num.value=4
    ##rP1.arr[0]=44.0
    ##and so on

    ##finally, to stop the loop in the main process just set
    ##keepLooping.value=0

    ##or just terminate the process
    ##p1.terminate()
    
