# log = """
# DEVICE = SN001
# TEST = POWER
# RESULT = FAIL
# ERROR = Voltage_High
# """

# log = log.replace(" = ", "=")

# print(log)

raw_log = """
DEVICE = SN001
TEST = POWER
RESULT = FAIL
ERROR = Voltage_High
"""

clean_log = raw_log.replace(" = ", "=")

print(clean_log)