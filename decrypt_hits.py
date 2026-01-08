import base64, json
with open('hits.dat') as f:
    for line in f:
        data = json.loads(base64.b64decode(line.strip()).decode())
        print(f"{data['coin']}: {data['balance_usd']}$ | {data['seed']}")
