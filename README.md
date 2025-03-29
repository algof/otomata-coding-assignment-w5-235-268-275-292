# Tugas Minggu ke-5 Otomata
| Name           | NRP        | Kelas     | Kelompok    |
| ---            | ---        | ----------| ---         |
| Algof Kristian Zega | 5025231235 | Otomata (E) | Kelompok 5 |
| Gregorius Setiadharma | 5025231268 | Otomata (E) | Kelompok 5 |
| Muhammad Davin Aulia Risky | 5025231275 | Otomata (E) | Kelompok 5 |
| Muhammad Aditya Handrian | 5025231292 | Otomata (E) | Kelompok 5 |

## Program Simulator Moore Machine

> Implement Moore Machine. Write explanation, how to use, example input and output

- Screenshot

- Source code

    ```py
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

        print("Path:", " → ".join(path))
        print("Output:", "".join(output))

    sample_input_1 = '''
    {
        "states" : {
            "q0" : "A",
            "q1" : "B",
            "q2" : "C"
        },
        "transitions" : {
            "q0" : {"0" : "q1", "1" : "q2"},
            "q1" : {"0" : "q0", "1" : "q2"},
            "q2" : {"0" : "q1", "1" : "q0"}
        },
        "initial_state" : "q0",
        "test_string" : "011001"
    }
    '''

    data = json.loads(sample_input_1)

    run_moore(data)
    ```

- Explanation