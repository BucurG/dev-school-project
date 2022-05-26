# Azure configuration

The next steps we took were some required configurations needed in order to be able to run the build pipeline in Azure DevOps.

The actions we performed were:
- Create an Ubuntu VM and configure Docker on it;
- Create an Azure Container Registry.

You can use the below resources to document about creating those resources:
- [Quickstart: Create a Linux virtual machine in the Azure portal](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal)
  > **NOTE:** The regions part might be tricky, depending on your account. You might have to do some trial and error here.
- [Install Docker using repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- [Quickstart: Create an Azure container registry using the Azure portal](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal)

> **NOTE:** Be careful to **always** create a resource group before performing anything! The clean-up is much more easier.