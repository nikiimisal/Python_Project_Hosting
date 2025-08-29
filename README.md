# Python_Project_Hosting














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
   
