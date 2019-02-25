
def what_vids():
    vids = []
    print("Enter the file names of the videos you want to process. Enter 'done' when you're finished")
    user_input = ""
    while user_input != "done":
        user_input = input()
        vids.append(user_input)
    return vids[0:-1]

if __name__ == "__main__":
    test = what_vids()
    print(test)
