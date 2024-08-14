import json
from db import connection
from app.model.voltage_to_capacity.predict_capacity import vol_to_cap
from app.model.capacity_to_rul.predict_rul import cap_to_rul


def upload_bms(tanggal):
    try:
        with open('app/data/bms.json', 'r') as file:
            bms = json.load(file)
            print("File berhasil dibaca")
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return
    except json.JSONDecodeError:
        print("Error saat membaca file JSON.")
        return

    for value in bms:
        id_bms = value['bms']
        voltage = value['voltage']
        capacity = vol_to_cap(voltage)
        temperature = value['temperature']
        rul = cap_to_rul(capacity)
        query = "INSERT INTO bms (id_bms, tanggal, voltage, temperature, capacity, rul) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (id_bms, tanggal, voltage, temperature, capacity, rul) #untuk postgres menggunakan tuple
        connection(query, 'insert', value)

    print("Data terkirim")

    