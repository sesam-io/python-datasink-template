========================
python-datasink-template
========================

A python microservice template for receiving a JSON entity stream from a Sesam service instance.

::

  $ python3 service/datasink-service.py
   * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger pin code: 260-787-156

The service listens on port 5001. The port number can be changed by passing in the PORT environment variable.

JSON entities can be posted to 'http://localhost:5001/receiver'.
