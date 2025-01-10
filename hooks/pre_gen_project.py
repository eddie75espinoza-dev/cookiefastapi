import secrets


def main():
    secret_key = secrets.token_urlsafe(32)

    {{ cookiecutter.update({"token_secret_key": secret_key}) }}

if __name__ == '__main__':
    main()
