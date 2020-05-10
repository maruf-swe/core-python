command = ""
started = False
while True:
    command = input(">").lower()
    if command == 'help':
        print("""
  Start - Start to the car"
  Stop - Stop to the car"
  Quit - Quit to the car
        """)
    elif command == 'start':
        if started:
            print("Car is already Started")
        else:
            started = True
            print("Start the car")
    elif command == 'stop':
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Stop the car")
    elif command =='quit':
        print("Quit the car")
        break
    else:
        print("I don't understand")
