import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return jsonify({
        "endpoints": [str(rule) for rule in app.url_map.iter_rules()]
    })

@app.route('/member', methods=['POST'])
def add_member():
    try:
        member = request.get_json()
        jackson_family.add_member(member)
        return jsonify({"message": "Member added successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"message": "Member not found"}), 404

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        result = jackson_family.delete_member(member_id)
        if result:
            return jsonify({"done": True}), 200
        else:
            return jsonify({"message": "Member not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 400

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

