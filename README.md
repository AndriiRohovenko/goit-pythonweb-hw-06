# Student Management Project

This project uses **Poetry** for dependency management and **PostgreSQL** as the database.

## 🚀 Getting Started

1. **Clone the repo**

2. **Install dependencies**

   ```
   poetry install
   ```

3. **Run DB**
   ```
   docker run --name student_db -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres
   ```

**Additional note**
This project requires a .env file with database credentials.
Note: .env is committed (removed from .gitignore) so you can see the exact format for docker setup.

4. **RUN**
   ```
   poetry run src/python my_select.py
   ```
