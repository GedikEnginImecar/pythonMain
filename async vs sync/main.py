# necessary modules
import multiprocessing
import time


# square numbers up to n to get cpu to do calculations/'something'
def cpu_bound_task(n):
    return sum(i * i for i in range(n))


# single-threaded func

# calls cpu based task

def single_threaded(n, avg):
    total_time = 0
    for i in range(avg):    
        start_time = time.time()  # starts time
        cpu_bound_task(n)  # ends time
        end_time = time.time()  # returns time difference
        total_time += end_time - start_time

    print("Average single-threaded time:", total_time/avg)


# multi-thread func

def multi_processed(n, avg):
    start_time = time.time()  # start timer
    processes = []
    num_processes = multiprocessing.cpu_count()  # number of processes = number of cpu cores
    total_time = 0
    # create & start multiple processes to execute the task concurrently
    for i in range(num_processes):
        part_n = max(1, n // num_processes)  # calc portion of task per cpu & ensures that there is at least one task per core

        process = multiprocessing.Process(target=cpu_bound_task, args=(part_n,))  # Create a Process object configured to run the cpu_bound_task function with part_n as an argument

        processes.append(process)  # Start the process

        process.start()  # Keep track of the process objects

    # wait for process to complete
    for process in processes:
        process.join()  # joins the different threads outputs
        end_time = time.time()  # get end time
        total_time += end_time - start_time
    print("Average multi-processed time:", total_time/avg)  # return how long it takes to run


# The following condition checks if this script is the main program and is not being imported by another script
# This is crucial in Windows to prevent recursive process spawning when using multiprocessing
if __name__ == '__main__':
    n = 10000000  # n is the number you want the square up to, designed to test cpu
    avg = 10
    single_threaded(n, avg)  # call single thread
    multi_processed(n, avg)  # call multi thread
