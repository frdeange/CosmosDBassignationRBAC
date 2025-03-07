import os
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set environment variables
resource_group = os.getenv("RESOURCE_GROUP_NAME")
account_name = os.getenv("COSMOS_ACCOUNT_NAME")
role_definition_id = os.getenv("ROLE_DEFINITION_ID")
principal_id = os.getenv("PRINCIPAL_ID")
principal_type = os.getenv("PRINCIPAL_TYPE")


# Build the command
command = [
    "az", "cosmosdb", "sql", "role", "assignment", "create",
    "--account-name", account_name,
    "--resource-group", resource_group,
    "--scope", "/",
    "--principal-id", principal_id,
    "--role-definition-id", role_definition_id
]

# If principal_type is set, add it to the command
if principal_type:
    command.extend(["--principal-type", principal_type])

# Execute the command
try:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print("Éxito:", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error:", e.stderr)
