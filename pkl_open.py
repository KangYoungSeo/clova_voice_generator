import pickle

with open('./test7.pkl', "rb") as f:
    data = pickle.load(f)
    print(data)
