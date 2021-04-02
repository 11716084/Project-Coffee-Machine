import math

water = 400
milk = 540
beans = 120
cups = 9
dollars = 550

print(f"""The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{dollars} of money""")


def function_buy():
    g = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    if g == '1':
        print(f"""The coffee machine has:
{water - 250} of water
{milk} of milk
{beans - 16} of coffee beans
{cups - 1} of disposable cups
{dollars + 4} of money""")
    if g == '2':
        print(f"""The coffee machine has:
{water - 350} of water
{milk - 75} of milk
{beans - 20} of coffee beans
{cups - 1} of disposable cups
{dollars + 7} of money""")
    if g == '3':
        print(f"""The coffee machine has:
{water-200} of water
{milk -100} of milk
{beans-12} of coffee beans
{cups - 1} of disposable cups
{dollars + 6} of money""")
def function_take():
    print(f"I gave you ${dollars}\n")
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{0} of money""")

def function_fill():
    W = input("Write how many ml of water do you want to add:\n")
    M = input("Write how many ml of milk do you want to add:\n")
    B = input("Write how many grams of coffee beans do you want to add:\n")
    C = input("Write how many disposable cups of coffee do you want to add:\n")
    print(f"""The coffee machine has:,
{int(water) + int(W)} of water
{int(milk) + int(M)} of milk
{int(beans) + int(B)} of coffee beans
{int(cups) + int(C)} of disposable cups
{int(dollars)} of money""")

user = input("\nWrite action (buy, fill, take)\n")
if user == 'buy':
    function_buy()
if user == 'fill':
    function_fill()
if user == 'take':
    function_take()
