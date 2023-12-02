def wifi_connection():
    print('Reboot the computer and try to connect.')
    input_user = input('Did that fix the problem: ')
    if input_user =="NO" or input_user =='no':
        print('Reboot the router and try to connect.')
        input_user = input('Did that fix the problem: ')
        if input_user =="NO" or input_user =='no':
            print('make sure cables between cables and router are plugged in firely ')
            input_user= input('Did that fix the problem: ')
            if input_user == "NO" or input_user == 'no':
                print('move router to new location and try to connect')
                input_user = input('Did that fix the problem: ')
                if input_user == "NO" or input_user == 'no':
                    print("Get a new router")
                else:
                    print('Connection has secured')
            else:
                print('Connection has secured')
        else:
            print('Connection has secured')
    else:
        print('Connection has secured')


# Call function
wifi_connection()