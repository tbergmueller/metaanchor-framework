import logging

from flask import Blueprint, request, current_app, Response, send_file, abort
import werkzeug.exceptions
import cv2

from src.metaanchor_api import MetaAnchorAPI

bp = Blueprint('artwork', __name__, url_prefix='/artwork/')

@bp.route('/<string:collection_name>/<string:anchor>', methods=['GET'])
def getAnchorImage(collection_name, anchor):
    # Use opencv to paint a bit on the image

    [slid, anchor] = MetaAnchorAPI().resolve(anchor)

    if not slid:
        raise werkzeug.exceptions.NotFound(f"No artwork for anchor {anchor}")

    # For Demo-Purposes, we will now write the SLID into the image!
    # This is a security risk in an actual setting
    # Never make the SLID public!
    img = cv2.imread('assets/metaanchor_template.png', cv2.IMREAD_UNCHANGED)

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 0, 255)
    thickness = 5

    # Using cv2.putText() method
    img = cv2.putText(img, slid,  (200, 620), font, 2, color, thickness, cv2.LINE_AA)
    img = cv2.putText(img, "DigitalSoul", (200, 110), font, 1.7, color, 4, cv2.LINE_AA)
    img = cv2.putText(img, "(R)", (480, 80), font, 0.8, color, 1, cv2.LINE_AA)

    _, img_encoded = cv2.imencode('.png', img)
    buf = img_encoded.tobytes()
    response = Response(buf, mimetype='image/png')
    response.headers.set('Content-Length', len(buf))

    return response