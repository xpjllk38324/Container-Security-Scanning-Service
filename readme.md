Container security scanning service
Team: 3-4
Complexity: Complex
Size: Medium

The GitOps process implemented by the framework implies that user code is deployed to and run on the k8s cluster without any manual checking by the framework administrators. The project aims at modeling the security threats resulting from such an approach, developing a container vulnerability scanning service integrated into the CI/CD pipeline of the framework and its container registry, and reporting on the results for both developers and administrators.
