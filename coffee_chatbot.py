# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  print(size)
  drink_type = get_drink_type()
  print(drink_type)

  print("alright, that's a {} {}!".format(size,drink_type))
  name = input("Can I get your name please?")
  print("Thanks {}! Your drink will be ready shortly.".format(name))


def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ').lower()
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input("what type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ").lower()
  if res == 'a':
    return "Brewed Coffee"
  elif res == 'b':
    return "Mocha"
  elif res == 'c':
    return order_latte()
    
  else:
    print_message()
    return get_drink_type()
  
def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>").lower()
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
# Call coffee_bot()!
coffee_bot()
