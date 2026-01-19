# Form Submission & Management System

## How to Run ( IMPORTANT NOTE : All the demo data is included)

## How to Run (Windows)

### Requirements
- Python 3.9+
- Git

---

<!-- Steps --> 
paste these commands in to vs code powershell terminal to run the web app

# Clone the repository
git clone https://github.com/Mashood19/student-management-system.git
cd student-management-system

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations

python manage.py migrate

# Run the server
python manage.py runserver


username: mashood

password: mashood

 Note: The link will open to the form , to access the management panel add /management after http://127.0.0.1:8000 in the adress bar



### Prerequisites
- Python 3.10+ installed
- Git
- DATABASE is Sqlite 3 ( django's defualt)


    