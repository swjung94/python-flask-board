from sboard import create_app
import config
if __name__ == "__main__":
    create_app().run(host="localhost", port=config.PORT, debug=config.DEBUG_MODE)
