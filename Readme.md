
### Blog App

#### Overview

The Blog app allows users to create, view, and manage blog posts. Users can write articles, view all posts, view their own posts, and log out.

#### Features

1. **Logout View**: The `logout_view` allows logged-in users to log out. It clears the session and deletes the session cookie.

2. **View All Posts**: The `AllPosts` view fetches all blog posts from the database and displays them on the `articles.html` template.

3. **Write Article**: The `Write_article` view allows users to write and save new blog posts. It validates the title, description, and content before saving.

4. **Your Posts**: The `YourPosts` view displays the blog posts authored by the currently logged-in user.

#### Usage

    1. Clone the repository: `git clone https://github.com/Prashant-Bhatt-2000/PostCraft.git`
    2. Install the required packages: `pip install -r requirements.txt`
    3. Set up the database: `python manage.py makemigrations` `python manage.py migrate`
    4. Start the development server: `python manage.py runserver`
    5. Access the app at `http://127.0.0.1:8000/`

### Accounts App

#### Overview

    The Accounts app provides user registration and authentication functionalities. Users can register, log in, and log out.

#### Features

    1. **Registration**: The `Register` view allows users to register with a unique username, email, and password. It checks for existing users before creating a new one.

    2. **Login**: The `loginuser` view handles user login. It verifies the email and password and logs the user in if the credentials are correct.

    3. **Home**: The `home` view is a simple landing page for the app.

#### Usage

1. Clone the repository: `git clone https://github.com/Prashant-Bhatt-2000/PostCraft.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`
5. Access the app at `http://127.0.0.1:8000/accounts/`

### Enjoy your new Blogging app
