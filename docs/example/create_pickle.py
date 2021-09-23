import pickle

data = {
    '2': 0,
    '3': 50,
    '3.5': 60,
    '4': 70,
    '4.5': 80,
    '5': 90
}

with open('model.pkl', 'wb') as f:
    pickle.dump(data, f)