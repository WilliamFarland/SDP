import multiprocessing
import os                                                               

# Creating the tuple of all the processes
all_processes = ('MainCode.py', 'MIDI.py')                                    
                                                  
# This block of code enables us to call the script from command line.                                                                                
def execute(process):                                                             
    os.system('python3 ' + str(process))                                       
                                                                                
                                                                                
process_pool = multiprocessing.Pool(processes = 2)                                                        
process_pool.map(execute, all_processes)
