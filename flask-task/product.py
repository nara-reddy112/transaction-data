import csv

def get_productName(productId):
    # Open file
    with open('ProductReference.csv') as file_obj:
        
        # Create reader object by passing the file
        # object to reader method
        reader_obj = csv.reader(file_obj)
        # import pdb;pdb.set_trace()
        # Iterate over each row in the csv
        # file using reader object
        for row in reader_obj:
            if row[0] == productId:
            	productname = row[1]
            	return productname

def get_cityName(productId):
    # Open file
    with open('ProductReference.csv') as file_obj:
        
        # Create reader object by passing the file
        # object to reader method
        reader_obj = csv.reader(file_obj)
        # import pdb;pdb.set_trace()
        # Iterate over each row in the csv
        # file using reader object
        for row in reader_obj:
            if row[0] == productId:
            	cityname = row[2]
            	return cityname    