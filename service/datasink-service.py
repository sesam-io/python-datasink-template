from flask import Flask, request, Response
import cherrypy
import json
import os

app = Flask(__name__)

@app.route('/receiver', methods=['POST'])
def receiver():
    # create output directory
    directory = os.path.join(os.getcwd(), "received")
    os.makedirs(directory, exist_ok=True)

    # get entities from request and write each of them to a file
    entities = request.get_json()
    if not isinstance(entities, list):
        entities = [entities]

    for entity in entities:
        entity_id = entity["_id"]
        filename = os.path.join(directory, entity_id + ".json")
        print("Writing entity \"%s\" to file '%s'" % (entity_id, filename))
        with open(filename, "w") as fp:
            json.dump(entity, fp, indent=4, sort_keys=True)

    # create the response
    return Response("Thanks!", mimetype='text/plain')

if __name__ == '__main__':
    cherrypy.tree.graft(app, '/')

    # Set the configuration of the web server to production mode
    cherrypy.config.update({
        'environment': 'production',
        'engine.autoreload_on': False,
        'log.screen': True,
        'server.socket_port': 5001,
        'server.socket_host': '0.0.0.0'
    })

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()
