import base64
import hashlib
import os
import time
import uuid


def _build_wsse_header(app_key: str, app_secret: str) -> str:
    """Construct the value of X-WSSE.

    Args:
        app_key (str): application key
        app_secret (str): application secret

    Returns:
        str: x-wsse content, to be used on Request header
    """
    now = time.strftime(r'%Y-%m-%dT%H:%M:%SZ')
    nonce = str(uuid.uuid4()).replace('-', '')
    digest = hashlib.sha256((nonce + now + app_secret).encode()).hexdigest()
    digestBase64 = base64.b64encode(digest.encode()).decode()

    wsse = f'UsernameToken Username="{app_key}",'
    wsse += f'PasswordDigest="{digestBase64}",Nonce="{nonce}",'
    wsse += f'Created="{now}"'
    return wsse


def build_headers() -> dict:
    """Build headers for SMS sending request

    Returns:
        dict: header parameters
    """
    app_key = os.getenv('APP_KEY')
    app_secret = os.getenv('APP_SECRET')

    header = {
        'Authorization':
            'WSSE realm="SDP",profile="UsernameToken",type="Appkey"',
        'X-WSSE': _build_wsse_header(app_key, app_secret)
    }

    return header


def build_body(
        receiver: str, template_id: str, template_params: str,
        status_callback: str = "") -> dict:
    """Build body for SMS sending request.

    Args:
        receiver (str): Number of receiver(s) in global format
            (+{Country code}{Area code}{Terminal number}).
            Separate multiple recipient numbers with commas (,).
        template_id (str): Template ID
        template_params (str): List of SMS template variables, used to
            configure the variables specified in template_id.
            This parameter is in the JSONArray format.
        status_callback (str): Callback address of the user for
            receiving the SMS status report. Default is "" (no callback)

    Returns:
        dict: request body
    """
    body = {
        'from': os.getenv('CHANNEL_NO'),
        'to': receiver,
        'templateId': template_id,
        'templateParas': template_params,
        'statusCallback': status_callback
    }
    return body
