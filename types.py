data = [
    100,                
    25.5,               
    "Lighter",                   
    [1, 2, 3],          
    (10, 20),           
    {"a": 1},           
]

for item in data:
    print(item, "->", type(item))
    