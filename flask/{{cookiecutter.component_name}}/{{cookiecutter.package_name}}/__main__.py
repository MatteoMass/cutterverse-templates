import argparse

from {{cookiecutter.package_name}}.app import gunicorn_builder


def get_args():

    parser = argparse.ArgumentParser()
    # add here parser.add_argument("-x", "--example")
    args, _ = parser.parse_known_args()
    return args


def main():

    # Get args
    args = get_args()

    # Use them: args.example
    app = gunicorn_builder.create_app()
    app.run()


if __name__ == '__main__':
    main()