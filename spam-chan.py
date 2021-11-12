# Don't forget to pip install
import pyautogui
import pyperclip
import time

# Create vars
text = ""
amount = ""
withDiscordTag = False

# init
def init():
    # Set text and amount of spam
    global text 
    global amount 

    text = input("What word would you like me the spam senpai? ")
    amount = input("How many times? ")

    # Discord tag check
    check_using_discord_tag()

# Check if u want to use discord @
def check_using_discord_tag():
    # Globals
    global withDiscordTag

    withDiscordTag = input("Wanna use a discord tag? Answer with True or False! ").capitalize()

    print(withDiscordTag)

    if withDiscordTag == str(True):
        withDiscordTag = True
        start_the_spammening()
    elif withDiscordTag == str(False):
        withDiscordTag = False
        start_the_spammening()
    else:
        print("Answer with True or False!")
        check_using_discord_tag()

# Function for spamming
def start_the_spammening():
    # Globals
    global withDiscordTag

    # Time to switch to the input u want to spam
    print("starting spammening pls switch to the input u want to spam...")

    # Sleep with countdown
    for i in range(5, 0, -1):
        time.sleep(1)
        print(i)

    # Copy text
    pyperclip.copy(text)

    # Loop for the spamming UwU
    for x in range(int(amount)):
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")

        if withDiscordTag:
            time.sleep(0.2)
            pyautogui.press("enter")

        time.sleep(0.5)
    
    print("Successfully annoyed someone!")

# Starting spam-chan...
print("starting spam-chan...")
init()