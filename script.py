import os
import argparse

# Set options
usage = "usage: python get_security_object_usage.py --name MyCustomRule [--edgerc ~/.edgerc] [--section default] [--accountSwitchKey <ask>] [--debug]"
parser = argparse.ArgumentParser(usage=usage)
parser.add_argument(
    "--akamai_client_token", action="store", dest="akamai_client_token", required=True, help="Akamai Client Token"
)
parser.add_argument(
    "--akamai_access_token", action="store", dest="akamai_access_token", required=True, help="Akamai Access Token"
)
parser.add_argument(
    "--akamai_client_secret", action="store", dest="akamai_client_secret", required=True, help="Akamai Client Secret"
)
parser.add_argument("--akamai_host", action="store", dest="akamai_host", required=True, help="Akamai Host")

args = parser.parse_args()

print(str(args))
