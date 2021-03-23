# Lost & Found (Backend)

Author: Syafiq Abdillah Umarghanis
# Live Demo (Heroku)
You can access the live demo version at <br>
https://lostandfound-syafiq.herokuapp.com/ <br>
# Installation Manual
## System Requirements 
1. Python 3.8.x
2. Git 2.27.01
## Prerequisites
1. Go to certain directory or make a new one. Let's call it LNF <br> 
`mkdir LNF && cd LNF`
2. Clone this repo to to LNF <br> 
`git clone https://github.com/syafiqabdillah/lostandfound-backend.git backend`
3. Download .env file that has been sent via email
## Installation
1. Go to LNF directory 
2. Go to backend directory 
`cd backend`
3. Install virtual environment library for python if you don't have any similar library<br>
`python install virtualenv`
4. Create a new environment <br>
`virtualenv venv`
5. Enter the environment <br>
`venv\Scripts\activate` for Windows <br>
`source venv/bin/activate` for Linux & MacOS
3. Install all dependencies <br>
`pip install -r requirements.txt`
4. Copy paste .env file for backend (sent via email) to backend directory
5. Run the server <br>
`uvicorn main:app --reload`
6. Check if server is running by opening http://localhost:8000 in your browser
## Questions 
Any questions or difficulties? Don't hesitate to ask me by posting new issue in this repo or sending me emails at abdillah.syafiq@gmail.com