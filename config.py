from os import environ as env
import multiprocessing

PORT = int(env.get("PORT", 8077))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)
#workers = multiprocessing.cpu_count() * 2 + 1
#threads = 2 * multiprocessing.cpu_count()
workers = 5 + 1
threads = 5
