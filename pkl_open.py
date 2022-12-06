import pickle

with open('./test2.pkl', "rb") as f:
    data = pickle.load(f)
    print(data)
