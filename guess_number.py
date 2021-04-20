def guesse_number_game():
    import random as rd
    target_number = rd.randint(1,100)
    times = 1
    while times <= 10:
        try:
            guess_number = int(input('input you guess number:'))
        except ValueError:
            print('input number type error,please input 1~100:')
            continue
        if guess_number == target_number:
            return 'you are right'
            #break
        elif guess_number > target_number: 
            if times < 10:
                print('wrong! Too big!')
            else:
                print('you guessed 10 times, also not right.The game over, the target number is : {}'.format(target_number))
        else:
            if times < 10:
                print('wrong! Too small')
            else:
                print('you guessed 10 times, also not right.The game over, the target number is : {}'.format(target_number))
        
        times = times+1

def main():
    guesse_result = guesse_number_game()
    print(guesse_result)

if __name__ == '__main__':
    main()