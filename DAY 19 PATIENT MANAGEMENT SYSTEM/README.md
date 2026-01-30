# In the Health Care domain we are making a project 

Name :- API and a Backend for a New Customer to a doctor 

idea :- We have to make a api that stores all customer data in a json file , we can use a database but now, for small scale we are using a json file for storing the customer data , in that what we have to do we are making some endpoints and what the doctor can do he can update a existing data of a coustemer.

Example :- If the customer weight get loss then the doctor can change that and the backend can change the bmi of the coustmer.


# Objectives 

We are making this project specially for the doctor or a health care purpose so , they can analyze there customer data and make minimal use of a wrtting instead of use this application.


# Now Endpoints we are Making 

1) Create a New Patient   ( /create  )

In this the doctor can create a new patient data in a JSON format and add a new patient in the file 


2) Viewing a Patient Details  ( /view )

In this we can view any ones profile in from the JSON format 


3) Update a patient Details ( /update )

In this we can update patient details and make them update in a Backend


4) Delete the Patient Deatils with the help of a patient ID 

In this we are saying that we can delete the patient details permanently by the patient id


Note :- This is the Project Structure 


# Structure of a Complete API

# Get HTTPS Methods 

we have firstly made a home page when you hit our local host you directed to our home page and then you can hit the endpoints by changing the URL's and then 

1) Home Endpoint :- This is our first endpoint that we you can hit and in that we have to just add a ('/') slash in that url of our local host so, you can land on the same page of a home 


2) About Endpoint :- The about is our 2nd Endpoint of a our local host in that i have to add a ( /about ) in the url at the so, it can show us a what we have written on a about endpoint


3) view Endpoint  :-  If user or client hit the url by typing a ( /view ) at end of a URL then it will see all the Database in the JSON format


4) patient_id Endpoint :- If user hit this URL then it is simple to see the database of a single person data by there id itself 
Note :- But client has to hit the URL by typing a  ( patient/id )  at the end of a local host if user add this to url then it will see the patient details.
Example :- /patient/P001 
So, after the url if client type this then it will see the all details off a patient which is having a id "P001" 


5) sort Endpoint :- We have make a special endpoint for sorting purpose as per our need so, we can sort our patients on the basis of the height , weight , age and a bmi , so we can check easily our data an the most important thing is that we can order it in that i have a order input and by that we can check the data and alalize it.


# Post HTTPS Method 

Now we can add a new Patient by the post method , with the help of this method we can create new patients 


6) 