# Overview
The repository contains all the lab work for the mobile security course.  

The repository contains:
  * Python files for backend
  * HTML, CSS, JS files for frontend
  * Docker to start the project

To run the application locally there are three options:  
  * run through the IDE
  * run through the terminal 
  * run through Docker

# Branches
main: Contains all project source files and Docker files for running the application.

# Building
+ IDE. Clone the repository, you can do this by using command ```git clone``` or downloading the zip archive. Install the IDE you like. For example you can use PyCharm.  
Install all the libraries you need for the application to work. See the requirements.txt file for a complete list.
+ Terminal. Clone the repository, you can do this by using command ```git clone``` or downloading the zip archive.  
The next step is to enter a command ```python app.py``` in the project folder.
+ Docker. Clone the repository, you can do this by using command ```git clone``` or downloading the zip archive.
Start with docker - You need to execute two commands (in the project folder) ```docker build -t security_lab:dev .``` and then ```docker run -p 5000:5000 security_lab:dev```.
After that you can see how the application works by clicking on the link http://127.0.0.1:5000.

# Bug
+ Lab1. At this stage, the site has one bug. When you choose to check the system status one item at a time, you need to make sure that there is no ```/refresh``` in the address bar at this point.
+ Lab2. There is a problem with creating an archive from a folder located in ```C://```. 

# Startup features in Docker
+ When you enter the file path, you are looking for the file in the docker, not on your host system.
+ System metrics - indicators of the resources that have been allocated to the container.


# Terms of Reference
1. [lab1](https://github.com/andrey1pf/Mobile-security/blob/main/Conditions/Task%201%20-%20OS%20and%20Device%20Info.pdf)
2. [lab2](https://github.com/andrey1pf/Mobile-security/blob/main/Conditions/Task%202%20-%20Work%20with%20permissions.pdf)
