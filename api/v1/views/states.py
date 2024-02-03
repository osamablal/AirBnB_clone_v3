#!/usr/bin/python3
'''
    RESTful API action for State Object.
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'],
                 strict_slashes=False)
def get_all_states():
    '''
        Retrieving States Objects.
    '''
    state_list = []
    for state in storage.all('State').values():
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    '''
        Retrieving a State Object.
    '''
    try:
        state = storage.get('State', state_id)
        return jsonify(state.to_dict())
    except Exception:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    '''
        Deleting State Object.
    '''
    try:
        state = storage.get('State', state_id)
        storate.delete(state)
        return jsonify({}), 200
    except Exception:
        abort(404)


@app_views.route('/states', methods=['POST'],
                 strict_slashes=False)
def post_state():
    '''
        Creating State Object.
    '''
    if not request.json:
        abort(400)
        return jsonify({"error": "Not a JSON"})
    if 'name' not in request.json:
        abort(400)
        return jsonify({"error": "Missing name"})
    new_state = State(**request.get_json())
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state(state_id):
    '''
        Update a State object
    '''
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
