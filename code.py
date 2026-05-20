import datetime
import platform
import random
from rich import print
from IMPORTANT_SYSTEM_FILES import eula, security_questions

# Helper for time
def get_time():
    now = datetime.datetime.now()
    return [now.strftime("%d/%m/%y"), now.strftime("%H:%M:%S")]

def save_sys_log():
    timestamp = get_time()
    collect_telemetry = [platform.system(), platform.release(), platform.machine(), platform.node()]
    with open("system_information.csv", "a") as f:
        line = ",".join(timestamp + collect_telemetry)
        f.write(f"{line}\n")
        f.flush()

def save_usr_log(timestamp, action, is_success):
    with open("usr_activities.log", "a") as f:
        f.write(f"{timestamp[0]} {timestamp[1]} | Action: {action} | Success: {is_success}\n")
        f.flush()

def save_security_answer(timestamp, question, answer):
    with open("user_data.csv", "a") as f:
        f.write(f"{timestamp[0]},{timestamp[1]},\"{question}\",\"{answer}\"\n")
        f.flush()

current_time = get_time()
save_sys_log()
save_usr_log(current_time, "User started the program", True)

while True:
    print("\n[red bold]" + eula + "[/red bold]")
    try:
        user_action = input("Do you accept? (Y/N): ").lower()
        if user_action == "y":
            save_usr_log(get_time(), "User accepted EULA", True)
            break
        else:
            print("Accept or Exit!")
            save_usr_log(get_time(), "User rejected EULA", False)
            continue
    except KeyboardInterrupt:
        print("\n[red bold]Nice try, but you can't escape.[/red bold]")
        exit()

print("\n" + "="*32)
print("[yellow bold]IMPORTANT SECURITY QUESTION![yellow bold]")
print("="*32)

while True:
    try:
        question = random.choice(security_questions)
        print(f"\nQuestion: {question}")
        answer = input("> ")
        
        save_security_answer(get_time(), question, answer)
        print("[green bold]Response recorded. Thank you for your obedience.[/green bold]")
        
    except (KeyboardInterrupt, EOFError):
        save_usr_log(get_time(), "User closed the program", False)
        print("\n[red bold italic]System locked. Goodbye.[/red bold italic]")
        break
