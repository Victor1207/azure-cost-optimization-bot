import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient

app = func.FunctionApp()

@app.function_name(name="cost_optimizer_timer")
@app.schedule(
    schedule="0 */5 * * * *",  # every 5 minutes
    arg_name="myTimer",
    run_on_startup=True
)
def cost_optimizer_timer(myTimer: func.TimerRequest) -> None:
    logging.info("Cost optimizer function started")

    # Authenticate using Managed Identity
    credential = DefaultAzureCredential()
    client = CostManagementClient(credential)

    # Subscription scope
    subscription_id = "8fb4ccc7-a8e3-4433-ae8f-29204aa114a9"
    scope = f"/subscriptions/{subscription_id}"

    # Cost query
    query = {
        "type": "Usage",
        "timeframe": "MonthToDate",
        "dataset": {
            "granularity": "None",
            "aggregation": {
                "totalCost": {
                    "name": "Cost",
                    "function": "Sum"
                }
            }
        }
    }

    # Execute cost query
    result = client.query.usage(scope=scope, parameters=query)

    if result.rows:
        cost = result.rows[0][0]
        logging.info(f"Current month Azure spend: €{cost}")
    else:
        logging.warning("No cost data returned")
