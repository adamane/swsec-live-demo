import logging
from pyspiffe.workloadapi.default_workload_api_client import DefaultWorkloadApiClient
from pyspiffe.workloadapi.exceptions import FetchX509SvidError

def main():
    logging.basicConfig(level=logging.INFO)

    # Initialisiere den SPIFFE Workload API Client
    client = DefaultWorkloadApiClient(spiffe_endpoint_socket='/run/spire/sockets/spire-agent.sock')

    try:
        # Rufe das X.509 SVID ab
        svids = client.fetch_x509_svid()
        for svid in svids:
            logging.info(f"Got SPIFFE ID: {svid.spiffe_id}")
            logging.info(f"Certificates: {svid.cert_chain}")
    except FetchX509SvidError as e:
        logging.error(f"Error fetching X.509 SVID: {e}")
    finally:
        client.close()

if __name__ == '__main__':
    main()
