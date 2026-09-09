result = {
    "status": "PASS",
    "message": "VOLTAGE正常",
    "data": {
        "voltage": 220
    }
}

assert result["status"] == "FAIL"