# qraph-killer

# GraphQL Detection Tool

## Overview

The **GraphQL Endpoint Detection Tool** is a Python script designed to identify potential GraphQL endpoints for a given list of URLs. It supports multiple commonly used GraphQL endpoint paths and logs the results to an output file for further analysis.

This tool can be useful for security researchers, developers, and penetration testers seeking to identify GraphQL endpoints in a web application.

---

## Features

- Detects GraphQL endpoints across various standard and custom paths.
- Supports multiple input URLs provided via a text file.
- Outputs results to a specified file with detailed status information.
- Handles common HTTP response codes and timeouts gracefully.
- Easy to customize and extend with additional GraphQL paths.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shaheen101sec/qraph-killer.git
   cd graphql-endpoint-detector
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Dependencies**:
   - `requests`: For making HTTP requests.
   - `colorama`: For colored terminal output.

---

## Usage

Run the script with the following command:
```bash
python3 tool.sh -l <input_file> -o <output_file>
```

### Parameters:
- `-l` or `--list`: Path to the input file containing URLs (one URL per line).
- `-o` or `--output`: Path to the output file where results will be saved.

### Example:
```bash
python3 tool.sh -l sites.txt -o output.txt
```

---

## Input Format

The input file should be a text file containing one URL per line:
```
example.com
http://another-example.com
https://secure-example.org
```

---

## Output Format

The script generates an output file containing results for each tested URL and path combination, with the following statuses:
- **[FOUND]**: GraphQL endpoint detected and responding successfully.
- **[POSSIBLE]**: A potential GraphQL endpoint detected (e.g., HTTP 403 or 405).
- **[FAILED]**: No GraphQL endpoint found at the specified path.
- **[ERROR]**: Connection errors or timeouts.

Example output:
```
[FOUND] GraphQL endpoint detected at: https://example.com/graphql
[POSSIBLE] Possible GraphQL endpoint at: https://example.com/api/graphql (HTTP 403)
[FAILED] No GraphQL endpoint at: https://example.com/query (HTTP 404)
[ERROR] Could not connect to: https://another-example.com/graphql - Timeout
```

---

## Supported GraphQL Paths

you can add more paths in the code if you want,
The tool tests the following paths by default:
```
/graphql
/gql
/graphiql
/v1/graphql
/api/graphql
/graphql/api
/query
/playground
/admin/graphql
/public/graphql
/backend/graphql
/user/graphql
/graphql/v2
/graphql/schema
/graphql/console
/graphql/debug
/graphql/ide
/graphql-playground
/graph
/graphqldoc
/api/v2/graphql
/api/v1/graphql
/api/graph
/graphql-explorer
/graphql/query
/graphql-endpoint
/api/graphql-query
/graphqlapi
/graphqlproxy
/graphql-backend
/gql-api
/gql/v1
/graphql/v1
/graphql/v3
/graphql-endpoint
/graphql-admin
/graph-query
```

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you'd like to:
- Suggest additional GraphQL paths.
- Report bugs or issues.
- Improve the script or documentation.

---

Have a nice day !

---

## Disclaimer

This tool is intended for lawful use only. Ensure you have proper authorization before scanning or testing any URLs. The developers are not responsible for misuse of this tool.
