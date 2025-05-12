from multiprocessing import Pool


class PythonMultiProcessing:
    # Function to perform some computation
    def square(self,number):
        return number * number


x = PythonMultiProcessing()
numbers = [1, 2, 3, 4, 5]
with Pool(3) as pool:
    results = pool.map(x.square, numbers)
    print("Original numbers:", numbers)
    print("Squared numbers:", results)

