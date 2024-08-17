### API-Practice
This project is to establish a flask API for handling ordering data. The SOLID concepts applied to the project are:
1. Single responsibility principle(SRP): each class/function is responsible for only one thing.
2. Open/close principle(OCP): each class contains similar purpose of functions. For example, the class ```ConverData``` contains any function for transforming data, so that any function other than the function ```currency()``` can be included to the class.
3. Liskov substitution principle(LSP): any function can be replaced by other function, as long as it still has same outputs. For example, the ```CheckData.currency_``` can be re-desinged to:  

    ```
    def currency_(currency: str):
        if currency == 'TWD' or currency == 'USD':
            return True
        else:
            return False
    ```


### Prepareation
The flask app can run in either local or in docker image. If using docker, steps to build and run the image are:
1. Build image:  
    ```docker build -t api-practice .```
2. Start image:
    ```docker run -id -p 8080:8080 --name api-practice api-practice```


### Test the API
There are 2 ways to test the API:
1. Run the unit test script by executing the Python command:  
    ```python3 core/unit_test.py```  
2. Enter the image and then run the testing script:  
    ```docker exec -it api-practice /bin/bash```  
    ```python3 core/unit_test.py```