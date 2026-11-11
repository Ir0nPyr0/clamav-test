<!-- ********************************************************************************
 * Copyright (c) 2026 Schwarz Digits Cloud GmbH & Co. KG
 *
 * This program and the accompanying materials are made available under the
 * terms of the Creative Commons Attribution-ShareAlike 4.0 International Public License
 * which is available at https://creativecommons.org/licenses/by-sa/4.0/.
 *
 * SPDX-License-Identifier: CC-BY-SA-4.0
 *
 * Contributors:
 *   Andy Riexinger - initial contribution
 ******************************************************************************* -->
 
# SML 3 — Data Sovereignty

*Data sovereignty measures the control parameters established over data assets throughout their life cycle.*

---

### SML 3.CO 1 Access Control
**Objective:** To ensure customers retain control over access to their data.  
*Sovereignty Contribution:* Ensures that customers can independently define and enforce access to their data without reliance on the provider. Prevents unauthorized and privileged provider access and enables full control through technical enforcement mechanisms, including customer-controlled cryptographic keys.

#### SML 3.CO 1.C 1 (Contractual)
*   **Scope:** Service Provider 
*   **Service Type:** All
*   Contracts ensure that the customer retains sole authority to define, grant, modify, and revoke access rights to their data.
*   **SML 3.CO 1.C 1.Q 1:** Does the contract explicitly grant the customer sole authority to define, grant, modify, and revoke access to their data?

#### SML 3.CO 1.C 2 (Governance and Operations)
*   **Scope:** Service Provider 
*   **Service Type:** All
*   Policies and procedures ensure that access to customer data is restricted to authorized entities and is not performed without explicit customer authorization.
*   **SML 3.CO 1.C 2.Q 1:** Are policies and procedures in place to ensure that access to customer data is restricted and only performed with explicit customer authorization?

#### SML 3.CO 1.C 3 (Technical)
*   **Scope:** Client-Facing Service 
*   **Service Type:** SaaS, Managed Service, AI Service
*   Customers use role-based and/or attribute-based access control models to define, assign, and enforce access rights to their data.
*   **SML 3.CO 1.C 3.Q 1:** Can customers independently define and enforce access rights to their data using role-based or attribute-based access control mechanisms?

#### SML 3.CO 1.C 4 (Technical)
*   **Scope:** Client-Facing Service 
*   **Service Type:** SaaS, AI Service, Managed Service
*  Access to customer data is technically protected through cryptographic mechanisms, making access impossible without use of the corresponding cryptographic keys.
*   **SML 3.CO 1.C 4.Q 1:** Is access to customer data technically enforced through encryption mechanisms that prevent access without the corresponding cryptographic keys?

#### SML 3.CO 1.C 5 (Technical)
*   **Scope:** Service Provider 
*   **Service Type:** PaaS, SaaS, AI Service, Managed Service
*   Customers can independently obtain, manage, and control cryptographic keys.
*   **SML 3.CO 1.C 5.Q 1:** Can customers independently manage, rotate, and control cryptographic keys associated with their data?

#### SML 3.CO 1.C 6 (Technical)
*   **Scope:** Underlying Service 
*   **Service Type:** IaaS, PaaS
*   The underlying services support customer-controlled key management and access control capabilities required to enforce customer-defined access restrictions.
*   **SML 3.CO 1.C 6.Q 1:** Do the underlying services support customer-controlled key management and access control capabilities required to enforce customer-defined access restrictions?

---

### SML 3.CO 2 Portability
**Objective:** To enable customers to access, retrieve, and export their data in a usable and portable manner.    
*Sovereignty Contribution:* Ensures that customers can retrieve and transfer their data without dependency on the provider, enabling effective data portability and preventing vendor lock-in.

#### SML 3.CO 2.C 1 (Contractual)
*   **Scope:** Service Provider 
*   **Service Type:** All
*   The contract ensures that the customer can access, retrieve, and export their data at any time without undue restrictions or delays.
*   **SML 3.CO 2.C 1.Q 1:** Does the contract ensure that the customer can access, retrieve, and export their data at any time without undue restrictions or delays?

#### SML 3.CO 2.C 2 (Governance and Operations)
*   **Scope:** Service Provider 
*   **Service Type:** All
*   Processes exist that allow customers to retrieve and export data including all relevant datasets required for continued use.
*   **SML 3.CO 2.C 2.Q 1:** Are there defined and implemented processes ensuring that customer data can be retrieved and exported in a complete and consistent manner?

#### SML 3.CO 2.C 3 (Technical)
*   **Scope:** Client-Facing Service 
*   **Service Type:** Managed Service, AI Service, SaaS
*   The service provides mechanisms that allow customers to access and retrieve their data independently via user interfaces and/or APIs.
*   **SML 3.CO 2.C 3.Q 1:** Can customers retrieve and/or export their data via a defined process?

#### SML 3.CO 2.C 4 (Technical)
*   **Scope:** Client-Facing Service 
*   **Service Type:** Managed Service, AI Service, SaaS
*   Backup systems and data duplication locations are restricted to jurisdictions listed in the AJL.
*   **SML 3.CO 2.C 4.Q 1:** Are backup systems and data duplication locations restricted to jurisdictions listed in the AJL?

#### SML 3.CO 2.C 5 (Technical)
*   **Scope:** Client-Facing Service 
*   **Service Type:** Managed Service, AI Service, SaaS
*   Complete and correct data export is ensured to enable effective reuse of the data.
*   **SML 3.CO 2.C 5.Q 1:** Can a complete and correct data export be ensured?

