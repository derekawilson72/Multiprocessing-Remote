# Multiprocessing-Remote
Python program to run a process in the background within its own IPython kernel.

This python module will start a Python process in the background while allowing users to monitor the process status and intecede (if necessary) in any of the calculations or procedure.  Opening the process within the Ipython console allows users to access resources otherwise hidden from view and detached from user's control.  

##Instructions
###Main test script to instantiate the shared variables, call the remote process and run the process in the background.  Users can then access this remote process by opening its kernel in Ipython

num = Value('d', 0.0)

arr = Array('f', range(10))

keepLooping=Value('i', 1)##set the initial shared parameters

####start the kernel in its own process so that the main process can proceed without delay.
p1=Process(target=launchIPythonProcess, args=(num,arr,keepLooping,))
p1.start()
#####in the example loop, watch the value increment for num.value
1. 
2. 
3.  ....
#

p1.pid  ##get the process id.  users can access this process in Ipython as follows: 
ipython console --existing kernel-<your-pid-above>.json



####in the ipython console access the remote process variables
rP1.num.value

rP1.arr[:]

rP1.keepLooping.value

####you can even set and share these values
rP1.num.value=4

rP1.arr[0]=44.0
####...and so on

####finally, to stop the loop in the main process just set
keepLooping.value=0

####or just terminate the process
p1.terminate()
    
