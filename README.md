# acqstackdb

`release`: [![Build Status](https://travis-ci.org/18F/acqstackdb.svg?branch=release)](https://travis-ci.org/18F/acqstackdb)

`develop`: [![Build Status](https://travis-ci.org/18F/acqstackdb.svg?branch=develop)](https://travis-ci.org/18F/acqstackdb) [![Accessibility](https://continua11y.18f.gov/18F/acqstackdb.svg?branch=develop)](https://continua11y.18f.gov/18F/acqstackdb)

This is a Django app built to track the progress of acquisitions by 18F Acquisitions.

## Installation

This app is designed to run on Python 3.5.1. `pyenv` is recommended for managing your Python version, along with `pyenv-virtualenvwrapper` for managing the dependencies installed with `pip`. With that, you can prepare your development environment by running:

```
git clone https://github.com/18f/acqstackdb.git
cd acqstackdb
createdb acqstackdb
mkvirtualenv acqstackdb
pip install -r requirements.txt
```

Authentication is managed via GitHub OAuth, with access limited to a specified GitHub team. First, you'll need a [GitHub application](https://github.com/settings/applications/new). Next, you'll need a GitHub organization and [a team within it](https://help.github.com/articles/setting-up-teams/). Getting the team's ID is a bit tricky, unfortunately, and involves [querying the GitHub API](https://developer.github.com/v3/orgs/teams/#list-teams).

At this point, you'll have the GitHub application's `Client ID` and `Client Secret`, along with your team's `ID`. Now, run the following:

```
export SOCIAL_AUTH_GITHUB_TEAM_KEY=YOUR_CLIENT_ID
export SOCIAL_AUTH_GITHUB_TEAM_SECRET=YOUR_CLIENT_SECRET
export SOCIAL_AUTH_GITHUB_TEAM_ID=YOUR_TEAM_ID
export SOCIAL_AUTH_REDIRECT_IS_HTTPS=False # to allow HTTP redirect to http://localhost
./manage.py runserver
```

The app should now be running at http://localhost:8000.

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

### Branch flow

- Main branch: `release`
- Development branch: `develop`

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
