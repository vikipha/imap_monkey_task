## Email attachment executor

The application receives commands from the body of incoming emails.
If the body contains `keyword` it looks for an python file attachment, executes it and responds with the result in email body.
When the `keyword` is missing, responds with `Invalid
keyword` in the body and when just attachment is missing, it returns `Attachment missing`.

### How does it work
The application uses a configured IMAP account/folder, retrieves emails from the sender matching certain pattern, executes `commands` in the body of the email.
and responds accordingly. If the email is successfully processed, a flag is set to prevent it from being processed the next time it is run.


### Requirements:
- User credentials and configuration for some email account with IMAP and SMTP access.


### Configurations
Application is configured through an ENV variables.
Use env file template `env/monkey.env.template`. Make the copy in `env/monkey.env` and replace placeholders 
with your own values.

### Running
It can be run from shell or by included docker-compose.

#### Shell
All you will need is `python` and `pipenv` installed.

```shell
pipenv shell
    bash  # if not already
set -o allexport && source env/monkey.env && set +o allexport
python run.py
```

#### Docker-compose

```shell
docker-compose up
```

#### running tests
```shell
pipenv shell
pipenv install --dev
pytest .
```

### Other
- Code is typed, you can check it by running `mypy .` from pipenv shell (dev packages required, see running test above).
- Code is formatted by [Black](https://github.com/psf/black/).
- [Isort](https://pycqa.github.io/isort/) is used for sorting imports.
