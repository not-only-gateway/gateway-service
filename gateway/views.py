from flask import jsonify
from flask import request
from app import app
from utils import Utils
from gateway.request import make_request
import env
import request as python_request
from utils import make_jwt, decrypt_jwt


@app.route('/<mask>/<any:uri>', methods=['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def redirect(mask, uri=None):
    token = make_jwt({'service': 'gateway'})
    service = python_request.get(
        env.SERVICE_MANAGEMENT_URL,
        headers={'Authorization': token},
        params={
            'mask': mask,
            'uri': uri,
            'user_authorization': request.headers.get('Authorization', None)
        }
    )
    service = service.json()
    # service.json = {'accepted': bool, 'service_url': PATH, 'service_id': integer}



    if service.get('accepted', False):
        response = make_request(
            service_mask=mask,
            service_id=service.get('service_id', None),
            service_url=service.get('service_url', None),
            request=request
        )
        return response[0], response[1]
    else:
        return jsonify({'status': 'error', 'description': 'not_found', 'code': 404}), 404
