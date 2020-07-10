from ts3audiobot_api.ts3audiobot import TS3AudioBot

ts3audiobot = TS3AudioBot("45.132.125.235", "xn7q4NRcECG/sJoR45EW7EgtzoA=:s8c5okNYzRH8znlLsrHzrZL4D6v7ypXg")

t = ts3audiobot.get_command_executor()

connect = t.connect_via_template("302bd9ca-4361-4dbe-950f-1d994be5ccb5")

print(connect)

print(connect["Id"])

