from azure.mgmt.subscription import SubscriptionClient
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os

credential = AzureCliCredential()
client = SubscriptionClient(credential)
subs = [sub.as_dict() for sub in client.subscriptions.list()]

for subcription in subs:
    str(subcription)
    #print("subcription", str(subcription))
    # split dictionary into keys and values
    keys, values = zip(*subcription.items())
    # printing keys and values separately
    #print("keys : ", str(keys))
    #print("values : ", str(values))

    subscription_id = values[1]
    #subscription_id = subcription.get("")
    #print(subscription_id)
    if subscription_id == subscription_id:
        resource_client = ResourceManagementClient(credential, subscription_id)
        resource_list = resource_client.resources.list()
        print(resource_list)
        column_width = 75
        #print("Resource".ljust(column_width) + "Type".ljust(column_width) + "Id".ljust(column_width))
        print("Resource".ljust(column_width) + "Location".ljust(column_width) + "Type".ljust(column_width) + "Id".ljust(column_width))
        print("-" * (column_width * 5))
        for resource in list(resource_list):
            if (resource.type == "Microsoft.Web/sites") and (
                    (resource.kind == "functionapp") or (resource.kind == "functionapp,linux")):
                print(f"{resource.name:<{column_width}}{resource.location:<{column_width}}{resource.type:<{column_width}}{resource.id:<{column_width}}")
