import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

smallest = w.clusters.select_node_type(local_disk=True)

created = w.instance_pools.create(instance_pool_name=f'sdk-{time.time_ns()}', node_type_id=smallest)

w.instance_pools.edit(instance_pool_id=created.instance_pool_id,
                      instance_pool_name=f'sdk-{time.time_ns()}',
                      node_type_id=smallest)

# cleanup
w.instance_pools.delete(delete=created.instance_pool_id)