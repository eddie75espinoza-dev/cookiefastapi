import os
import secrets

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_root = os.path.join(current_dir, "..")
    cookiecutter_json_path = os.path.join(template_root, "cookiecutter.json")

    with open(cookiecutter_json_path, "r") as f:
        content = f.read()

    secret_key = secrets.token_urlsafe(32)
    content = content.replace("GENERATE_TOKEN_SECRET_KEY", secret_key)

    with open(cookiecutter_json_path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    main()
