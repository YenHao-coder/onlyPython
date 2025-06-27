from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 咖啡機流程:
# 1.詢問顧客訂單
# 2.查看原料數量並原料回傳是否能製作
# 3.計算投入的硬幣金額並回傳支付金
# 4.查看支付金是否負擔價格，計算支付後零錢金額，並回傳交易成功
# 5.咖啡製作並扣除使用的原料數量

clerk = Menu() # 接收訂單與傳達的服務員
casher = MoneyMachine() # 計算支付與統計收入的會計
barista = CoffeeMaker() # 製作咖啡與計算原料的廚師
power = True
while power:
    orders = input(f"What would you like? : ({clerk.get_items()})? ")
    if orders == "off":
        power =False
    elif orders == "report":
        barista.report()
        casher.report()
    else:
        drink = clerk.find_drink(orders)
        if barista.is_resource_sufficient(drink):
            price = drink.cost
            if casher.make_payment(price):
                barista.make_coffee(drink)

