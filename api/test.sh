source .env
export FLASK_ENV='testing'
python3 -m pytest tests
