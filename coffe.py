# Write your code here
class Coffee():
    start = [550, 400, 540, 120, 9]  #money, water, milk, beans, cups
    buf_start = start
    sup = ['money', 'water', 'milk', 'beans', 'cups']
    flg = True
    buy_flg = True

    def __init__(self, string):
        while self.flg:
            self.take_input()



    def print_ballance(self):
        global start
        print('The coffee machine has:\n' + str(self.start[1]) + ' of water\n' + str(self.start[2]) + ' of milk\n' + str(self.start[3]) +
              ' of coffee beans\n' + str(self.start[4]) + ' of disposable cups\n' + str(self.start[0]) + ' of money')

    def buy(self):

        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if coffee == '1':
            self.buy_flg = False
            self.esp = [0, 250, 0, 16, 1]
            self.a = [0] * 5
            for i in range(len(self.buf_start)):
                self.a[i] = self.buf_start[i] - self.esp[i]
            if self.start[1] >= 250 and self.start[3] >= 16 and self.start[4] > 0:
                self.start[0] += 4
                self.start[1] -= 250
                self.start[3] -= 16
                self.start[4] -= 1
                self.buf_start = self.start

                print('I have enough resources, making you a coffee!')
            else:

                for i in range(len(self.a)):
                    if self.a[i] < 0:
                        print('Sorry, not enough ' + self.sup[i])
                self.buf_start = self.start

        elif coffee == '2':
            self.buy_flg = False
            self.lat = [0, 350, 75, 20, 1]
            self.a = [0] * 5
            for i in range(len(self.buf_start)):
                self.a[i] = self.buf_start[i] - self.lat[i]
            if self.start[1] >= 350 and self.start[2] >= 75 and self.start[3] >= 20 and self.start[4] >= 1:
                print('I have enough resources, making you a coffee!')
                self.start[0] += 7
                self.start[1] -= 350
                self.start[2] -= 75
                self.start[3] -= 20
                self.start[4] -= 1
                self.buf_start = self.start
            else:
                for i in range(len(self.a)):
                    if self.a[i] < 0:
                        print('Sorry, not enough ' + self.sup[i])
                self.buf_start = self.start

        elif coffee == '3':
            self.buy_flg = False
            self.kap = [0, 200, 100, 12, 1]
            self.a = [0] * 5

            for i in range(len(self.buf_start)):
                self.a[i] = self.buf_start[i] - self.kap[i]
            if self.start[1] >= 200 and self.start[2] >= 100 and self.start[3] >= 12 and self.start[4] >= 1:
                self.start[0] += 6
                self.start[1] -= 200
                self.start[2] -= 100
                self.start[3] -= 12
                self.start[4] -= 1
                self.buf_start = self.start
                print('I have enough resources, making you a coffee!')
            else:

                for i in range(len(self.a)):
                    if self.a[i] < 0:
                        print('Sorry, not enough ' + self.sup[i])
                self.buf_start = self.start
        elif coffee == 'back':
            self.take_input()




    def fill(self):


        self.start[1] += int(input('Write how many ml of water do you want to add:'))
        self.start[2] += int(input('Write how many ml of milk do you want to add:'))
        self.start[3] += int(input('Write how many grams of coffee beans do you want to add:'))
        self.start[4] += int(input('Write how many disposable cups of coffee do you want to add:'))
        self.buf_start = self.start


    def take(self):

        print('I gave you $' + str(self.start[0]))
        self.start[0] = 0
        self.buf_start = self.start



    def take_input(self):
        global flg

        self.act = input('Write action (buy, fill, take, remaining, exit):')

        if self.act == 'buy':
            self.buy()
        elif self.act == 'fill':
            self.fill()
        elif self.act == 'take':
            self.take()
        elif self.act == 'remaining':
            self.print_ballance()
        elif self.act == 'exit':
             self.flg = False


Coffee('buy')