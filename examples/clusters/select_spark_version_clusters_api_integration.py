from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

latest = w.clusters.select_spark_version(latest=True)
