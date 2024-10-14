# Alumni_Backend 🎓👩🏼‍🎓👨🏼‍🎓🎓

## Prerequisites
- Django 5.1.1
- Python vs 3.12
- Postgresql 16.3.2

<br> 

## Installation and execution  🛠️

1. **Fork the repository**

   Open the repository [Alumni_Back](https://github.com/Angelinabassano/Alumni_Back) and click the "Fork" button located in the upper right corner of the page. It creates a copy of our repository in your own Github account.
<br>

2. **Clone your forked repository**

   Open a Git Bash terminal and clone your new repository:

```bash
# Clone this repository 
git clone https://github.com/your-github-profile/your-project-name.git

```

3. **In Pycharm, open the project's directory you've just cloned**
<br> 

4. **Create the virtual environment and then activate it**

```bash
# Create the virtual environment

python -m venv .venv

# Activate the virtual environment

.venv\Scripts\activate

#And if you need to deactivate the virtual environment

.venv\Scripts\deactivate

```
<br>

5. **Continue with the following installations**
```bash
#Install all the Python packages listed in the file requirements.txt.

pip install -r requirements.txt

At the root of your project, create a .env file and fill it with the required information. Please see our .env example.

Remember that configuration variables and cached files should be added to `.gitignore` so they are not tracked: .env

#Start the Django development server:

python manage.py runserver

#Finally, type these commands in your terminal to manage database changes in your Django project:

python manage.py makemigrations
python manage.py migrate

```
<br>

6. **Create your branch and start working!**

```bash
#Create your branch

git checkout -b feature/yourbranchname
```
<br>

## How to interact  

Users interact with the frontend website and call this API, which uses a PostgreSQL database to store data. 

[Alumni_Front](https://github.com/laradrb/Alumni_Front.git)
