device = int(input("Enter device: "))

match device:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Headlights Opened")
            case 2:
                print("Indicators Opened")
            case 3:
                print("Hazard Lights Opened")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Playing Next Track")
            case 4:
                print("Playing Previous Track")
            case _:
                print("Invalid Option")

    case 4:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Device")


