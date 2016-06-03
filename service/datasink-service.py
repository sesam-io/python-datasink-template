from flask import Flask, request, Response
import json
import os

app = Flask(__name__)

@app.route('/receiver', methods=['POST'])
def receiver():
    entities = request.get_json()
    for entity in entities:
        entity_id = entity["_id"]
        filename = os.path.join(os.getcwd(), entity_id + ".json")
        print("Writing entity \"%s\" to file '%s'" % (entity_id, filename))
        with open(filename, "w") as fp:
            json.dump(entity, fp, indent=4, sort_keys=True)
    return Response("Thanks!", mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

