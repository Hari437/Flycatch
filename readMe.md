Notes:
	- I have excluded DB from git. Have used sqlite3 for DB.
	- Run "python manage.py migrate" for quick DB setup
	(You can run bootstrap.sh for quick setup)
	- Used sqlite3
 	- Have used viewset instead of views and in built mixins for list, update and delete objects for redundancy. Also used routers for registering

 	- The following are the endpoints:
 		1) List: GET /peoples/
 		2) Retrieve a single instance : GET /peoples/<id>/
 		3) Update: PUT /peoples/<id>/
 		4) Delete: DELETE /peoples/<id>/