#!/usr/bin/ python
from flask import abort
import random
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/api/v1.0/<float:lat>@<float:longt>|<float:dlat>@<float:dlongt>', methods=['GET'])
def get_coordinate(lat, longt, dlat, dlongt):
    """
    import direction_handler
    direction_json = direction_handler.get_direction_json(lat, longt, dlat, dlongt)
    for step in direction_json['legs'][0]['steps']:
      try:
        if step['maneuver'] == 'turn-left' or step['maneuver'] == 'turn-slight-left':
            continue
        get_speed_stat(step)
      except (KeyError, IndexError) as e:
            continue
    """
    random_speed = random.randint(5,80)
    return jsonify({'speed': random_speed, "callback_time":random_speed})

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8090)

