choice=int(input("1.PDF\n2.JPG\n3.PNG\n4.MP3\n5.MP4\nEnter extension:-"))
match choice:
    case 1:
        print("Document")
    case 2:
        print("Image")
    case 3:
        print("Image")
    case 4:
        print("Audio")
    case 4:
        print("Video")
    case _:
        print("Unknown File Type")