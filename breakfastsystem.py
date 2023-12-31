# -*- coding: utf-8 -*-
"""
"""

import ipywidgets as widgets
from IPython.display import display, Image
import csv

subtotal_output = widgets.Output()
total_output = widgets.Output()

from typing_extensions import clear_overloads
#字典
meal_D={'主餐':0,
    '義大利麵':100,
    '脆皮烤鴨':120,
    '肉肉咖哩飯':150}
dessert_D={'甜點':0,
    '鬆餅':70,
    '杯子蛋糕':80,
    '草莓馬卡龍':90}
drink_D={'飲料':0,
    '葡萄柚汁':50,
    '綜合水果汁':55,
    '紅莓藍莓的互利共生':60}
print('\033[1m菜單\t主餐\t\t\t甜點\t\t\t\t飲料\033[0m')
print('\t義大利麵:100\t\t鬆餅:　70\t\t\t葡萄柚汁:50')
print('\t脆皮烤鴨:120\t\t杯子蛋糕:80\t\t\t綜合水果汁:55')
print('\t肉肉咖哩飯:150\t\t草莓馬卡龍:　90\t\t\t紅莓藍莓的互利共生:60')
#袋子
bag = widgets.Checkbox(
    value = False,
    #True
    description = "是否需要購物袋(需+1元)",
    disabled = False)
#數量
meal_number= widgets.Dropdown(
    options=['0','1','2','3','4','5','6','7','8','9','10'],
    value='0',
    description='主餐數量：',
    disabled=False,)
drink_number= widgets.Dropdown(
    options=['0','1','2','3','4','5','6','7','8','9','10'],
    value='0',
    description='飲料數量：',
    disabled=False,)
dessert_number= widgets.Dropdown(
    options=['0','1','2','3','4','5','6','7','8','9','10'],
    value='0',
    description='點心數量：',
    disabled=False,)
#下拉
meal = widgets.Dropdown(
    options=['義大利麵', '脆皮烤鴨', '肉肉咖哩飯'],
    value='義大利麵',
    description='選擇主餐:')

meal_image = widgets.Image(width=250)

bag = widgets.Checkbox(
    value = False,
    #True
    description = "是否需要購物袋(需+1元)",
    disabled = False)

def meal_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        meal_image.value = open(change['new']+'.jpg', 'rb').read()
drink = widgets.Dropdown(
    options=['葡萄柚汁', '綜合水果汁', '紅莓藍莓的互利共生'],
    value='葡萄柚汁',
    description='選擇飲料:')
drink_image = widgets.Image(width=250)
def drink_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        drink_image.value = open(change['new']+'.jpg', 'rb').read()
dessert = widgets.Dropdown(
    options=['杯子蛋糕','鬆餅','草莓馬卡龍'],
    value='杯子蛋糕',
    description='選擇甜點:')
dessert_image = widgets.Image(width=250)
def dessert_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        dessert_image.value = open(change['new']+'.jpg', 'rb').read()

order= widgets.VBox([widgets.HBox([meal_image,dessert_image,drink_image]),
          widgets.HBox([meal,meal_number]),
          widgets.HBox([dessert,drink_number]),
          widgets.HBox([drink,dessert_number]),
          widgets.HBox([bag])])

meal.observe(meal_change)
dessert.observe(dessert_change)
drink.observe(drink_change)

display(order)

#結帳按鈕
check_number=0
def button_click(_):
    if bag.value==True:
      bag1=1
    else:
      bag1=0
    fee=bag1+int(meal_D[meal.value])*int(meal_number.value)+int(drink_D[drink.value])*int(drink_number.value)+int(dessert_D[dessert.value])*int(dessert_number.value)
    global check_number
    check_number+=1

    print("您的訂單編號:",check_number,'\n'
      ,"主餐品項:", meal.value,'共', meal_number.value ,"份\t",int(meal_D[meal.value])*int(meal_number.value),"元\n"
      ,"飲料品項:", drink.value,'共', drink_number.value,"份\t",int(drink_D[drink.value])*int(drink_number.value),"元\n"
      ,"甜點品項:", dessert.value,'共', dessert_number.value,"份\t",int(dessert_D[dessert.value])*int(dessert_number.value),"元\n"
      ,"購物袋:",str(bag1),"份共",str(bag1),"元\n"
      ,"點餐金額:", fee,'元\n')

    checkout=["您的訂單編號:",str(check_number),'\n'
      ,"主餐品項:", str(meal.value),'共', str(meal_number.value) ,"份\t",str(int(meal_D[meal.value])*int(meal_number.value)),"元\n"
      ,"飲料品項:", str(drink.value),'共', str(drink_number.value),"份\t",str(int(drink_D[drink.value])*int(drink_number.value)),"元\n"
      ,"甜點品項:", str(dessert.value),'共', str(dessert_number.value),"份\t",str(int(dessert_D[dessert.value])*int(dessert_number.value)),"元\n"
      ,"購物袋:",str(bag1),"份共",str(bag1),"元\n"
      ,"點餐金額:", str(fee),'元\n\n']

    file = open("checkout.txt","a")
    file.writelines(checkout)
    file.close()

button = widgets.Button(description="結帳！")
button.on_click(button_click)
display(button)
