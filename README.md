# Note-Taking Website

<p>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoft-sql-server&logoColor=white" />
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/html5-E34F26?logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6?logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/bootstrap-563D7C?logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-07405E?logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/GIT-E44C30?logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/prettier-1A2C34?logo=prettier&logoColor=white" />
<img src="https://img.shields.io/badge/docker-1572B6?logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub_Actions-563D7C?logo=github-actions&logoColor=white"/>
</p>

![PyPI v0.5](https://img.shields.io/badge/PyPI-v0.5-blue.svg)
![MIT License](https://img.shields.io/badge/License-MIT-lightgray.svg)
![build](https://img.shields.io/badge/Build-passing-green.svg)


Welcome to my Note-Taking Website repository! This web application is built using Django, a Python web framework, to provide a user-friendly and secure platform for managing notes. Users can sign up, log in, and log out to create, edit, and delete their notes seamlessly.

![alt text](https://github.com/izam-mohammed/Notes/blob/main/Demo/demo.png)

## Features

- **User Authentication:** Secure user registration, login, and logout functionalities are integrated to ensure data privacy.
- **Note Creation:** Users can create new notes with titles and content, making it easy to organize and manage their thoughts.
- **Note Editing:** The ability to edit existing notes allows users to update their content whenever necessary.
- **Note Deletion:** Users can remove notes they no longer need, enhancing note management efficiency.
- **Responsive Design:** The web application is designed to provide a seamless experience across various devices and screen sizes.

## Getting Started

### Run with Docker

Before you start, ensure you have the following installed:

- Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/izam-mohammed/Notes.git
   cd Notes
   ```

2. **Run these:**
   ```
   docker-compose build
   docker-compose up
   ```

### Manual way

To get started with the Note Taking Website, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/izam-mohammed/Notes.git
   cd Notes
   ```

2. **Setup Virtualenv (Windows)**:
   ```
   pip install virtualenv
   virtualenv venv
   .\venv\Scripts\Activate
   ```
   **Setup Virtualenv (mac/linux)**:
   ```
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:** Install the required Python packages using `pip`:
   ```
   pip install -r requirements.txt
   ```

4. **Database Setup:** Set up the database by running migrations:
   ```
   cd NotesWebsite
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server:** Start the development server:
   ```
   python manage.py runserver
   ```

6. **Access the Website:** Open your web browser and go to `http://127.0.0.1:8000/` to access the Note Taking Website.
   Default admin: **Username**: user **passowrd**:1234

## Contributing

Contributions are welcome! If you'd like to contribute to the project, feel free to submit issues or pull requests. Please ensure your contributions align with the project's coding standards and guidelines.

## Repository Code Formatting

This repository follows a consistent code formatting approach to enhance readability and maintainability.

### Python Files

Python files in this repository are formatted using [Black](https://github.com/psf/black). Black is an opinionated code formatter that automatically formats your Python code to adhere to the PEP 8 style guide.

To ensure that your Python code is formatted correctly, you can install Black and format the code by running the following command in your terminal:

```bash
pip install black
black .
```

### HTML Files

HTML files in this repository are formatted using [Prettier](https://prettier.io/). Prettier is a code formatter that supports multiple languages, including HTML.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The project utilizes the [Django Framework](https://www.djangoproject.com/) for web development.
- UI styling is based on [Bootstrap](https://getbootstrap.com/) for a responsive design.
- Icons are provided by [Font Awesome](https://fontawesome.com/).

---

Feel free to customize this `README.md` template to suit your project's specific details and add any additional sections you find relevant.


