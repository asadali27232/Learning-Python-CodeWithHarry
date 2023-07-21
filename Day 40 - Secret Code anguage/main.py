while True:
    mode = input("Code or Decode? (C/D): ").lower()

    if mode == "c":
        message = input("Enter the message: ")
        messages = message.split(" ")

        code = []
        for message in messages:
            message = message.strip()
            if len(message) <= 3:
                # reverse the message
                code.append(message[::-1])
            else:
                code.append("pq" + message[1:] + message[0] + "za")

        code = " ".join(code)
        print("The code is:", code)
    elif mode == "d":
        code = input("Enter the code: ")
        codes = code.split(" ")

        message = []
        for code in codes:
            code = code.strip()
            if len(code) <= 3:
                # Reverse back
                message.append(code[::-1])
            else:
                message.append(code[-3] + code[2:-3])

        message = " ".join(message)
        print("The message is:", message)
    else:
        print("Invalid mode!")
