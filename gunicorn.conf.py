# Gunicorn configuration file
import multiprocessing

# Worker Options
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
threads = 4

# Logging Options
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Process Naming
proc_name = 'flask-example'

# Socket
bind = '0.0.0.0:8000'

# SSL Options (if needed)
# keyfile = '/path/to/keyfile'
# certfile = '/path/to/certfile'

# Server Mechanics
timeout = 30
keepalive = 2

# Server Hook Options
def on_starting(server):
    """Called just before the master process is initialized."""
    pass

def on_reload(server):
    """Called before code is reloaded."""
    pass

def when_ready(server):
    """Called just after the server is started."""
    pass