import os

from flask import Blueprint, request, current_app, Response, send_file
from src.database import get_db
import json
from src.metaanchor_api import MetaAnchorAPI


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


@bp.route('/<int:token_id>', methods=['GET'])
def getMetadata(token_id):

    # Create a dynamic URL for images
    public_url = os.getenv('PUBLIC_URL', request.base_url.replace(f'collection/{token_id}', ''))
    # Note the SLID should never be disclosed, this is for demo-purposes only
    # If you disclose a label-identifier, use the Anchor!
    slid, anchor = MetaAnchorAPI().resolve(token_id=token_id)

    return {
        "name": f"MetaAnchor {anchor[0:5]}..{anchor[-3:]}", # Note the SLID should normally never be disclosed. This is for demo-purposes only!
        "description": "This is DigitalSoul SandboxDemo Metadata and subject to change!",
        "image": public_url.strip('/') + f'/artwork/{anchor}', # This calls the endpoint below
        "external_url": "",
        "background_color": "",
        "attributes": [
            {
                "trait_type": "Anchor",
                "value": anchor
            }
        ]
    }


