from flask import Flask, Response
from prometheus_client import Gauge, CollectorRegistry, generate_latest
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    registry = CollectorRegistry()

    # Définition des métriques
    total_queries = Gauge('bind_total_queries', 'Total DNS queries', registry=registry)
    nx_domains = Gauge('bind_nxdomain_responses', 'NXDOMAIN responses', registry=registry)

    try:
        r = requests.get("http://bind9:8053/", timeout=2)
        if r.status_code == 200:
            xml_data = ET.fromstring(r.text)
            for counter in xml_data.iter('counter'):
                name = counter.attrib.get('name')
                value = int(counter.text or 0)
                if name == 'QrySuccess':
                    total_queries.set(value)
                elif name == 'QryNXDOMAIN':
                    nx_domains.set(value)
    except Exception as e:
        print(f"Erreur: {e}")

    return Response(generate_latest(registry), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9119)
