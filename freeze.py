from flask_frozen import Freezer
from app import app

# Config: Relative URLs Ready to Used
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'build'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print("Your website ready to go! check out the build folder...")