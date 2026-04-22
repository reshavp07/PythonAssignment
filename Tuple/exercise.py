#take input from user
# create empty set()
# if user is new and input 1 add him to the empty set
# if user input  2 unsubscribe

email_set = set()
user_input = int(input("Click\n1.Subscribe\n2.Unsubscribe\n Enter the number:"))

if user_input == 1:
    email_inp = input("Enter your email:")
    email_set.add(email_inp)
user_input = int(input("Click\n1.Subscribe\n2.Unsubscribe\n Enter the number:"))
if user_input == 2:
    email_inp = input("Enter your email:")
    email_set.remove(email_inp)

print(email_set)

