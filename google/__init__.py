import inspect
import sys
import os

# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# currentdir = os.path.dirname(os.getcwd())
# parentdir = os.path.dirname(os.getcwd())
# sys.path.append(parentdir)

# current_dir =  os.path.abspath(os.path.dirname(__file__))
# parent_dir = os.path.abspath(current_dir + "/../")
# sys.path.append(parent_dir)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))