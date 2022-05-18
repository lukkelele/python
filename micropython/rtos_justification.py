import time

condition1 = 0
condition2 = 0
condition3 = 0

def super_loop(verbose=False):
    if verbose: print("==> Super loop")
    # Loop forever
    while True:
        if condition1: get_temp()
        elif condition2: display_clock()
        elif condition3: ping()
        else:
            print("loop done")
            time.sleep(1)
            

def event_driven_asynchronous(verbose=False):
    if verbose: print("==> Event Driven: Asynchronous")

def event_driven_synchronous(verbose=False):
    if verbose: print("==> Event Driven: Synchronous")

def ping(verbose=False):
    if verbose: print("==> Pinging...")

def get_temp(verbose=False):
    if verbose: print("==> Gathering temperature")
    temp = 0
    print(f"==> Temperature: {temp}C")

def display_clock(verbose=False):
    if verbose: print("==> Updating clock")


super_loop()
event_driven_asynchronous()
event_driven_synchronous()


