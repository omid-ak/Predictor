import Prediction
def menu():
    while True:
        print('Enter C to predict car price\nEnter H to predict home price\nEnter Q to quit the App\n')
        ch = input('Enter your choice : \n')
        if ch == 'C':
            print('car prediction')
            car_model = input('Enter your car model\n')
            car_year = input('Enter your car production year\n')
            car_color = input('Enter color of your car\n')
            karkard = input('How Much function counter of your car(in Kilo meter) ?\n')
            print('Predicted price for your car is {} Rials'.format(Prediction.car_predicting(car_model, car_year, car_color, karkard)))

        elif ch == 'H':
            print('Home prediction\n')
            city = input('Enter Your City\n')
            rooms = input('How many rooms ate there in this home \n')
            meterix = input('How much meterix of this home(in meter)?\n')
            print('Predicted price of your Home is {} Rials'.format(Prediction.home_predicting(city, rooms, meterix)))
        elif ch == 'Q':
            print('Bye :)')
            break
        else:
            print('Wrong Command please Enter a correct command')

if __name__ == "__main__":
    menu()