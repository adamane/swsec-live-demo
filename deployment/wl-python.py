import logging
from spiffe import WorkloadApiClient, JwtSvid, WorkloadApiError

def main():
    logging.basicConfig(level=logging.INFO)

    # Der Workload API Socket-Pfad (standardmäßig im SPIRE Agent-Pod geordnet)
    workload_api_socket = '/run/spire/sockets/spire-agent.sock'

    # Erstellen des Workload API Clients
    try:
        client = WorkloadApiClient(
            spiffe_socket_path=workload_api_socket  # Path zum SPIFFE Workload API Socket
        )
    except Exception as e:
        logging.error(f"Fehler beim Verbinden mit der Workload API: {e}")
        return

    try:
        # Audience (Zielgruppe) definieren
        audience = ['https://vault2.adamane.dev']

        # Abrufen eines JWT-SVID mit der angegebenen Audience
        jwt_svid = client.fetch_jwt_svid(audience=audience)
        
        if isinstance(jwt_svid, JwtSvid):
            # SPIFFE-ID und JWT-Tokens protokollieren
            logging.info(f"Erhaltene SPIFFE-ID: {jwt_svid.spiffe_id()}")
            logging.info(f"JWT-Token: {jwt_svid.token_string()}")
        else:
            logging.error("Kein gültiges JWT-SVID abgerufen.")

    except WorkloadApiError as e:
        logging.error(f"Fehler beim Abrufen des JWT-SVIDs: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    main()
