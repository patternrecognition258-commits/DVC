import pandas as pd 

data = {
    "name":  ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ian", "Jack"],
    "age":   [25, 30, 22, 28, 26, 24, 27, 23, 29, 21],
    "score": [85, 78, 92, 88, 95, 80, 89, 76, 84, 90]
}

df = pd.DataFrame(data)

df.to_csv('data/sample.csv')