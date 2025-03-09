from loguru import logger as log
from flask import Flask, make_response, request
from datetime import datetime

DATAFILE = "data.txt"

app = Flask("rook-radar-server")

@app.route("/", methods=["GET"])
def mainpage():
    log.info("main page read")
    with open(DATAFILE, 'r') as fh:
        return make_response(fh.read())


@app.route("/datum", methods=["PUT", "POST"])
def datum():
    log.debug(f"datum write {request.method}")
    with open(DATAFILE, "a") as fh:
        record = f'{datetime.utcnow()} {request.get_data().decode('utf-8')}'
        fh.write(record)
        fh.write('\n')
        log.info(record)
    return make_response('ok')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1999, debug=True)