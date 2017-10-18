"""!deploy <app> задеплоит приложение на прод"""

import re
import hashlib

def deploy(app):
    encoded_app = app.encode()
    app_hash = hashlib.md5(encoded_app)

    # sendToGraphite(deploys.production,1)
    # scp something to AWS

    return "деплой приложения  `{}` с хешем `{}` на `прод` ".format(app,
            app_hash.hexdigest())



def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!(?:deploy) (.*)", text)
    if not match:
        return

    return deploy(match[0])
