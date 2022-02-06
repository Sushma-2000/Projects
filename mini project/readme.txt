1.Create a virtual environment and download Django.
2.Then download all the required libraries present in the "requirements.txt" file using the below command:
	pip install -r requirements.txt
3.Change path to Django project in the command line prompt.
4.Run the following commands while launching project for the first time and everytime changes are made to the models.py file.
	i)python manage.py makemigrations
	ii)python manage.py migrate 
5.Create a superuser to access databases and tables in Django.Then run the below command:
	python manage.py runserver
6.Database tables can be viewed at "http://127.0.0.1:8000/admin".
7.Make an entry in the "Users" table because login page only accepts values present in this table and validates the user.
8.Then enter the questions to be displayed in the form in the:
	"Questions" table:For OOP subject
	"Dbms(Database and Management Systems)_questions" table:For DBMS subject
	"Os(Operating Systems)_questions" table:For OS subject
9.Enter model answers for each question entered in the tables,the questions and answers are mapped using the 'id' field in modelanswers tables
  and 'number' field in respective questions table:
	"Oops(Object Oriented and programming)_modelans" table:For OOP subject
	"Dbms_modelans" table:For DBMS subject
	"Os_modelans" table:For OS subject
(3 model answers can be entered for each question)
10.Then the actual login page followed by the test can be displayed at "http://127.0.0.1:8000/users"
11.Enter any of the email and password details stored in the 'users' table.The login page validates this and on clicking submit 'Instructions' page is displayed.
12.Then on clicking "Take Test!" ,OOP subject questions will appear.On typing answers and then clicking on submit:
Each time user answers are submitted they will stored in userans tables along with question number(id) and user email.
	"Oops_userans" table:For OOP subject
	"Dbms_userans" table:For DBMS subject
	"Os_userans" table:For OS subject
13.[Relevance score,semantic similarity score,class] of the answer will be displayed on the next page.
14.Upon clicking 'Next Section' DBMS questions will appear and then followed by OS questions.
15.Upon clicking button on the OS score page,it will be redirected to final results page.
16.On this page,User details and subject-wise relevance scores are displayed.
17.Then click on logout button,by doing so the taken_test(type=boolean) field in 'users' table will be assigned 'True' which restricts user from taking the test more than once.