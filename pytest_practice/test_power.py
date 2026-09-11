from data_structure import check_value
import pytest

@pytest.mark.parametrize(
    "log, expected",
    [
        ("TEST=POWER VOLTAGE=220 CURRENT=5", "PASS"),
        ("TEST=POWER VOLTAGE=199 CURRENT=5", "FAIL"),
        ("TEST=POWER VOLTAGE=200 CURRENT=5", "PASS"),
        ("TEST=POWER VOLTAGE=240 CURRENT=5", "PASS"),
        ("TEST=POWER VOLTAGE=241 CURRENT=5", "FAIL"),
        #("TEST=POWER VOLTAGE=241 CURRENT=5", "PASS"),
    ],
    ids=[
        "正常220V",
        "低于200V",
        "边界200V",
        "边界240V",
        "高于240V"
    ]
)

def test_voltage_normal(log, expected):
    result = check_value(
        log,
        "VOLTAGE",
        240,
        200
    )
    assert result["status"] == expected
    

@pytest.mark.parametrize(
    "log, expected",
    [
        ("TEST=POWER VOLTAGE=", "FAIL"),
        ("TEST=POWER VOLTAGE=abc", "FAIL"),
        ("TEST=POWER", "FAIL"),
    ]
)

def test_voltage_invalid(log, expected):
    result = check_value(
        log, 
        "VOLTAGE",
        240,
        200
    )
    assert result["status"] == expected

# def test_voltage(log, expected):
#     result = check_value(
#         log,
#         "VOLTAGE",
#         240,
#         200
#         )
#     assert result["status"] == expected

# def test_voltage_normal():
#     result = check_value(
#         "TEST=POWER VOLTAGE=220 CURRENT=5",
#         "VOLTAGE",
#         240,
#         200
#     )

#     assert result["status"] == "PASS"
#     #assert result["status"] == "FAIL"

# def test_voltage_low():
#     result = check_value(
#         "TEST=POWER VOLTAGE=199 CURRENT=5",
#         "VOLTAGE",
#         240,
#         200
#     )

#     assert result["status"] == "FAIL"

# def test_voltage_min():
#     result = check_value(
#         "TEST=POWER VOLTAGE=200 CURRENT=5",
#         "VOLTAGE",
#         240,
#         200
#     )

#     assert result["status"] == "PASS"

# def test_voltage_max():
#     result = check_value(
#         "TEST=POWER VOLTAGE=240 CURRENT=5",
#         "VOLTAGE",
#         240,
#         200
#     )

#     assert result["status"] == "PASS"

# def test_voltage_high():
#     result = check_value(
#         "TEST=POWER VOLTAGE=241 CURRENT=5",
#         "VOLTAGE",
#         240,
#         200
#     )

#     assert result["status"] == "FAIL"

# def test_voltage_empty():
#     result = check_value(
#         "TEST=POWER VOLTAGE=",
#         "VOLTAGE",
#         240,
#         200
#     )

#     assert result["status"] == "FAIL"

# def test_voltage_invalid_format():
#     result = check_value(
#         "TEST=POWER VOLTAGE=abc",
#         "VOLTAGE",
#         240,
#         200
#     )

#     assert result["status"] == "FAIL"

# def test_voltage_missing():
#     result = check_value(
#         "TEST=POWER",
#         "VOLTAGE",
#         240,
#         200        
#     )

#     assert result["status"] == "FAIL"