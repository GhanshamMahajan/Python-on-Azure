from azure.mgmt.subscription import SubscriptionClient
from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
import os

exceptrglist = ["ATLASSIAN-PROD-EMEA-IAAS-PRIMARY", "ATLASSIAN-TEST-EMEA-IAAS-PRIMARY", "GDS-DEV-EMEA-IAAS-PRIMARY", "GDS-PROD-EMEA-IAAS-PRIMARY"]

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
        #print(subscription_id)
        compute_client = ComputeManagementClient(credential, subscription_id)
        vm_list = compute_client.virtual_machines.list_all()
        for vm_general in vm_list:
            general_view = vm_general.id.split("/")
            #print(general_view[4])
            if (general_view[4] == exceptrglist[0]) or (general_view[4] == exceptrglist[1]) or (general_view[4] == exceptrglist[2] or (general_view[4] == exceptrglist[3])):
                pass
            else:
                resource_group = general_view[4]
                vm_name = general_view[-1]
                vm = compute_client.virtual_machines.get(resource_group, vm_name, expand='instanceView')
                if vm.storage_profile.os_disk.os_type == "Linux":
                    vm_status = compute_client.virtual_machines.instance_view(resource_group, vm.name).statuses[1].code
                    if vm_status == "PowerState/running":
                        print(resource_group)
                        print(vm.name)
                        print(vm.location)
                        print(vm.storage_profile.os_disk.os_type)
