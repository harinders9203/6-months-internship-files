try:
    import pswd_fun as s

    p=input("Enter your password: ")
    print(s.strength(p))
except KeyboardInterrupt:
    print("\nYou cancelled the program")