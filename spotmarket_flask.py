#-----------------------------------------------------------------------------
# spotmarket_flask.py
# https://github.com/brentnowak/spotmarket
#-----------------------------------------------------------------------------
# Version: 0.1
# - Initial release
# Version: 0.3
# - Migration to Flask+Bootstrap
#-----------------------------------------------------------------------------

from app import app

app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
