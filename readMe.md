Notes:
	- Admin credentials :(devadmin, 12345)
	- Used sqlite3
 	- Have used viewset instead of views and in built mixins for list, update and delete objects for redundancy. Also used routers for registering

 	- The following are the endpoints:
 		1) List: GET /peoples/
 		2) Retrieve a single instance : GET /peoples/<id>/
 		3) Update: PUT /peoples/<id>/
 		4) Delete: DELETE /peoples/<id>/