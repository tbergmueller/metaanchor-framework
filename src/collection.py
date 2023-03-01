from flask import Blueprint, request, current_app, Response
from src.database import get_db
import json
import requests

bp = Blueprint('collection', __name__, url_prefix='/collection/')
db = get_db() # move that to app.db


@bp.route('/<string:collection_name>/<int:token_id>', methods=['GET'])
def _create_job(collection_name, token_id):
    return {
        "name": "MetaAnchor DigitalSoul Sandbox",
        "description": "This is DigitalSoul SandboxDemo Metadata and subject to change!",
        "image": "ipfs://QmUhvy1WYQGiWP8z2jKsBMVUKinicbaV9xx9TfKYhPP2HC/4.gif",
        "external_url": "",
        "background_color": "",
        "attributes": [
            {
                "trait_type": "SLID",
                "value": "H898SJ8"
            }
        ]
    }
