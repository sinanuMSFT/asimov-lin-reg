# input values for three laptops: processor speed, size of harddrive (TB), weight, size of memory (GB), processor generation
X = [
        [2.5, 0.5,  1.8,  8, 2], # Mid-range laptop
        [3.2, 1,    2.2, 16, 3], # High-end laptop
        [1.8, 0.25, 3,  4, 1]  # Budget laptop
    ]
c = [200, 50, -200, 40, 300]   # coefficient values

def predict(X, c):
    for x in X:
        price = 0
        for i in range(len(x)):
            price += x[i] * c[i]         
        print(price)

predict(X, c)
