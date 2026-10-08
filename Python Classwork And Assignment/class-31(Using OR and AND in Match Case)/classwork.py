service_type=int(input("Choose The Following Options:-\n1.Bookings & Reservations\n2.Baggage & Claims\n3.Frequent Flyer Program \nEnter Your Response:-"))

match service_type:
    case 1:
        action_type=int(input("Choose the Following action type:-\n1.To Book a new flight\n2.To Cancel an existing Flight\n3.To Return to booking main menu\nEnter Your Response:-"))
        match action_type:
            case 1:
                print("The details of new flights are as follows:-\n.........")
            case 2:
                print("Your existing Flight is Cancelled")
            case _:
                print("You are Redirecting to Main Menu")
    case 2:
        action_type=int(input("Choose the action type:-\n2.To Track a lost bag\n2.To File a damage claim\n3.To Transfer directly to a baggage agent\nEnter Your Response:-"))
        match action_type:
            case 1:
                print("Tracking Your Bag Location")
            case 2:
                print("Filing Your damage claim")
            case _:
                print("You Are Transferred directly to a baggage agent.\nPlease Wait .......")
    case 3:
        action_type=int(input("Choose the action type:-\n1.Check mileage balance\n2.Go back to the main greeting\nEnter Your Response:-"))
        match action_type:
            case 1:
                print("Fetching your current frequent flyer mileage balance...")
            case _:
                print(" Go back to the main greeting")
    case _:
        print("Disconnect the call with an 'Invalid Selection' message")