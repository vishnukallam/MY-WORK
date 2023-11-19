import random
rock = '''(""""")
        (         )
      (             )
      (             )
       (           )
        (         )
          (""""")'''
paper = '''______________
          |              |
          |              |
          |              |
          |              |
          |              |
          ^^^^^^^^^^^^^^^'''
scissors  ='''
              |           |
               |         |
                |       |
                 |     |
                  |   | 
                   | |
                    | '''
shapes=[rock,paper,scissors]
user = int(input('enter choice\n0.Rock\n1.paper\n2.scissors\n'))
print(f"the user's choice is{user}\n  \t {shapes[user]}")
if user <0 and user >=3:
    print('the number you entered if invalid')
else:
    computer = random.randint(0,2)
    print(f'the computer choice is{computer}\n  \t {shapes[computer]}')
    if user == computer:
        print('The game is tie')
    elif computer == 0 and user == 2:
        print("YOU LOSE")
    elif computer == 2 and user == 0:
        print("YOU WON")
    elif computer > user:
        print('YOU lose')
    else:
        print('YOU WON')