 <h1>Prerequisites</h1>
Before starting this journey, I ensured I had:

• An AWS EC2 instance running 
• Basic knowledge of Linux commands
• A Python Project ready for deployment

>>Personal Note: Setting up the EC2 instance was straightforward, but I recommend thoroughly understanding AWS security groups and network settings before proceeding.
Ensure that ports 5000 or 8501 are open in the security group.

<h1>Install the software related(necessary) to your project … just as listed below</h1>

  >>If you want to install and use Nginx with a proxy_pass, that’s a great approach. I’ve created these notes just for practice. So if you’d like to use that method, you can proceed with adding this process...i.e adding MariaDB, etc.
   
    sudo yum update
 Make shure install git,Because we have go to clone the repo.
 
    sudo yum install git -y
   <br>
   
    git clone https://github.com/Spidy20/InNews.git
    ls
check python avabile or not

    python3 -V
  if not download it
   
     pip3 -V
  if not download it
  
     sudo yum install python3-pip -y
Now we have access the pip

    python3 -m pip

Right know we have to install all requriments to this project Repo.

    cd InNews/
    python3 -m pip install -r requriments.txt
<br>

    python3 -m streamlit run App.py
 copy the external url and pest in browser 

If you want the website to keep running even after closing the Linux (or PowerShell) session..But you must keep the server instance running.

     cd InNews/
     nohup python3 -m streamlit  run App.py

   if you want to stop this backgroung process 
     login instance
     
     sudo ps -ef

  Look there python3 -m streamlit  run App.py
  Select the perticullar process id section(PID) & kill it

    Kill 123(PID)
  
  
   <h1>I followed the steps based on a video reference… but these processes may change in the future… so stay up to date.😊</h1>

     


