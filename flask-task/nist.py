import logging
import flask
from flask import request, Response
from flask import jsonify
from product import get_productName, get_cityName
from datetime import datetime
import datetime
from datetime import timedelta, date

# try:
#     if config.mongoAuth:
#         connect(config.mongoName, host=config.mongoHost, port=config.mongoPort,
#                             username=config.mongoUsername, password=config.mongoPassword,
#                             authentication_source='admin')
#     else:
#         connect(config.mongoName, host=config.mongoHost, port=config.mongoPort)

# except Exception as e:
#     print(e)




app = flask.Flask(__name__)
app.debug = True



@app.route('/assignment/transactionSummaryByManufacturingCity/<last_n_days>', methods=['GET'])
def city_scan_ctrl(last_n_days):
    try:
        import csv
        p1amount = 0
        p2amount = 0
        p3amount = 0
        p4amount = 0        
        
        with open('Transaction_20180101101010.csv') as file_obj:
            
        #     # Create reader object by passing the file
        #     # object to reader method
            reader_obj = csv.reader(file_obj)
        #     # Iterate over each row in the csv
        #     # file using reader object
            date_time_str = datetime.date.today()
            
            actual_date = date.today() + timedelta(days=-int(last_n_days[1]))


            for row in reader_obj:
                date_split = row[3].split(" ",1)
                formats = '%Y/%m/%d'
                date_org = datetime.datetime.strptime(date_split[0], "%d/%m/%Y").strftime("%Y/%m/%d")
                datetimes = datetime.datetime.strptime(date_org, formats)
                if datetimes.date() > actual_date:

                    # if row[1] == 
                    cityName = get_cityName(row[1])
                    if cityName == 'C1':
                        transactionAmount = row[2]
                        
                        p1amount = p1amount+int(transactionAmount)
                        
                    elif cityName == 'C2':
                        transactionAmount = row[2]
                        p2amount = p2amount+int(transactionAmount)
                    elif cityName == 'C3':
                        transactionAmount = row[2]
                        p3amount = p3amount+int(transactionAmount)

                    elif cityName == 'C4':
                        transactionAmount = row[2]
                        p4amount = p4amount+int(transactionAmount)

                else:
                    pass
            
        
                
        ls = [{"CityName": "C1" , "totalAmount": p1amount},{"CityName": "C2" 
                , "totalAmount": p2amount},{"CityName": "C3" , "totalAmount": p3amount}
                ,{"CityName": "C4" , "totalAmount": p4amount}]
        data = { "summary": ls}

        return data
    except Exception as err:
        app.logger.error(err)
        return 'Bad Request', 400













@app.route('/assignment/transactionSummaryByProducts/<last_n_days>', methods=['GET'])
def trans_scan_ctrl(last_n_days):
    try:
        import csv
        
        # Open file
        
        p1amount = 0
        p2amount = 0
        p3amount = 0
        p4amount = 0        
        

        with open('Transaction_20180101101010.csv') as file_obj:
            
        #     # Create reader object by passing the file
        #     # object to reader method
            reader_obj = csv.reader(file_obj)
        #     # Iterate over each row in the csv
        #     # file using reader object
            date_time_str = datetime.date.today()
            
            actual_date = date.today() + timedelta(days=-int(last_n_days[1]))


            for row in reader_obj:
                date_split = row[3].split(" ",1)
                formats = '%Y/%m/%d'
                date_org = datetime.datetime.strptime(date_split[0], "%d/%m/%Y").strftime("%Y/%m/%d")
                datetimes = datetime.datetime.strptime(date_org, formats)
                if datetimes.date() > actual_date:
                    productName = get_productName(row[1])
                    if productName == 'P1':
                        transactionAmount = row[2]
                        
                        p1amount = p1amount+int(transactionAmount)
                        
                    elif productName == 'P2':
                        transactionAmount = row[2]
                        p2amount = p2amount+int(transactionAmount)
                    elif productName == 'P3':
                        transactionAmount = row[2]
                        p3amount = p3amount+int(transactionAmount)

                    elif productName == 'P4':
                        transactionAmount = row[2]
                        p4amount = p4amount+int(transactionAmount)
                    else: 
                        pass



                    # print("OK")
                else:
                    pass
            
        
                
        ls = [{"productName": "P1" , "totalAmount": p1amount},{"productName": "P2" 
                , "totalAmount": p2amount},{"productName": "P3" , "totalAmount": p3amount}
                ,{"productName": "P4" , "totalAmount": p4amount}]
        data = { "summary": ls}
        return data
    except Exception as err:
        app.logger.error(err)
        return 'Bad Request', 400








@app.route('/assignment/transaction/<transaction_id>', methods=['GET'])
def scan_ctrl(transaction_id):
    try:
        import csv
        
        # Open file
        with open('Transaction_20180101101010.csv') as file_obj:
            
            # Create reader object by passing the file
            # object to reader method
            reader_obj = csv.reader(file_obj)
            # Iterate over each row in the csv
            # file using reader object
            for row in reader_obj:
                
                if row[0] == transaction_id[1]:                
                    productName = get_productName(row[1])
                    data: dict = {"transactionId": row[0], "productName": productName, "transactionAmount": row[2], "transactionDatetime": row[3]}
                    return data
                    




        
        return data
    except Exception as err:
        app.logger.error(err)
        return 'Bad Request', 400



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

