import secrets


def main():
    secret_key = secrets.token_urlsafe(32)

    with open("cookiecutter.json", "r") as f:
        content = f.read()

    content = content.replace("GENERATE_TOKEN_SECRET_KEY", secret_key)

    with open("cookiecutter.json", "w") as f:
        f.write(content)

if __name__ == "__main__":
    main()
