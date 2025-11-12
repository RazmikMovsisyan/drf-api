# Loopin

[Click here to go to live Project](https://loopin-8006788e0f02.herokuapp.com/)

![alt text](assets/images/API.png)

Loopin is a social networking platform designed for authenticated users to share images and content with others. Members can post, like, and comment on content, as well as edit or delete their own posts. They can also follow other users to create a personalized feed of posts.

[Frontend Github](https://github.com/RazmikMovsisyan/loopin)

[Frontend Heroku](https://loopinapp-d364a1b22906.herokuapp.com/)

### Objective

The goal of this project is to showcase my expertise in React, Typescript, Django Rest Framework, and Python. Additionally, I aim to demonstrate my skills in Object-Oriented Programming and core programming concepts such as flow control, iteration, conditionals, functions, and data structures.

## Table of Contents

- [Endpoints](#endpoints)
  - [Authentication](#authentication)
    - [User Login](#user-login)
    - [User Logout](#user-logout)
  - [Profiles](#profiles)
    - [Profile List](#profile-list)
    - [Profile Detail](#profile-detail)
  - [Posts](#posts)
    - [Post List](#post-list)
    - [Post Detail](#post-detail)
  - [Likes](#likes)
    - [Like List](#like-list)
  - [Followers](#followers)
    - [Follower List](#follower-list)
  - [Comments](#comments)
    - [Comment List](#comment-list)
    - [Comment Detail](#comment-detail)
- [ER Diagram Django API](#er-diagram-django-api)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Github](#github)
- [Deployment](#deployment)
  - [Deployment](#deployment)
  - [Heroku](#heroku)
- [Credits](#credits)
  - [Used Technologies and Tools](#used-technologies-and-tools)
  - [Django Apps](#django-apps)
  - [Content and Media](#content-and-media)

## Endpoints

## Authentication

#### User Login

- **GET:** `/api-auth/login/` - Returns Django login form
- **POST:** `/api-auth/login/` - Authenticates user and creates session

#### User Logout

- **GET:** `/api-auth/logout/` - Returns Django logout form
- **POST:** `/api-auth/logout/` - Logs out user and ends session

_Note: Uses Django REST Framework session authentication. After login, users are redirected to `/accounts/profile/` (404) - this is normal Django behavior._

## Profiles

#### Profile List

- **GET:** `/profiles/` - Returns paginated list of all profiles

#### Profile Detail

- **GET:** `/profiles/{id}/` - Returns specific profile details

_Note: No dedicated follow/unfollow endpoints - follow functionality is handled through followers endpoint_

## Posts

#### Post List

- **GET:** `/posts/` - Returns paginated list of all posts
- **POST:** `/posts/` - Allows authenticated users to create posts

#### Post Detail

- **GET:** `/posts/{id}/` - Returns specific post details
- **PUT:** `/posts/{id}/` - Allows post owner to update post
- **DELETE:** `/posts/{id}/` - Allows post owner to delete post

_Note: Like status is included in post responses via `like_id` and `likes_count` fields_

## Likes

#### Like List

- **GET:** `/likes/` - Returns paginated list of all likes
- **POST:** `/likes/` - Allows authenticated users to create likes
- **DELETE:** `/likes/{id}/` - Allows like owner to delete like

## Followers

#### Follower List

- **GET:** `/followers/` - Returns paginated list of all follow relationships
- **POST:** `/followers/` - Allows authenticated users to create follow relationships
- **DELETE:** `/followers/{id}/` - Allows follow owner to delete follow relationship

## Comments

#### Comment List

- **GET:** `/comments/` - Returns paginated list of all comments
- **POST:** `/comments/` - Allows authenticated users to create comments

#### Comment Detail

- **GET:** `/comments/{id}/` - Returns specific comment details
- **PUT:** `/comments/{id}/` - Allows comment owner to update comment
- **DELETE:** `/comments/{id}/` - Allows comment owner to delete comment

### **ER Diagram Django API**

## Database Design

Based on my project structure, I created an Entity-Relationship Diagram (ERD) that illustrates the relationships between the models in your Django API using Mermaid. I chose Mermaid because it allows for quick, readable diagrams directly from text, making it easy to maintain and update alongside your code.

This ERD highlights the core models of the Django project and their connections.
I kept it simple and clear so that anyone can quickly understand how the data is structured and how the models interact with each other.

![Entity Relationship Diagrams](assets/images/entity-relationship-diagrams.png)
[Live Preview in Mermaid Editor](https://mermaid.live/edit#pako:eNqtlW1vmzAQx78K8uu0goQSwrspo1W0JExJpmoTEjJwIZ7AjmyzLEvz3WcgTytuk0m1hPDd_e372fjwDiUsBeQh4J8JzjguQmqo9m3uz4yXl7s7tjO-zoLH0dg3PGOFhSYczBcqlnDAEjTxYTCZ-NNKsuFEqxiPvvjvzfAYjMfB82j6pERLluds86bIn82ViIio0UEaxdtGW2O2kE4rugwfeDgkQH6BRjD8tPCfgtl3JYohZzQTkWQhvYDaNf2qESoNkp5tITmhmVEK4BQX0ApAgUne8q6xEBvGL-ZJ1WZJUkDdiX4yQuEQ3TevA_fh671DVNkVTqTBjAlr-UiBM9CAlOuqm0ZY6jiq_bsCgUu5YloMSWTe3qqEUQlU3gzYnLAz4O30xxNzZQFrJmT02sk2VL-3LfwPAK3P7sdQvknzT8JzcV7J2k5QeU91-v-ZT1V4vdi0hZaCSDhZS8KoZvap_zwf-4vFTcX8qmZP_KKMqxzx5RJQB2WcpMiTvIQOKoCrwcpEdZoQyRUoWOSpbgpLXOYyRCGthq0x_cFYcRzJWZmtkLfEuVBWcyoOP_GjRBUUm29pcrTVDMjbod_Is3ruvWWZXac_6A6sXm_w0EFb5PUrr2vbtvvgOLZjWvsO-lPnNO_7btceqMe0-6brOl1FADQFPmQllchzrA6ClEjGJ82VUt8s-7-GH-Lj)

### Manual Testing

- I thoroughly tested each page and feature manually during the development process.

## API Manual Testing

## Overview

Comprehensive manual testing was performed on all API endpoints to ensure proper functionality across authentication, profiles, posts, and comments features.

## Test Results

### Authentication Endpoints

| Feature     | Method | Endpoint            | Description                   | Test Result |
| ----------- | ------ | ------------------- | ----------------------------- | ----------- |
| User Login  | GET    | `/api-auth/login/`  | Returns Django login form     | ✅          |
| User Login  | POST   | `/api-auth/login/`  | Creates authenticated session | ✅          |
| User Logout | GET    | `/api-auth/logout/` | Returns Django logout form    | ✅          |
| User Logout | POST   | `/api-auth/logout/` | Ends user session             | ✅          |

### Profile Endpoints

| Feature        | Method | Endpoint          | Description                            | Test Result |
| -------------- | ------ | ----------------- | -------------------------------------- | ----------- |
| Profile List   | GET    | `/profiles/`      | Returns paginated list of all profiles | ✅          |
| Profile Detail | GET    | `/profiles/{id}/` | Returns specific profile details       | ✅          |

### Post Endpoints

| Feature     | Method | Endpoint       | Description                         | Test Result |
| ----------- | ------ | -------------- | ----------------------------------- | ----------- |
| Post List   | GET    | `/posts/`      | Returns paginated list of all posts | ✅          |
| Post Detail | GET    | `/posts/{id}/` | Returns specific post details       | ✅          |
| Create Post | POST   | `/posts/`      | Creates a new post (authenticated)  | ✅          |
| Update Post | PUT    | `/posts/{id}/` | Updates a post (owner only)         | ✅          |
| Delete Post | DELETE | `/posts/{id}/` | Deletes a post (owner only)         | ✅          |

### Like Endpoints

| Feature     | Method | Endpoint       | Description                         | Test Result |
| ----------- | ------ | -------------- | ----------------------------------- | ----------- |
| Like List   | GET    | `/likes/`      | Returns paginated list of all likes | ✅          |
| Like Detail | GET    | `/likes/{id}/` | Returns specific like details       | ✅          |
| Create Like | POST   | `/likes/`      | Creates a new like (authenticated)  | ✅          |
| Delete Like | DELETE | `/likes/{id}/` | Deletes a like (owner only)         | ✅          |

### Comment Endpoints

| Feature        | Method | Endpoint          | Description                            | Test Result |
| -------------- | ------ | ----------------- | -------------------------------------- | ----------- |
| Comment List   | GET    | `/comments/`      | Returns paginated list of all comments | ✅          |
| Comment Detail | GET    | `/comments/{id}/` | Returns specific comment details       | ✅          |
| Create Comment | POST   | `/comments/`      | Creates a new comment (authenticated)  | ✅          |
| Update Comment | PUT    | `/comments/{id}/` | Updates a comment (owner only)         | ✅          |
| Delete Comment | DELETE | `/comments/{id}/` | Deletes a comment (owner only)         | ✅          |

### Follower Endpoints

| Feature         | Method | Endpoint           | Description                                        | Test Result |
| --------------- | ------ | ------------------ | -------------------------------------------------- | ----------- |
| Follower List   | GET    | `/followers/`      | Returns paginated list of all follow relationships | ✅          |
| Follower Detail | GET    | `/followers/{id}/` | Returns specific follow relationship               | ✅          |
| Create Follow   | POST   | `/followers/`      | Creates a new follow relationship (authenticated)  | ✅          |
| Delete Follow   | DELETE | `/followers/{id}/` | Deletes a follow relationship (owner only)         | ✅          |

### Key Features in Responses:

- **Posts include**: `like_id` (null if not liked, ID if liked) and `likes_count`
- **Profiles include**: `is_owner`, `following_id`, posts_count, followers_count, following_count
- **Likes include**: post ID and owner information

## Testing Methodology

Each endpoint was tested for:

- Proper HTTP status codes and pagination
- Authentication and authorization requirements
- CRUD operations (Create, Read, Update, Delete)
- Data consistency across related endpoints
- Error handling for invalid requests

All tests confirmed the API follows RESTful conventions with consistent paginated responses.

## Bugs

**Application Error in Production for Unauthorized Unsafe Methods**  
Issue: The signup and signin pages were automatically redirecting users directly to the homepage. This bug completely blocked access to the authentication forms, preventing users from registering new accounts or logging into existing ones. As a result, users could not authenticate and were unable to access the application's core functionality.

Fix: This was fixed by correcting the flawed routing logic. The code was updated to ensure the authentication pages (/signup and /signin) remain accessible and do not redirect away until a user successfully submits a form. The forms themselves were also verified to be fully functional, restoring the ability for users to register and log in.

### Github

- I regularly used `git add <filename>` to stage my changes, followed by `git commit -m 'short descriptive message here'` to commit them to the local repository.
- To push my changes, I used `git push` which triggered an automatic deployment to Heroku from the 'main' branch.

## **Deployment**

### **Heroku**

Deployed via **Heroku**.
The live link can be found here: [Loopin API](https://loopin-8006788e0f02.herokuapp.com/)

Steps:

1. Created Heroku app and linked GitHub repo.
2. Added PostgreSQL and Cloudinary add-ons.
3. Config Vars added: `DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`, etc.
4. Added `Procfile`, `requirements.txt`, `runtime.txt`.
5. Disabled Django debug, ensured `.env` file excluded via `.gitignore`.

---

> [!IMPORTANT]
> You would replace the values with your own if cloning/forking my repository.

### Setting Config Vars on Heroku

- Click on the **Settings** tab of your Heroku app.
- Scroll down to the **Config Vars** section and click **Reveal Config Vars**.
- Add the required environment variables by entering the appropriate **Key** and **Value**.

![loopinapp](assets/images/loopin-heroku-config-vars.png)
![loopinapp](assets/images/heroku_settings_var.png)

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `CLOUDINARY_URL`        | user-inserts-own-cloudinary-url                                      |
| `DATABASE_URL`          | user-inserts-own-postgres-database-url                               |
| `SECRET_KEY`            | any-random-secret-key                                                |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |

I have used [Randomkeygen](https://randomkeygen.com/) to generate my individual `SECRET_KEY`

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (_where applicable_) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- _replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located_

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (_recommended_):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (_replace `app_name` with your app name_)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

Or:

Deploy manually:
To deploy your app manually via the Heroku Dashboard:

- Go to your app on the Heroku website.
  ![loopinapp](assets/images/loopinapp.png)

- In the top menu, click on **“Deploy.”**
  ![Deploy1](assets/images/deploy-branch.png)
- Scroll down to the Manual Deploy section and click on **Deploy Branch**
  ![Deploy2](assets/images/heroku_settings_var.png)

- After a successful deployment, click the **“View”** button to open your live app.
  ![Deploy3](assets/images/deployed.png)

The project should now be connected and deployed to Heroku!

### Cloudinary API

- **Create an account** and log in at [cloudinary.com](https://cloudinary.com).
- Once logged in, go to your **Dashboard**.
- Click on **Go to API Keys**:  
   ![dashboard](assets/images/cloudinary_dashboard.png)

- Then click on **Generate New API Key**:  
   ![generate_api](assets/images/cloudinary_generate_api.png)

- You will now see:

  - **Key Name**
  - **API Key**
  - **API Secret**

- These are your Cloudinary credentials used to connect your app.
- Copy the `Key Name`, `API Key`, and `API Secret`.
- Store them in your environment variables (e.g., in a `.env` or `env.py` file):

  ```env
  CLOUDINARY_URL=cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@your_cloud_name
  ```

  > ⚠️ Make sure you include the full URL (starting with `cloudinary://`) as the **value** for the key `CLOUDINARY_URL`.

- Add the same `CLOUDINARY_URL` as a Config Var in Heroku under **Settings > Config Vars**.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!NOTE]
> PostgreSQL databases by Code Institute are only available to CI Students.
> You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
  - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

## Clone and Fork

You can easily clone or fork the **Loopin API** repository for further development.

1. Visit the repository on GitHub: [Loopin API Repository](https://github.com/RazmikMovsisyan/drf-api).
2. Click the **Fork** button to create your own copy.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary
os.environ.setdefault("HOST", "user-inserts-own-host")
os.environ.setdefault("CSRF_TRUSTED_ORIGIN", "https://localhost")

# local environment only (do not include these in production/deployment!)
# (in settings I made sure that DEBUG = False in heroku if you do not add DEBUG to your config vars there)
os.environ.setdefault("DEBUG", "False")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (_Windows/Linux_) or `⌘+C` (_Mac_)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (_if applicable_): `python3 manage.py loaddata file-name.json` (_repeat for each file_)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- _repeat this action for each model you wish to backup_
- **NOTE**: You should never make a backup of the default _admin_ or _users_ data with confidential information.

#### **Clone the Repository using VS Code**

The repository has a single branch with a clear commit history. To clone the repository:

##### For **Mac** Users:

1. Open the **Terminal**.
2. Navigate to your preferred directory:
   ```bash
   cd /path/to/your/directory
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/RazmikMovsisyan/drf-api
   ```
4. Navigate into the directory:
   ```bash
   cd drf_api
   ```

##### For **Windows** Users:

1. Open **Command Prompt** or **PowerShell**.
2. Navigate to the desired directory:
   ```cmd
   cd C:\path\to\your\directory
   ```
3. Clone the repository:
   ```cmd
   git clone https://github.com/RazmikMovsisyan/drf-api
   ```
4. Navigate into the directory:
   ```cmd
   cd drf_api
   ```

# Credits

### Used Technologies and Tools

- [Django Rest Framework](https://www.django-rest-framework.org/) - Framework used for the project
- [Heroku](https://www.heroku.com/) - Platform for deployment
- [Cloudinary](https://cloudinary.com/) - Service for image storage

### Django Apps

- [dj_rest_auth](https://pypi.org/project/dj-rest-auth/) - Used for handling user registration
- [django-allauth](https://pypi.org/project/django-allauth/) - Used for handling user authentication
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Used to add CORS headers to responses
- [rest-framework-simplejwt](https://pypi.org/project/rest-framework-simplejwt/) - Used for JWT-based authentication
- [cloudinary_storage and cloudinary](https://pypi.org/project/django-cloudinary-storage/) - Used for storing images

---

[⬆ Back to Top](#loopin)
