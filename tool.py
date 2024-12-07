import requests
import argparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# List of possible GraphQL paths
GRAPHQL_PATHS = [
    "/graphql", "/gql", "/graphiql", "/v1/graphql", "/api/graphql", "/graphql/api",
    "/query", "/playground", "/admin/graphql", "/public/graphql", "/backend/graphql",
    "/user/graphql", "/graphql/v2", "/graphql/schema", "/graphql/console",
    "/graphql/debug", "/graphql/ide", "/graphql-playground", "/graph", "/graphqldoc",
    "/api/v2/graphql", "/api/v1/graphql", "/api/graph", "/graphql-explorer",
    "/graphql/query", "/graphql-endpoint", "/api/graphql-query", "/graphqlapi",
    "/graphqlproxy", "/graphql-backend", "/gql-api", "/gql/v1", "/graphql/v1",
    "/graphql/v3", "/graphql-endpoint", "/graphql-admin", "/graph-query"
]

def scan_url(url, output_file=None):
    """Scan a single URL for GraphQL endpoints."""
    if not url.startswith("http://") and not url.startswith("https://"):
        url = f"https://{url.strip()}"

    results = []
    for path in GRAPHQL_PATHS:
        graphql_url = f"{url.rstrip('/')}{path}"
        try:
            # Send a POST request to the GraphQL endpoint
            response = requests.post(graphql_url, json={"query": "{ __schema { queryType { name } } }"}, timeout=5)

            # Check the response
            if response.status_code == 200:
                result = f"[FOUND] GraphQL endpoint detected at: {graphql_url}"
                print(f"{Fore.GREEN}{result}")
                results.append(result)
            elif response.status_code in [403, 405]:
                result = f"[POSSIBLE] Possible GraphQL endpoint at: {graphql_url} (HTTP {response.status_code})"
                print(f"{Fore.YELLOW}{result}")
                results.append(result)
            else:
                result = f"[FAILED] No GraphQL endpoint at: {graphql_url} (HTTP {response.status_code})"
                print(f"{Fore.RED}{result}")
        except requests.exceptions.RequestException as e:
            result = f"[ERROR] Could not connect to: {graphql_url} - {e}"
            print(f"{Fore.RED}{result}")
            results.append(result)

    # Write results to output file if specified
    if output_file:
        with open(output_file, "w") as outfile:
            for result in results:
                outfile.write(result + "\n")

def detect_graphql(input_file, output_file):
    """Scan a list of URLs for GraphQL endpoints."""
    try:
        # Open the file containing URLs
        with open(input_file, 'r') as file:
            urls = file.read().splitlines()

        for url in urls:
            scan_url(url, output_file)
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] Input file '{input_file}' not found.")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GraphQL Endpoint Detection Tool")
    parser.add_argument("-l", "--list", help="Input file containing URLs (one per line)")
    parser.add_argument("-u", "--url", help="Single URL to scan")
    parser.add_argument("-o", "--output", help="Output file to save results")
    
    args = parser.parse_args()

    if args.url and args.list:
        print(f"{Fore.RED}[ERROR] You cannot specify both a single URL and a list of URLs. Choose one.")
    elif args.url:
        scan_url(args.url, args.output)
    elif args.list:
        if not args.output:
            print(f"{Fore.RED}[ERROR] You must specify an output file when scanning a list of URLs.")
        else:
            detect_graphql(args.list, args.output)
    else:
        print(f"{Fore.RED}[ERROR]use (-h) for help, You must specify either a single URL (-u) or a list of URLs (-l).")
