# Simple Blog/News Site

## Overview

The **Simple Blog/News Site** is a web-based platform for creating, managing, and publishing categorized media content. This application is designed to provide an engaging and user-friendly experience for public visitors and an efficient content management interface for site administrators. 

The project is built using **Bootstrap** for the frontend and **Django** for the backend.

---

## Features

### Public Section
1. **Homepage**  
   - Displays categorized posts (e.g., cultural, sports, social) with at least four categories.  
   - Highlights featured or important posts in a dedicated section.  
   - Designed with a responsive layout for audience engagement.  

2. **Category Pages**  
   - Displays posts in paginated form (10 posts per page).  
   - Includes navigation buttons for easy access to additional pages.  

3. **Search Functionality**  
   - Enables users to search posts by content or keywords.  

4. **Post Pages**  
   - Each post includes a title, image, publication date, and summary. Full content is displayed upon clicking the post.  
   - Users can leave comments on posts.  
   - Visitor registration timestamps are recorded using the solar date format.  

5. **Responsive Design**  
   - Fully responsive layout powered by **Bootstrap** for optimal viewing on various devices.  

---

### Management Panel Section
1. **Authentication**  
   - User login with a username and password.  
   - Restricted access ensures only authenticated users can access the management panel.  

2. **Content Management (CRUD)**  
   - Manage categories: Create, update, delete, and view category lists.  
   - Manage posts: Create, update, delete, and view post lists.  
   - Schedule posts to be published at future dates.  

3. **Comments Management**  
   - View comments associated with posts.  
   - Delete unwanted comments through a simple interface.  

4. **Content Preview**  
   - Preview posts before publishing to ensure accuracy.  

5. **Logout**  
   - Provides an option to log out securely from the management panel.  

---

## Simplifications
To reduce complexity:
- User access levels and profiles are not implemented.  
- Each user manages only their own posts.  
- Advanced content editing features are excluded.  
- Comments are displayed in a basic format with only deletion functionality available for administrators.  

---

## Installation

### Prerequisites
- Python 3.x  
- Django  
- Bootstrap (linked via CDN in templates)  

### Steps
1. Clone the repository:  
   ```bash
   git clone https://github.com/mohdelite/Advance_blog.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd Advance_blog
   ```
3. Create a virtual environment and activate it:  
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```
4. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:  
   ```bash
   python manage.py migrate
   ```
6. Start the development server:  
   ```bash
   python manage.py runserver
   ```
7. Open the site in your browser at `http://127.0.0.1:8000/`.

---

## Technologies Used
- **Frontend:** Bootstrap, HTML, CSS  
- **Backend:** Django  
- **Database:** SQLite (default for Django; replaceable with other DBs like PostgreSQL or MySQL)  

---

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.
