# Azure DevOps

Next, we created a pipeline in Azure DevOps which builds the Docker image and pushes it into the ACR we created earlier.
In order to do this, we performed the following:

- Configured the Ubuntu VM as a pipeline agent: [Azure Pipelines agents](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=browser);
- Created a Service Connection so that we have access from the pipeline to the ACR: [Manage service connections](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml);
- Set up our pipeline YAML which does the following:
  - performes login command to authenticate to the ACR;
  - performs build command to build the image based on our Dockerfile;
  - performs push command to push the image in our ACR.

> **NOTE:** Since you will be working in pairs, make sure you give your colleagues basic access to your Azure DevOps organization in order for them to make commits.