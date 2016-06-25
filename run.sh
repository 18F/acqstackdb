# Per https://docs.docker.com/compose/startup-order/, we are going to use
# wait-for-it (source: https://github.com/vishnubob/wait-for-it) as a wrapper
# to ensure that postgres is ready to accept connections
./third-party/wait-for-it/wait-for-it.sh db:5432

# Now, run the script
python manage.py migrate
python manage.py runserver 0.0.0.0:5000
