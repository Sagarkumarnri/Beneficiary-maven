for python -install python 3  and pip   

run fine_tune.py for training the model ---command:python fine_tune.py4

go to install all the python dependency in terminal using pip
 
after model is  trained run app command: python app.py

you will see the  FAST api server running on local host 8000

now run your spring boot app and in post man curl this url




curl --location 'http://localhost:8080/api/similarity' \
--header 'Content-Type: application/json' \
--data '{
  "name1": "jcob",
  "name2": "jay cob"
}'

pip install locust


 python -m locust -f apiLoadTesting.py --host=http://127.0.0.1:8000 
