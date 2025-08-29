# Python_Project_Hosting

<h1> Prerequisites</h1>
Before starting this journey, I ensured I had:

• An AWS EC2 instance running 
• Basic knowledge of Linux commands
• A MEAN stack application ready for deployment

>>Personal Note: Setting up the EC2 instance was straightforward, but I recommend thoroughly understanding AWS security groups and network settings before proceeding.<br>
Ensure that ports 5000 and 27017 are open in the security group.

<h1>Setteping infrastructure of project</h1>

Step-by-Step Explanation

1. Check Python Version if Python software not avalible download it..
   
       python3 -V
   <br>
   
       sudo yum update
       sudo yum install python3 python3-pip
This verifies which version of Python 3 is installed, ensuring compatibility with your application.

2. Install Python Tools
   
        sudo yum install python3-pip -y
        sudo yum install python3-virtualenv -y
These commands install pip (for package management) and virtualenv (for creating isolated Python environments).
>>PIP:pip is a python package manager (a recursive acronym for “Pip Installs Packages”) is the standard package installer for Python, designed to help you easily install, manage, and organize libraries that aren't part of the standard library.<br>
>> Virtualenv : In two separate directories, virtual environments keep projects clean and organized. As a result, there are no interdependencies between the projects.

• Isolates project dependencies
• Prevents version clashes and system conflicts
• Enables consistent, reproducible setups across development environments

4. Set Up Project Directory












python3 -V
sudo yum install python3-pip -y
sudo yum install python3-virtualenv -y
mkdir pythonapp
cd pythonapp/
source myenv/bin/activate
python3 -m venv myenv
ls
ls myenv
 sudo nano requirements.txt
 sudo nano app.py
  pip install -r requirements.txt
  python3 app.py

  Until now, we had been running it in the foreground; from now on, it will run in the background

  gunicorn --bind 0.0.0.0:5000 app:app --daemon

  sudo yum install nginx
  sudo service nginx start
   sudo nano /etc/nginx/nginx.conf
   sudo service nginx reload

   mkdir templates
   cd templates
   sudo nano form.html
   cd ..
   python3 app.py
   add app2.py or remove app.py and added new app.py
   python3 app.py
   pip3 install mysql-connector-python
   sudo yum install mariadb105-server
   sudo service mariadb start
   sudo mysql -u root -p

   create database table
   use table
   
