# US Civics 100 Web App

## Overview

The US Civics 100 Web App is an educational tool designed to help individuals prepare for the US citizenship exam. 

This web app provides access to the 100 civics questions and answers required for the exam, along with additional features to enhance the learning experience.

![](/us-civics-readme.png)

My web app has been deployed on render.com using free web service.

You can access my web app at: [https://us-civics-100.onrender.com/](https://us-civics-100.onrender.com/) 

Note from render.com: 

Render spins down a Free web service that goes 15 minutes without receiving inbound traffic. Render spins the service back up whenever it next receives a request to process.

Spinning up a service takes a few seconds, which causes a noticeable delay for incoming requests until the service is back up and running. For example, a browser page load will hang momentarily

---

## Features
. Learning Mode: Access the 100 civics questions and answers to study and improve your knowledge.

. Quiz Test: Take a quiz test to assess your readiness for the US citizenship exam. Score greater than 6 to pass.

. User Authentication: Create an account and log in to access the quiz test feature.

. Future Enhancements: I have plans to add more features, including a search function for questions, instructions on how to apply for US citizenship, and a "what means" feature to explain key terms asked during the interview.

## Getting Started

### Requirement
. Python (version 3.8.13)

. Flask

. React

### Installation
1. Fork and clone this repository: 
[https://github.com/nnpk1007/phase-5-project-us-civics-100](https://github.com/nnpk1007/phase-5-project-us-civics-100)
and change directory into this folder.

2. Create virtual enviroment for this project. 
```console
pipenv shell
```

3. Install dependencies:
```console
pip install -r requirements.txt
```

4. Open VSCode:
```console
code .
```
5. Create a .env file in the server directory and set your environment variables:
```console
SQLALCHEMY_DATABASE_URI=sqlite:///app.db
SECRET_KEY = <create your owm secret key>
```

6. Open the terminal in VSCode, seed your database and run the server:
```console
cd server
python seed.py
python app.py
```
Your server is now on [http://localhost:5555](http://localhost:5555`)

7. Open another terminal in VSCode, from root directory, run:
```console
cd client
npm install
npm start
```
Your React app is now on [http://localhost:3000](http://localhost:3000)

## License
This project is licensed under the MIT License.

## Acknowledgments
The USCIS for providing the 100 civics questions and answers.

