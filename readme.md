# Loopin
[Click here to go to live Project](https://loopin-8006788e0f02.herokuapp.com/)

![alt text](assets/images/API.png)

Loopin is a social networking platform designed for authenticated users to share images and content with others. Members can post, like, and comment on content, as well as edit or delete their own posts. They can also follow other users to create a personalized feed of posts.


[Frontend Github](https://github.com/RazmikMovsisyan/loopin)

[Frontend Heroku](https://loopinapp-d364a1b22906.herokuapp.com/)

### Objective
The goal of this project is to showcase my expertise in React, Typescript, Django Rest Framework, and Python. Additionally, I aim to demonstrate my skills in Object-Oriented Programming and core programming concepts such as flow control, iteration, conditionals, functions, and data structures.

## Table of Contents
* [Endpoints](#endpoints)
  * [Authentication](#authentication)
    * [Registration](#registration)
    * [API Tokens](#api-tokens)
    * [API Token Refresh](#api-tokens-refresh)
  * [Profiles](#profiles)
    * [Profile List](#profile-list)
    * [Profile Detail](#profile-detail)
    * [Profile Follow](#profile-follow)
    * [User Profile](#user-profile)
  * [Posts](#posts) 
    * [Post List](#post-list)
    * [Post Detail](#post-detail)
    * [Post Like](#post-like)
    * [Post Search](#post-search)
    * [Profile Post List](#profile-post-list)
    * [Follow Post List](#follow-post-list)
    * [Liked Post List](#liked-post-list)
  * [Comments](#comments) 
    * [Comment List](#comment-list)
    * [Comment Detail](#comment-detail)
 * [Manual Testing](#manual-testing)
 * [Bugs](#bugs)
* [Git](#git)
* [Deployment](#deployment)
  * [Deployment Preparation](#deployment-preparation)
  * [Setup](#setup)
* [Credits](#credits)
  * [Used Technologies and Tools](#used-technologies-and-tools)
  * [Django Apps](#django-apps)
  * [Content and Media](#content-and-media)

## Endpoints

## Authentication

#### Registration
- **POST:** Creates a new user

#### API Tokens
- **POST:** Returns a set of JWT tokens

#### API Token Refresh
- **POST:** Allows authenticated users to refresh their access token by providing a refresh token

## Profiles

#### Profile List
- **GET:** Returns a list of all profiles

#### Profile Detail
- **GET:** Returns the profile specified by ID

#### Profile Follow
- **GET:** Lists profiles following the specified profile  
- **POST:** Allows authenticated users to follow the specified profile

#### User Profile
- **GET:** Returns the profile of the authenticated user  
- **PUT:** Allows users to update their profile

## Posts

#### Post List
- **GET:** Returns a list of all posts  
  - Authenticated: Filters out posts from the requesting user and the profiles they follow  
- **POST:** Allows authenticated users to create posts

#### Post Detail
- **GET:** Returns the post specified by ID  
- **PUT:** Allows the post owner to update the post  
- **DELETE:** Allows the post owner to delete the post

#### Post Like
- **GET:** Returns a list of profiles who liked the specified post  
- **POST:** Allows authenticated users to like the specified post

#### Post Search
- **GET:** Returns posts containing the specified keywords in their title, description, or author's profile name

#### Profile Post List
- **GET:** Returns all posts from the specified profile

#### Follow Post List
- **GET:** Allows authenticated users to retrieve a list of posts from profiles they follow

#### Liked Post List
- **GET:** Allows authenticated users to retrieve a list of posts they liked

## Comments

#### Comment List
- **GET:** Returns all comments from a specified post  
- **POST:** Allows authenticated users to create comments on the specified post

#### Comment Detail
- **GET:** Returns the comment specified by ID  
- **PUT:** Allows the comment owner to update the comment  
- **DELETE:** Allows the comment owner to delete the comment

### Manual Testing
- I thoroughly tested each page and feature manually during the development process.  

| Testcase                                                                     | Expected Result                                                                                             | Test Result |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| **Profiles**                                                                 |                                                                                                             |             |
| Profile List                                                                 | Returns 200 response: a list of all the profiles                                                            | ✅          |
| Profile Detail                                                                | Returns 200 response: the profile specified by ID                                                           | ✅          |
| Profile Follow                                                                | Returns 403 Forbidden (Unauthenticated) / 200 response (Authenticated)                                      | ✅          |
| User Profile                                                                 | Returns the profile of the requesting user (Authenticated) / 403 error (Unauthenticated)                    | ✅          |
| **Posts**                                                                    |                                                                                                             |             |
| Post List                                                                    | Returns 200 response: a list of all posts                                                                   | ✅          |
| Post Detail                                                                  | Returns the post specified by ID                                                                            | ✅          |
| Post Like                                                                   | Allows authenticated users to like the specified post (201 response)                                        | ✅          |
| Post Search                                                                 | Returns a list of posts containing the specified keywords                                                   | ✅          |
| **Comments**                                                                 |                                                                                                             |             |
| Comment List                                                                 | Returns all comments from a specified post                                                                  | ✅          |
| Comment Detail                                                               | Returns the comment specified by ID                                                                         | ✅          |
| POST Comment                                                                  | Allows authenticated users to create comments (201 response)                                                | ✅          |

## Bugs
**Application Error in Production for Unauthorized Unsafe Methods**  
Unauthorized requests using unsafe methods are causing errors in the live application. On local deployments, these requests return a 401 error. The issue might be related to the remote PostgreSQL database but hasn't been addressed due to time constraints. This happened after reaching out to tutor support.

Two days before the submission deadline of my PP5, I received a message from two Code Institute staff members informing me about a required password change for my Neon database.

After updating the database URL, the application’s functions and data fell into disarray.

Unfortunately, the same issue also affected my PP4 project, which is or was still under assessment at the time. As a result, I suddenly had to manage and fix problems in both projects at once.

For PP4, I lost all content because no backup had been created. I did not receive any support in this situation and got rejected by tutor support for two reasons and had to manually recreate all content, user accounts, and superusers on my own.

I immediately reached out to another tutor Support again to resolve the issue.

However, one of the tutors caused further issues in my PP5 project, disrupting basic functionalites. Instead of solving the existing issues, additional complications were introduced, and unfortunately I did not receive further assistance.

Ultimately, I was able to bring my project to a functional level with all core logic in place, to avoid the risk of failing the assessment.

I am willing to provide more details regarding this matter if needed to keep everything transparent.

### Git
- I regularly used `git add <filename>` to stage my changes, followed by `git commit -m 'short descriptive message here'` to commit them to the local repository.
- To push my changes, I used `git push` which triggered an automatic deployment to Heroku from the 'main' branch.

## Deployment

The website was deployed on Heroku.

### Deployment Preparation
Before deploying, the following preparations were made:
- The `DEBUG` setting in `settings.py` was set to `False`.
- All dependencies were recorded in the `requirements.txt` file by running `pip3 freeze --local > requirements.txt`.
- The start command `web: gunicorn Loopin-api.wsgi` was added to the `Procfile`.

### Setup
To deploy the app on Heroku, follow these steps:
- Create a new app from the Heroku dashboard.
- Choose an app name and select a region, then click "Create App".
- In the app’s settings, add necessary configuration variables such as Cloudinary URL, database URL, and Django secret key.
- Add the "Heroku/Python" buildpack.
- Go to the "Deploy" tab and choose "GitHub" as the deployment method, then follow the steps to link your GitHub repository to Heroku.
- Once connected, you can either enable automatic deployment or manually deploy a branch by clicking the "Deploy Branch" button.

The live link can be found here: [Loopin API](#)

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
