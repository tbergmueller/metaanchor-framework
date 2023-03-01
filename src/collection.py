import os

from flask import Blueprint, request, current_app, Response
from src.database import get_db
import json
import requests

bp = Blueprint('collection', __name__, url_prefix='/collection/')
db = get_db() # move that to app.db


def assemble_error_response(error_code, msg, http_err_code= 500, ex=None):
    resp_obj = {
        "success": False,
        "msg": msg,
        "error_code": error_code
    }

    if ex:
        resp_obj['exception'] = str(ex)

    return Response(json.dumps(resp_obj), status=http_err_code, mimetype='application/json')




@bp.route('/<string:collection_name>/<int:token_id>', methods=['GET'])
def getMetadata(collection_name, token_id):
    # generiere bild
    #

    slid_resolve_url = current_app.config['METAANCHOR_API_URL'] + f"/anchor/resolve-token/{token_id}"

    # FIXME PROPER! error handling
    headers = {'Authorization': f'Bearer {os.getenv("METAANCHOR_API_KEY")}'}
    response = requests.get(url=slid_resolve_url, headers=headers)

    jresp = json.loads(response.text)

    if "raw_resp" not in jresp:
        return assemble_error_response(error_code="INTERNAL_ERROR", msg="Unexpected response format")

    if "slid" not in jresp["raw_resp"]:
        return assemble_error_response(error_code="INTERNAL_ERROR", msg="Unexpected response format")

    slid = jresp["raw_resp"]['slid']

    return {
        "name": f"DS {slid}",
        "description": "This is DigitalSoul SandboxDemo Metadata and subject to change!",
        "image": "ipfs://QmUhvy1WYQGiWP8z2jKsBMVUKinicbaV9xx9TfKYhPP2HC/4.gif",
        "external_url": "",
        "background_color": "",
        "attributes": [
            {
                "trait_type": "SLID",
                "value": slid
            }
        ]
    }
