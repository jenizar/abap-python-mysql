# abap python mysql
 SAP ABAP post data to MySQL database using Python
 
![alt text](https://github.com/jenizar/abap-python-mysql/blob/master/Screenshot.PNG)

Run program :

1. xampp_start (start mysql db)

2. python app.py

Test @Postman :

POST -> Body -> raw data -> JSON (application/json)  

[{"matnr":"2485666S","maktx":"Thermostate","matkl":"N1000","ktmng":"85","peinh":"191"}]

Note:

The application has a limitation where if you want to display data in web browser then the service must be turned off then turned on again.

References:

https://wiki.scn.sap.com/wiki/display/Snippets/One+more+ABAP+to+JSON+Serializer+and+Deserializer


