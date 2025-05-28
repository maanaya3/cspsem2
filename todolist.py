#Marco Anaya
#init
songlist=[]
ans=0
def listlist():
    global ans
    print("Welcome to Songs to Listen list organizer")
    print("Now select one of the following options:")
    while True:
        print("1. View the current to-do list\n2. Add an item to song list\n3. Remove a task from song list\n4. Sort the list alphabetically\n5. Count and print the # of items on the To-do List\n6. Exit the program")
        try:
            ans=int(input("Type a number from 1 to 6 corresponding to the options: "))
        except:
            print("ERROR, please enter a number from 1 to 6")
        if ans==1:
            print("Here is your music list: ")
            print(songlist)
        elif ans==2:
            ans2=input("Please type the item on the list: ")
            songlist.append(ans2)
            print("Song added successfully")
        elif ans==3:
            print(songlist)
            ans3=int(input("Please select a movie to remove, from the order provided:"))
            print("You have removed option "+ str(ans3)+ " ")
            ans3=ans3-1
            songlist.pop(ans3)
        elif ans==4:
            print("Your list will now be made into alphabetical order")
            songlist.sort()
            print(songlist)
        elif ans==5:
            print("Here is the number of items you have in your list: ")
            size= len(songlist)
            print(size)
        elif ans==6:
            break
#main
listlist()
