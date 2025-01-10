import secrets

def generate_token_secret_key():
    return secrets.token_urlsafe(32)

def main():
    secret_key = generate_token_secret_key()

    context = {{ cookiecutter }}
    context['token_secret_key'] = secret_key

if __name__ == '__main__':
    main()
