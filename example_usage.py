from client import V2FunCharacterAnimatorClient
client = V2FunCharacterAnimatorClient()
print(client.animate_character([{"x": 100, "y": 200, "joint": "neck"}]))