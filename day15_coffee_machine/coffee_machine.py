menu = {
"espresso" :{
"ingredients" :{
"water" : 50 ,
"coffee" : 18
},
"cost" : 1.5
}, 
"latte" :{
"ingredients" :{
"water" : 200 ,
"coffee" : 24 ,
"milk" : 150
},
"cost" : 2.5
},
"cappuccino" :{
"ingredients" :{
"water" : 250 ,
"coffee" : 24 ,
"milk" : 100
},
"cost" : 3.0
} 
}

resources = {
"water" : 300,
"milk" : 200,
"coffee" : 100
}
# 待辦事項4 : 查看原料是否滿足咖啡訂單。
 #1.當顧客下訂單後，查看原料是否足夠
 #2.如果需要200 mL的水而只有 100 mL的情況，應顯示 "Sorry there is not enough water."
 #3.其他原料依此類推

def check_ingredients_sufficient(order_ingredients):
    """訂單可以製作回傳 'True',原料不足回傳 'False'."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# 待辦事項5 : 處理硬幣。1.在原料充足下提醒使用者投硬幣2. "quarters" = 0.25  "dimes" = 0.10 "nickles" = 0.05 "pennies" = 0.01 3.計算投入貨幣的總金額

def calculate_coins():
    """統計硬幣數量並回傳總金額"""
    print("Please insert coins.")
    summption = int(input("How many quarters ? ")) * 0.25
    summption += int(input("How many dimes ? ")) * 0.10
    summption += int(input("How many nickles ? ")) * 0.05
    summption += int(input("How many pennies ? ")) * 0.01
    return summption

# 待辦事項6 : 查看交易是否成功。
 #1.查看使用者投入足夠的錢購買飲料，如果錢不夠則回覆“Sorry that's not enough money. Money refunded.”
 #2.購買成功後將成本消耗計入原料中，展示在下一次的 "report"內
 #3.若投入過多金額，咖啡機需找回零錢。 "Here is {changes} in change."

def transaction_successful(money_receive,drink_cost):
    """接受支付金額回傳 'True',支付金額不足回傳 'False' """
    if money_receive >= drink_cost:
        change = round(money_receive - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
# 待辦事項7 : 咖啡製作。
 #1.當原料查看與金額符合之後，應從咖啡機原料扣除並製作咖啡
 #2.當原料扣除後, 告訴使用者"“Here is your latte. Enjoy!"

def make_coffee(drink_name, order_ingredients):
    """從原物料內減去訂單所需的數量"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.Enjoy!")
        

profit = 0
power = True

while power: #2.完成前一位使用者要求後重新詢問下一位
    order = input("What would you like? (espresso/latte/cappuccino): ") # 待辦事項1 : 1.查看使用者輸入指令決定下一步執行
    if order == "off": # 待辦事項2 : 使用 " off " 關閉咖啡機。輸入" off "後關閉咖啡機
        power = False
        print("Coffee closed")
    elif order == "report": # 待辦事項3 : 列印出 "剩餘原料"。輸入  "report" 顯示目前原料的剩餘數量
        print(f"""Water : {resources["water"]} mL
Milk : {resources["milk"]} mL
Coffee : {resources["coffee"]} g
Money : $ {profit}""")
    else:
        drink = menu[order] #令 "drink" 為 "menu" 裡面的 "name"
        if check_ingredients_sufficient(drink["ingredients"]):
            payment = calculate_coins()
        if transaction_successful(payment, drink["cost"]):
            make_coffee(order, drink["ingredients"])
            


