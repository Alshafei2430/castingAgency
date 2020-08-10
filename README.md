# Motivation for project

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

# Project dependencies

    run "pip install requirements.txt"

# local development

    <!-- make sure to install postgressql and populate setup.sh and .env files with your information-->
    cd into the root dierctory
    run "source setup.sh"
    run "flask run"

# hosting instructions

    cd into the root dierctory
    <!-- make sure to create heroku account and install heroku cli -->
    run "heroku login"
    run "git init"
    run "git add ."
    run "git commit -m "message" "
    run "heroku create"
    run "git push heroku master"
