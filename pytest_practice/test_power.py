from data_structure import check_value

def test_voltage_normal():
    result = check_value(
        "TEST=POWER VOLTAGE=220 CURRENT=5",
        "VOLTAGE",
        240,
        200
    )

    assert result["status"] == "PASS"
    #assert result["status"] == "FAIL"