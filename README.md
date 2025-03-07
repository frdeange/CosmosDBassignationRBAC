# CosmosDB Assignation RBAC

This project is designed to manage Role-Based Access Control (RBAC) assignments for Azure Cosmos DB. It includes scripts and configurations to facilitate the assignment of roles to users and services.

## Prerequisites

Before you can use this project, you need to have the following:

- An Azure account with the necessary permissions to manage RBAC assignments.
- Azure CLI installed on your local machine (if not using the devContainer).

## Using the devContainer

This project includes a devContainer configuration that sets up a development environment with all necessary dependencies. To use the devContainer:

1. Open the project in Visual Studio Code.
2. When prompted, reopen the project in the devContainer.
3. The devContainer will automatically install all required tools and dependencies.

## Using without the devContainer

If you prefer to use your local environment instead of the devContainer, you need to install the Azure CLI and log in to your Azure account:

1. Install the Azure CLI by following the instructions [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
2. Open a terminal and run the following command to log in to your Azure account:
    ```sh
    az login
    ```
3. Follow the instructions to complete the login process.

## Updating Configuration

Before running the project, make sure to rename the `.dev.fake` file to `.dev` and update it with your own information. This file contains configuration settings that are necessary for the scripts to run correctly.

To obtain the service principal ID or user ID, you can use the following commands:

- To get the service principal ID:
    ```sh
    az ad sp list --display-name <service-principal-name> --query "[].appId" -o tsv
    ```

- To get the user ID:
    ```sh
    az ad user show --id <user-email> --query "objectId" -o tsv
    ```

## Running the Project

Once you have set up your environment (either using the devContainer or your local environment), you can run the project scripts to manage RBAC assignments.

1. Open a terminal in the project directory.
2. Run the desired script to manage RBAC assignments.

## Additional Information

For more detailed information on how to use the scripts and manage RBAC assignments, please refer to the individual script documentation and comments within the code.

