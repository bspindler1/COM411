print("What type of cover does the book have?")

cover_type = input()

if cover_type == "soft":
    print("Is the book perfect-bound?")
    response = input()
    if response == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

elif cover_type == "hard":
    print("Books with hard covers can be more expensive!")