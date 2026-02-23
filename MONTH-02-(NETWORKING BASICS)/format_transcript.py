import json

try:
    with open('transcript.json', 'r', encoding='utf-16') as f:
        data = json.loads(f.read())
    
    text = " ".join([item['text'] for item in data])
    with open('transcript.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Done")
except Exception as e:
    print("Error:", e)
