from colorama import init, Fore, Back, Style

init()

def Menu():
  menu = Fore.LIGHTCYAN_EX + '''     
/\ \                            /\ \__              /\ \        
\ \ \/'\     ___     ___   _____\ \ ,_\    __    ___\ \ \___    
 \ \ , <    / __`\  / __`\/\ '__`\ \ \/  /'__`\ /'___\ \  _ `\  
  \ \ \\`\ /\ \L\ \/\ \L\ \ \ \L\ \ \ \_/\  __//\ \__/\ \ \ \ \ 
   \ \_\ \_\ \____/\ \____/\ \ ,__/\ \__\ \____\ \____\\ \_\ \_\
    \/_/\/_/\/___/  \/___/  \ \ \/  \/__/\/____/\/____/ \/_/\/_/
                           '''
  msg =  Fore.RED + '\n \nBot started'
  print(menu, msg)

