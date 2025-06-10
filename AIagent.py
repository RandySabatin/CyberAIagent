import json
import requests

# Replace with your actual Airouter API key
AIR_OUTER_API_KEY = 'your_airouter_api_key'
AIR_OUTER_API_URL = 'https://api.airouter.ai/v1/chat/completions'

def read_system_events(json_file_path):
    with open(json_file_path, 'r') as file:
        events = json.load(file)
    return events

def format_prompt(events):
    prompt = (
        "You are a cybersecurity analyst AI. Given the following system events, "
        "analyze the data and identify any signs of malware or potentially malicious activity. "
        "Respond with the type of threat (if any), indicators of compromise, and reasoning.\n\n"
        f"System Events:\n{json.dumps(events, indent=2)}"
    )
    return prompt

def ask_airouter(prompt):
    headers = {
        'Authorization': f'Bearer {AIR_OUTER_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "gpt-3.5-turbo",  # or the latest supported
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(AIR_OUTER_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

def main(json_path):
    events = read_system_events(json_path)
    prompt = format_prompt(events)
    result = ask_airouter(prompt)
    print("LLM Analysis:\n", result)

if __name__ == '__main__':
    # Example JSON file: system_events.json
    main('system_events.json')
