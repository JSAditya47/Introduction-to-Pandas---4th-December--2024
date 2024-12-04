import pandas

myData = {
    "Brands": ["Lamborghini", "Pagani", "Ferrari", "TataNano"],
    "Top Speed": [300, 400, 275, 75],
    "Price" : ["1.3M", "1.5M", "1.75M", "0.25M"],
    "Car Type": ["SuperCar", "SuperCar", "SuperCar", "Family Car"]
   
}

dataFrame = pandas.DataFrame(myData)
print(dataFrame)
print()
print(dataFrame.loc[3])