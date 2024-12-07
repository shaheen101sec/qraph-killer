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

def detect_graphql(input_file, output_file):
    try:
        # Open the file containing URLs
        with open(input_file, 'r') as file:
            urls = file.read().splitlines()

        # Prepare to write results to the output file
        with open(output_file, 'w') as outfile:
            print("Testing URLs for GraphQL endpoints...\n")
            for url in urls:
                if not url.startswith("http://") and not url.startswith("https://"):
                    url = f"https://{url.strip()}"

                for path in GRAPHQL_PATHS:
                    graphql_url = f"{url.rstrip('/')}{path}"
                    try:
                        # Send a POST request to the GraphQL endpoint
                        response = requests.post(graphql_url, json={"query": "{ __schema { queryType { name } } }"}, timeout=5)

                        # Check the response and write results to the output file
                        if response.status_code == 200:
                            result = f"[FOUND] GraphQL endpoint detected at: {graphql_url}"
                            print(f"{Fore.GREEN}{result}")
                            outfile.write(result + '\n')
                        elif response.status_code in [403, 405]:
                            result = f"[POSSIBLE] Possible GraphQL endpoint at: {graphql_url} (HTTP {response.status_code})"
                            print(f"{Fore.YELLOW}{result}")
                            outfile.write(result + '\n')
                        else:
                            result = f"[FAILED] No GraphQL endpoint at: {graphql_url} (HTTP {response.status_code})"
                            print(f"{Fore.RED}{result}")
                    except requests.exceptions.RequestException as e:
                        result = f"[ERROR] Could not connect to: {graphql_url} - {e}"
                        print(f"{Fore.RED}{result}")
                        outfile.write(result + '\n')

    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] Input file '{input_file}' not found.")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GraphQL Endpoint Detection Tool")
    parser.add_argument("-l", "--list", required=True, help="Input file containing URLs (one per line)")
    parser.add_argument("-o", "--output", required=True, help="Output file to save results")

    args = parser.parse_args()
    detect_graphql(args.list, args.output)
