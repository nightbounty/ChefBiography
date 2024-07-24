# Chef Biography

A web application that generates random chef biographies with contact information. This project utilizes a FastAPI backend, a Vue.js frontend, PostgreSQL for the database, and Docker for containerization.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)

## Project Overview

Chef Biography is a web application designed to create random chef biographies complete with contact information. The project is built using:
- **FastAPI** for the backend
- **Vue.js** for the frontend
- **PostgreSQL** as the database
- **Docker** for containerization
  
![Screenshot 2024-07-24 at 12 36 55 PM](https://github.com/user-attachments/assets/962c4913-095e-470f-976b-657c2381968b)


## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/nightbounty/ChefBiography.git
   cd ChefBiography
2. **Backend setup:**
   ```sh
   cd backend
   pip install -r requirements.txt
   fastapi dev main.py
  PS. Have an .env file with your postgresel database url. DATABASE_URL="postgresql:..."
  You can setup with docker too
  ```sh
      docker-compose up --build
  ```

3. **Frontend setup:**
   ```sh
   cd frontend
   npm install
   npm run dev

