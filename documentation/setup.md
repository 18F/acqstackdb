# Setup

There are two methods of setting up the acqstackdb application:

1. Local installation; and
2. Using docker-compose.

## Local Installation

This app is designed to run on Python 3.5.1. `pyenv` is recommended for managing
your Python version, along with `pyenv-virtualenvwrapper` for managing the
dependencies installed with `pip`. With that, you can prepare your development
environment by running:

```
git clone https://github.com/18f/acqstackdb.git
cd acqstackdb
createdb acqstackdb
./manage.py migrate
mkvirtualenv acqstackdb
pip install -r requirements.txt
```

Authentication is managed via GitHub OAuth, with access limited to a specified
GitHub team. First, you'll need a [GitHub
application](https://github.com/settings/applications/new). The callback URL for
the application is `[your-url]/complete/github-team`.  Next, you'll need a
GitHub organization and [a team within
it](https://help.github.com/articles/setting-up-teams/). Getting the team's ID
is a bit tricky, unfortunately, and involves [querying the GitHub
API](https://developer.github.com/v3/orgs/teams/#list-teams).

At this point, you'll have the GitHub application's `Client ID` and `Client
Secret`, along with your team's `ID`. Now, run the following:

```
export SOCIAL_AUTH_GITHUB_TEAM_KEY=YOUR_CLIENT_ID
export SOCIAL_AUTH_GITHUB_TEAM_SECRET=YOUR_CLIENT_SECRET
export SOCIAL_AUTH_GITHUB_TEAM_ID=YOUR_TEAM_ID
export SOCIAL_AUTH_REDIRECT_IS_HTTPS=False # to allow HTTP redirect to http://localhost
./manage.py runserver
```

The app should now be running at http://localhost:8000.

If you'd like to load some starter data, you have two options: fixtures and factories. To set up a skeleton that looks like our production site, `./manage.py loaddata acquisitions/fixtures/*.json` will pull in the tracks, stages, steps, and actors. For a wider-ranging randomized setup, you can use `./manage.py seed_database`.

## Using docker-compose

To use [docker-compose](https://docs.docker.com/compose/), you'll need to run the folloiwng commands:

```
git clone https://github.com/18f/acqstackdb.git
cd acqstackdb
mv .env.example .env
```

Then, edit the `.env` file with the GitHub application's `Client ID` and `Client
Secret`, along with your team's `ID`. Once, you done this, run:

```
docker-compose up
```
