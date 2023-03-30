if not os.path.isfile("users.txt"):
        with open("users.txt", "w") as f:
            f.write("username,password,balance,product_ID\n")
    with open("users.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n").split(",")
            if username == line[0]:
                print("Username already exists! Please try again.\n")
                return False