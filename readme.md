<div align="center"> <img src="Ιmages/header.png"> </div>
</br>
<sup>Image based on: Expert, G. (2024, June 27). Container Security Scanning: vulnerabilities, risks and tooling. GitGuardian Blog - Code Security for the DevOps Generation. https://blog.gitguardian.com/container-security-scanning-vulnerabilities-risks-and-tooling/ </sup>

# Container Security Scanning Service
This project is a part of the Advanced Software Design course at Higher School of Economics.  

## Project Description
The GitOps process implemented by the framework implies that user code is deployed to and run on the k8s cluster without any manual checking by the framework administrators. The project aims at modeling the security threats resulting from such an approach, developing a container vulnerability scanning service integrated into the CI/CD pipeline of the framework and its container registry, and reporting on the results for both developers and administrators.

## Members of "Data Visioners" Team
Pujun Xie

Adam Terlo

Syed Ali

## Table of Contents

- [Behavior Diagram](/Behavior%20Diagram)
- [Class Model](/Class%20Model)
- [Interaction Analysis](/Interaction%20Analysis)
- [Practices](/Practices)
- [Product Definition](/Product%20Definition)
- [Product Scope](/Product%20Scope)
- [StoryMap](/StoryMap)
- [Use Cases](/Use%20Cases)




## Overview
- **Members:** 3-4
- **Complexity:** Complex
- **Size:** Medium

## Objectives
This project aims to:
- Model the security threats resulting from the automated deployment process.
- Develop a container vulnerability scanning service that is integrated into the CI/CD pipeline of the framework and its container registry.
- Provide reporting on the results for both developers and administrators.

## Feature list:
1. Configure container scanning rules. Users can configure personalized settings for the container vulnerability scanning tools.
2. Perform container scanning tasks. Users can perform container scanning task according to the configured rules.
3. Assess container security. According to the result of the container’s scanning, the container vulnerability scanning service will assess container security.
4. Configure container security assessment rules. Users can set custom policy for the container security assessment.
5. Export container scan reports. Users can generate and get detailed reports containing scan results, vulnerability details and more.
6. Notify and alert. Users can get notifications and alerts in real time via email, SMS, and other channels.
7. Configure notify and alert rules. Users can set custom notify and alert rules, such as immediate notification when a high-risk vulnerability is detected.
8. Update of vulnerability database. Users can update the vulnerability database which container scanning tools use.

## Constraints:
1. Container scan engine needs to quickly and accurately identify security vulnerabilities and bad practices in containers.
2. Container scanning service needs to be integrated with existing CI/CD systems, which requires services with flexible architectures capable of supporting multiple integration approaches.
3. Container scanning service needs to ensure the security and privacy of user data. The service needs to take appropriate encryption measures to protect sensitive information during data transmission and storage.


## Directory layout

```
.
├── Behavior Diagram
│		 ├── Behavior Diagram Developer.svg
│		 ├── Behavior Diagram Developer.xml
│		 └── readme.md
├── Class Model
│		 ├── Class Model.gv
│		 ├── Class Model.png
│		 ├── Class Model.svg
│		 └── readme.md
├── Interaction analysis
│		 ├── Interaction Analysis.png
│		 └── readme.md
├── Practices
│		 ├── Task4 Images
│		 │		 └── ... .svg
│		 ├── Task4.docx
│		 ├── Task4.pdf
│		 └── readme.md
├── Product Definition
│		 ├── Product Definition.pdf
│		 ├── Product Definition.pptx
│		 └── readme.md
├── Product Scope
│		 ├── Product Scope.pdf
│		 └── readme.md
├── StoryMap
│		 ├── StoryMap.svg
│		 ├── StoryMap.xml
│		 └── readme.md
├── Use Cases
│		 ├── Use Cases Diagram.svg
│		 ├── Use Cases Diagram.xml
│		 ├── Use Cases Report.pdf
│		 └── readme.md
├── readme.md
└── Ιmages
    └── header.png

```

## ✅ First Module Presentation
<a href="https://docs.google.com/presentation/d/1jYT2z8IW7d-pIBxl-vZMGDVw9JMwZKOG/edit?usp=sharing&ouid=114089356352736591781&rtpof=true&sd=true"> Presentation </a>
