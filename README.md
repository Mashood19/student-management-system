# Form Submission & Management System

## How to Run

1. Clone:
   git clone https://github.com/Mashood19/student-management-system.git
2. Create virtual environment:
   python -m venv venv
   venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Create admin user:
   python manage.py createsuperuser
6. Run server:
   python manage.py runserver
7. Access:
   - Form page: http://127.0.0.1:8000/
   - Management panel: http://127.0.0.1:8000/management/


## Quick Start (Windows & macOS / Linux)

### Prerequisites
- Python 3.10+ installed
- Git
- (Optional) PostgreSQL or other DB for production

### 1. Clone
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
    