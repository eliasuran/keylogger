from app.main import App


def main() -> None:
    try:
        app = App()
        app.run()
    except KeyboardInterrupt:
        print("\nexiting..")
    except Exception as e:
        print(f"unknown exception: {e}")
        raise e
