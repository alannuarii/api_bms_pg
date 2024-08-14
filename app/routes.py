from app import app
from flask import jsonify
from app.controller.bms import upload_bms


@app.route('/uploadbms/<tanggal>', methods=['POST'])
def post_data(tanggal):
    try:
        upload_bms(tanggal)
        response = {"message": "Data berhasil dikirim"}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Data gagal terkirim", "error": str(e)}
        return jsonify(error_response), 500