#### SML 3.CO 2.C 6 (Technical)
*   **Scope:** Underlying Service 
*   **Service Type:** PaaS, IaaS
*   The underlying services support data extraction and transfer capabilities required to enable customer-driven data portability.
*   **SML 3.CO 2.C 6.Q 1:** Do the underlying services support data extraction and transfer capabilities required to enable customer-driven data portability?

---

### SML 3.CO 3 Usage Control
**Objective:** To ensure customer data is only processed and used for purposes explicitly defined and authorized by the customer.  
*Sovereignty Contribution:* Ensures that customer data is not used beyond customer-defined purposes, preventing unauthorized processing and maintaining full control over how data is utilized.

#### SML 3.CO 3.C 1 (Contractual)
*   **Scope:** Service Provider 
*   **Service Type:** All
*   The contract ensures that customer data is only processed and used for purposes explicitly defined and authorized by the customer.
*   **SML 3.CO 3.C 1.Q 1:** Does the contract explicitly restrict the processing and use of customer data to purposes defined and authorized by the customer?

#### SML 3.CO 3.C 2 (Governance and Operations)
*   **Scope:** Service Provider 
*   **Service Type:** All
*   The provider implements and enforces policies and procedures ensuring that customer data is not accessed or processed for purposes beyond those authorized by the customer.
*   **SML 3.CO 3.C 2.Q 1:** Are there enforced policies and procedures ensuring that customer data is not processed or used beyond authorized purposes?

#### SML 3.CO 3.C 3 (Technical)
*   **Scope:** Client-Facing Service 
*   **Service Type:** Managed Service, AI Service, SaaS
*   The service ensures that data processing activities are limited to configured and authorized purposes and cannot be executed outside of these defined constraints.
*   **SML 3.CO 3.C 3.Q 1:** Does the service ensure that data processing activities are restricted to configured and authorized purposes?

---

### SML 3.CO 4 Integrity
**Objective:** To ensure that customer data is protected against unauthorized modification or deletion.   
*Sovereignty Contribution:* Ensures that customer data cannot be altered or deleted without authorization, preserving data integrity and preventing unauthorized or provider-driven modifications.

#### SML 3.CO 4.C 1 (Contractual)
*   **Scope:** Service Provider 
*   **Service Type:** All
*   The contract ensures that customer data cannot be modified or deleted without authorization as defined by the customer.
*   **SML 3.CO 4.C 1.Q 1:** Does the contract explicitly ensure that customer data cannot be modified or deleted without customer-defined authorization?

#### SML 3.CO 4.C 2 (Governance and Operations)
*   **Scope:** Service Provider 
*   **Service Type:** All
*   Policies and procedures exist ensuring that all modifications and deletions of customer data are authorized, traceable and controlled.
*   **SML 3.CO 4.C 2.Q 1:** Are there enforced policies and procedures ensuring that all data modification and deletion activities are authorized, controlled, and traceable?

#### SML 3.CO 4.C 3 (Technical)
*   **Scope:** Client-Facing Service 
*   **Service Type:** SaaS, AI Service, Managed Service
*   The service ensures that all data modification and deletion actions are logged and regularly reviewed.
*   **SML 3.CO 4.C 3.Q 1:** Are all changes to and deletions of data logged and regularly monitored?

#### SML 3.CO 4.C 4 (Technical)
*   **Scope:** Client-Facing Service 
*   **Service Type:** SaaS, AI Service, Managed Service
*   The service provides mechanisms to protect data integrity, including versioning, immutability, or recovery capabilities to prevent or mitigate unauthorized changes or deletions.
*   **SML 3.CO 4.C 4.Q 1:** Does the service provide mechanisms such as versioning, immutability, or recovery capabilities to prevent or mitigate unauthorized data changes or deletions?

#### SML 3.CO 4.C 5 (Technical)
*   **Scope:** Underlying Service 
*   **Service Type:** IaaS, PaaS
*   The underlying service supports mechanisms for ensuring data integrity and preventing unauthorized modification or deletion.
*   **SML 3.CO 4.C 5.Q 1:** Does the underlying service support mechanisms to ensure data integrity and prevent unauthorized modification or deletion?

---

### Mapping of the Objectives to the corresponding Sovereignty Maturity Level

| ID | Initial | Managed | Advanced | Future-Proof |
|:---:|:---:|:---:|:---:|:---:|
| SML 3.CO 1.C 1 | x | x | x | x |
| SML 3.CO 1.C 2 |   | x | x | x |
| SML 3.CO 1.C 3 |   |   | x | x |
| SML 3.CO 1.C 4 |   |   | x | x |
| SML 3.CO 1.C 5 |   |   |   | x |
| SML 3.CO 1.C 6 |   |   |   | x |
| SML 3.CO 2.C 1 | x | x | x | x |
| SML 3.CO 2.C 2 |   | x | x | x |
| SML 3.CO 2.C 3 |   |   | x | x |
| SML 3.CO 2.C 4 |   |   | x | x |
| SML 3.CO 2.C 5 |   |   | x | x |
| SML 3.CO 2.C 6 |   |   |   | x |
| SML 3.CO 3.C 1 | x | x | x | x |
| SML 3.CO 3.C 2 |   | x | x | x |
| SML 3.CO 3.C 3 |   |   |   | x |
| SML 3.CO 4.C 1 | x | x | x | x |
| SML 3.CO 4.C 2 |   | x | x | x |
| SML 3.CO 4.C 3 |   |   | x | x |
| SML 3.CO 4.C 4 |   |   |   | x |
| SML 3.CO 4.C 5 |   |   |   | x |