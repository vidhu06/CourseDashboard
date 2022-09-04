# CourseDashboard


Undersanding and ASSUMPTIONS 

1. Our Platform is recieving data from LearnDash about the status of various couses by Employees of several Companies.
2. Our platform is storing the data.
3. Our platform has APIs along with filters to server as a source of providing data to display on a dashboard.

The APIs is created with the help of Django.

## Models/Tables 

### Person Table
#### Description - A table to store details about a person.
#### Columns 
1. user_id - Unique ID 
2. name - Name of the person
3. manager_id - Id of the manager from the same table.

### Courses Table
#### Description - To store details about a table.
#### Columns
1. course_id - Unique ID 
2. course_name - Name of the Course
3. company - Name of the company which the course belong to.
4. total_modules - Total Number of available modules in the course.

### PersonCourseActivity Table
#### Description - To store the details of Person Enrolled for a course and its progress.
#### Columns
1. id - Unique id
2. user_id - A foreign key to the Person Table
3. course_id - A foreign key to the Course Table
4. Completed_modules - No. of modules completed, this will be updated whenever we get progress details.
5. is_started - A flag to check if the person has started the course.
6. is_completed - A flag to check if the person has completed the course.
7. updated_ts - A timestamp for the update.



## API USES

CourseEnrollmentList 
API - http://127.0.0.1:8000/courses/courseEnrollment/ <br>
Description - It provides details of all the Users, their Courses along with the progress

Filters 

1. CourseEnrollmentList by users (User Based View) <br>
API - http://127.0.0.1:8000/courses/courseEnrollment/?user_id=1 <br>
Description - When a User wants to see the progress of courses, this API will provide the list of all courses of the user. <br>

2. CourseEnrollmentList under a manager <br>
API - http://127.0.0.1:8000/courses/courseEnrollment/?user_id__manager_id=1 <br>
Description - When a manager wants to see the progress of all the persons under him, the API will provide the response.

3. CourseEnrollmentList by Company <br>
API - http://127.0.0.1:8000/courses/courseEnrollment/?course_id__company=Brillio <br>
Description - To get the list of all the Courses

4. CourseEnrollmentList by Course <br>
API - http://127.0.0.1:8000/courses/courseEnrollment/?course_id__course_name=CourseA <br>
Description - To get the list of Users and Progress for a particular Course.

Please find Sample Response of each of the API in the document file.
https://github.com/vidhu06/CourseDashboard/blob/main/Document.txt

