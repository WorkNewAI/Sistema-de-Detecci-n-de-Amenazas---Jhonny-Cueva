#!/var/ossec/framework/python/bin/python3
import sys
import json
import requests

GLPI_URL = "poner su ip/apirest.php"
APP_TOKEN = "Poner el token aqui"
GLPI_USER = "glpi"
GLPI_PASS = "glpi"

def init_session():
    headers = {"App-Token": APP_TOKEN, "Content-Type": "application/json"}
    r = requests.get(f"{GLPI_URL}/initSession",
                      auth=(GLPI_USER, GLPI_PASS),
                      headers=headers)
    return r.json().get("session_token")

def create_ticket(session_token, title, content):
    headers = {
        "App-Token": APP_TOKEN,
        "Session-Token": session_token,
        "Content-Type": "application/json"
    }
    payload = {
        "input": {
            "name": title,
            "content": content,
            "urgency": 5,
            "type": 1
        }
    }
    r = requests.post(f"{GLPI_URL}/Ticket", headers=headers, json=payload)
    return r.json()

def main():
    alert_file = sys.argv[1]
    with open(alert_file) as f:
        alert_json = json.load(f)

    rule_desc = alert_json.get("rule", {}).get("description", "Alerta Wazuh")
    agent_name = alert_json.get("agent", {}).get("name", "desconocido")
    full_log = alert_json.get("full_log", "Sin detalle")

    title = f"[Wazuh] {rule_desc} - Agente: {agent_name}"
    content = f"Alerta generada por Wazuh:\n\n{full_log}"

    token = init_session()
    if token:
        result = create_ticket(token, title, content)
        print(json.dumps(result))

if __name__ == "__main__":
    main()
