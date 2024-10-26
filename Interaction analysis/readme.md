# Interaction Analysis 
<img src="./Interaction Analysis.png">
<sup> 🔍 <a href="https://docs.google.com/spreadsheets/d/1PmeDejna0FrRl6HxcAxIUhxDMOHLtNmbOyaGHdDB_0o/edit?usp=sharing">Table source</a> </sup>

-

In the analysis we outline cooperative actions and roles in maintaining container security across key functions like scanning, vulnerability management, alerting, etc. DevOps Engineers, Information Security Engineers, and Developers each work within these functions, engaging with core classes for a unified security process.

-

Container scanning rules are managed collaboratively, with DevOps and Security Engineers primarily interacting with `ContainerScanRule` to set consistent image assessment criteria. Scanning tasks, handled by `ScanTask` and `ScanningService`, involve all roles in initiating scans and consolidating vulnerability findings.

-

Assessment and reporting are managed through `AssessmentRule` and `ScanResult`, ensuring compliance checks and comprehensive vulnerability insights for all roles. Alerts and notifications, powered by `AlertService`, keep stakeholders informed of critical security issues, while configurable rules for alerts help target notifications effectively.

-

The `VulnerabilityDatabase` class, crucial for tracking vulnerabilities, enables roles to manage data entries for ongoing security maintenance. These interactions streamline container scanning and assessment as part of the CI/CD pipeline, supporting automated responses to security threats.

## Details
Author: Adam Terlo  
Reviewed by: Data Visioners Team  