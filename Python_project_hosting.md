# Python_Project_Hosting

<h1> Prerequisites</h1>
Before starting this journey, I ensured I had :<br>
<br>
• An AWS EC2 instance running <br>
• Basic knowledge of Linux commands<br>
• A MEAN stack application ready for deployment<br>

>>Personal Note: Setting up the EC2 instance was straightforward, but I recommend thoroughly understanding AWS security groups and network settings before proceeding.<br>
Ensure that reliable ports open in the security group.

<h1>Setupping infrastructure of project</h1>

Step-by-Step Explanation<br>

1. Check Python Version....if Python software not avalible download it..
   
       python3 -V
   <br>
   
       sudo yum update
       sudo yum install python3 python3-pip
This verifies which version of Python 3 is installed, ensuring compatibility with your application.<br>

2. Install Python Tools
   
        sudo yum install python3-pip -y
        sudo yum install python3-virtualenv -y
These commands install pip (for package management) and virtualenv (for creating isolated Python environments).
>>PIP : pip is a python package manager (a recursive acronym for “Pip Installs Packages”) is the standard package installer for Python, designed to help you easily install, manage, and organize libraries that aren't part of the standard library.<br>
>> Virtualenv : In two separate directories, virtual environments keep projects clean and organized. As a result, there are no interdependencies between the projects.<br>
• Isolates project dependencies<br>
• Prevents version clashes and system conflicts<br>
• Enables consistent, reproducible setups across development environments<br>

3. Set Up Project Directory

       mkdir pythonapp
       cd pythonapp/
Create and enter the pythonapp directory where your project will reside.<br>

4. Create & Activate Virtual Environment

       python3 -m venv myenv
       source myenv/bin/activate
   First, the virtual environment myenv is created, then activated—isolating your project's dependencies.<br>

5. Check Directory Contents

       ls
       ls myenv
   List current files and inspect contents of the myenv directory to confirm correct creation.<br>

6. Prepare Project Files

       sudo nano requirements.txt
       sudo nano app.py
   Create or edit:<br>

• requirements.txt — to list required Python packages.<br>
• app.py — your main application code.<br>
• I have provided the code for both of these files in the repository— view them there and copy-paste as needed.<br>

7. Install Dependencies & Run App
   
       pip install -r requirements.txt
       python3 app.py
   Install dependencies and run the application directly—in the current terminal (i.e., in the foreground).
8. Transition from Foreground to Background <br>  
         Until now, we had been running it in the foreground; from now on, it will run in the background.<br>
         or<br>
         This highlights that previously the application was started in the active terminal, but now you'll shift it to run independently of the terminal.<br>

9. Run Gunicorn as a Background Daemon
    
       gunicorn --bind 0.0.0.0:5000 app:app --daemon



<h1>From here onward, let's proceed to host a basic project</h1>

Nginx Installation & Configuration :

     sudo yum install nginx
     sudo service nginx start
     sudo systemctl enable nginx

   If you want to proxy_pass port 5000 to 80
   >>I prefer this setup because the Python development server running on port 5000 occasionally fails under heavy request loads

     sudo nano /etc/nginx/nginx.conf
 <br>
 
         location / {
         proxy_pass http://localhost:8000;
         }
   <br>      
    
     sudo service nginx reload

 Project Structure Setup :
 
      mkdir templates
      cd templates
      sudo nano forms.html
• I have provided the code file in the repository— view them there and copy-paste as needed.<br><br>
Setting Up MariaDB :<br><br>

To manage your application's data, you installed MariaDB, a popular relational database management system:

    sudo yum install mariadb105-server


After installation, you started the MariaDB service:

    sudo service mariadb start
You then logged into the MariaDB shell:

    sudo mysql -u root -p
    CREATE DATABASE nikhil;
    
  Back to the folder where your app.py file avalible
  The file should be linked to the appropriate HTML folder

        your-app/
        ├── app.py
        ├── templates
        │   └── form.html
<br>
  
      cd ..
      python3 app.py

. Deploying the Flask Application with Gunicorn and Nginx<br><br>

To deploy your Flask application in a production environment, you utilized Gunicorn, a Python WSGI HTTP server:

      pip3 install gunicorn
You then started the Gunicorn server:

    gunicorn --bind 0.0.0.0:5000 app:app --daemon


