import os
import sys

# Create some variables for us to use
PACKAGE_VENV_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_ROOT = os.path.dirname(os.path.dirname(PACKAGE_VENV_DIR))
PACKAGE_NAME = os.path.basename(PACKAGE_ROOT)
PACKAGE_SRC_DIR = os.path.join(PACKAGE_ROOT, "src/{}".format(PACKAGE_NAME))

# Add the src directory to our import path
sys.path.append(PACKAGE_SRC_DIR)

# Import the package modules directory to use them.
# (Imports come from the src/<package-name> directory)
# ie:
#   from main import method

# Use the test class to create printable tests on the modules.
class Test(object):
    def print(self):
        print("{}\n".format(self.run()))

    def run(self):
        raise Exception("run() needs to be created for each test class instance.")

# Create the tests here.
# ie:
#   class TestOne(Test):
#       def run(self):
#           result = method()
#           return result

# Run the tests in the global scope.
# ie:
#   TestOne.print()

# Use this file by running it when its imported.
# (While in <package_root>/venvs/pre)
# ie:
#   > pipenv install --python 3.6
#   > pipenv install <packages-required>
#   > pipenv run python
#   > import test
#   > ...tests are invoked...
