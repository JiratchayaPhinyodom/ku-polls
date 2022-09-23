# ku-polls
When application for polls and survey at ku

## Online Polls for Kasetsart University

An application for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/),
with additional functionality.

This application is part of the [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

## How to Install and Run

1. Clone this project repository to your machine.<br>
  ```
  git clone https://github.com/JiratchayaPhinyodom/ku-polls.git
  ```

2. Get into the directory of this repository.<br>
  ```
  cd ku-polls
  ```

3. Create a virtual environment.<br>
  ```
  python -m venv venv
  ```
4. Activate the virtual environment.<br>
  ```
  . env/bin/activate
  ```
5. Install all required packages.
  ```
  pip install -r requirements.txt
  ```
6. Create ```.env``` file in ```ku-polls```
  ```
  SECRET_KEY = django-insecure-ljxm5cbi)dqu##+m!s$qdpn(u*p!i4*(ow*s@#hz(1o0&ji-bx
  DEBUG = True
  TIME_ZONE = UTC
  ```
7. Run this command to migrate the database and load the data.
  ```
  python manage.py migrate
  python manage.py loaddate data/*.json
  ```
8. Start running the server by this command.
  ```
  python manage.py runserver
  ```
  
## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home)

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Project Plan](../../wiki/Development%20Plan)
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan)
- [Iteration 2 Plan](https://github.com/JiratchayaPhinyodom/ku-polls/wiki/Iteration-2-Plan)
- [Iteration 3 Plan](https://github.com/JiratchayaPhinyodom/ku-polls/wiki/Iteration-3-Plan)
- [Iteration 4 Plan](https://github.com/JiratchayaPhinyodom/ku-polls/wiki/Iteration-4-Plan)

## Running KU POLLS
Users provided by the initial data (users.json):

| Username  | Password  |
|-----------|-----------|
|   demo1   | demopass1 |
|   demo2   | demopass2 |

