import json

import requests
from simplejson.errors import JSONDecodeError
from flask import jsonify
from publisher import publisher


def make_request(service_mask, service_url, request, service_id):
    TIMEOUT = 30

    try:
        if request.method == 'GET':
            res = requests.get(service_url + request.full_path.replace('/' + service_mask, ''), headers=request.headers, timeout=TIMEOUT)
        elif request.method == 'POST':
            res = requests.post(service_url + request.path.replace('/' + service_mask, ''), headers=request.headers,
                                json=request.json, files=request.files, timeout=TIMEOUT)
        elif request.method == 'PUT':
            res = requests.put(service_url + request.full_path.replace('/' + service_mask, ''), headers=request.headers,
                               json=request.json, timeout=TIMEOUT)
        elif request.method == 'DELETE':
            res = requests.delete(service_url + request.full_path.replace('/' + service_mask, ''), headers=request.headers,
                                  json=request.json, timeout=TIMEOUT)
        else:
            raise 405

        publisher(
            service_id=service_id,
            request=request,
            status_code=int(res.status_code),
            response_time=res.elapsed.microseconds,
            response=package
        )

        if res is None:
            return [jsonify({'status': res.status_code, 'elapsed': res.elapsed.microseconds, 'json': res.json(),
                             'args': res.args}), res.status_code]
        else:
            return [jsonify(package), res.status_code]
    except (
            405,
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
            requests.exceptions.InvalidSchema
    ) as e:
        if e == 405:
            error_code = 405
            elapsed=0
        elif e is requests.exceptions.Timeout:
            error_code = 504
            elapsed = TIMEOUT
        else:
            error_code = 400
            elapsed = 0

        publisher(
            request=request,
            status_code=error_code,
            response_time=elapsed,
            response=None,
            service_id=service_id
        )
        print(error_code)
        return [jsonify({'status': str(e), 'elapsed': elapsed}), error_code]
