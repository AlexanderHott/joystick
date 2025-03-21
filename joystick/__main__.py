from joystick.config import get_config


def main():
    config = get_config()
    print(f"Hi from {config['name']}")


if __name__ == "__main__":
    main()
