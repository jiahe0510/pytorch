import json

if __name__ == '__main__':
    with open("openchat.train.text.json") as f:
        data = json.load(f)
        for line in data:
            print(line)
