import json

def run_moore(data):
    states = data['states']
    transitions = data['transitions']
    initial_state = data['initial_state']
    test_string = data['test_string']
    
    current_state = initial_state
    path = [current_state]
    output = [states[current_state]]
    
    for symbol in test_string:
        current_state = transitions[current_state][symbol]
        path.append(current_state)
        output.append(states[current_state])

    print("Input:", test_string)
    print("Path:", " → ".join(path))
    print("Output:", "".join(output))

# Ubah bila diperlukan, tergantung dari direktori mana kita menjalankan kode python ini
file_path = "src/input.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)
        run_moore(data)
except FileNotFoundError:
    print(f"Error: File '{file_path}' tidak ditemukan.")
except json.JSONDecodeError as e:
    print("Error: Format JSON tidak valid.")