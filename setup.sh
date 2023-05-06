rm -rf venv db.sqlite3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py shell < setup.py
python manage.py runserver
