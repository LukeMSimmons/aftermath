from app import app 
import sys

# Add project directory to sys.path
project_home = u'/home/aftermath/aftermath'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

application = app.server
