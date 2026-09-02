import time
import pyautogui
import pyperclip
from google import genai
from gemini import ask_ai

# check last sender 
def is_last_message_from_sender(chat_log, sender_name="Chris"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2026] ")[-1]
    if sender_name in messages:
        return True
    return False



# Step 1: Click on the chrome icon at coordinates (655, 1058)
pyautogui.click(655, 1058)
time.sleep(2) # wait for 1 second to ensure the click is registered

while True:

    # Step 2: Drag the mouse from (648 192) to (1883 960) to select the text
    pyautogui.moveTo(680, 223)
    pyautogui.dragTo(1882, 963, duration=1.0, button='left') # Drag for 1 second

    # Step 3 : Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2) # wait for 1 second to ensure the copy command is complete.
    pyautogui.click(663, 224)

    # Step 4: Retrieve the text from the clipboard and store it in a variable.
    chat_history = pyperclip.paste()

    # Print the copied text to verify 
    print(chat_history)


    # if the message if front the specifed person only then execute the below code.
    if is_last_message_from_sender(chat_history):
        
        # prints the reponse
        reponse = ask_ai(chat_history)
        print(reponse)

        # copied the given reponse.
        pyperclip.copy(reponse)

        # Step 5 : Click at coordinates (827, 1002)
        pyautogui.click(827, 1002)
        time.sleep(2) # wait 1 second to ensure the click resgistered

        # Step 6 : Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2) # wait 1 second to ensure the click resgistered

        # Step 7: Press Enter
        pyautogui.press('enter')