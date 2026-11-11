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

<img width="391" height="192" alt="SDT_ES3_Logo_4c_neg_RGB" src="https://github.com/user-attachments/assets/2ba57a71-8f9d-45ec-99fb-45045403eb10" />

# Welcome to the ES³ Sovereignty Maturity Level (SML) Framework!

## What is our Mission?

> **"To make digital sovereignty measurable, comparable, and manageable, empowering organizations with the absolute capability to terminate, migrate, or substitute IT services at any time without facing unacceptable technical, legal, operational, or supply chain dependencies."**

## What is ES³?

### Project Puropose of ES³
The **ES³ Sovereignty Maturity Level (SML) Framework** is a standardized, auditable, and evidence-based assessment system developed to measure and verify the digital sovereignty of IT services and cloud infrastructures. 

At its heart, the framework is guided by a fundamental definition of digital sovereignty: **"the ability to walk away from the table at any time."** This means guaranteeing organizations the ultimate freedom to migrate or terminate a service without facing prohibitive legal, technical, operational, or supply chain risks. By aligning with the **EU Cloud Sovereignty Framework** and operationalizing its objectives, the project establishes a rigorous, transparent standard that turns abstract sovereignty goals into quantifiable, comparable, and verifiable architectural and contractual realities.

### Scope of ES³
The SML Framework evaluates IT services and infrastructures across **nine key dimensions**:

1. **Strategic Sovereignty (SML 1):** Evaluates corporate governance structures, transparent beneficial ownership, explicit commitments to localized control, and executive exit capability.
2. **Legal & Jurisdictional Sovereignty (SML 2):** Assesses regulatory environments, geographic boundaries for service delivery and data processing, and protection against unauthorized or extraterritorial third-party access claims.
3. **Data Sovereignty (SML 3):** Measures control parameters over data assets throughout their lifecycle, covering customer-controlled access management, cross-environment data portability, and purpose-bound usage constraints.
4. **Operational Sovereignty (SML 4):** Evaluates the capacity to run, maintain, and support services independently, including administrative access controls, service operations, and autonomous incident recovery.
5. **Supply Chain Sovereignty (SML 5):** Measures the composition, component tracking (such as SBOM), and systemic resilience of the third-party ecosystem supporting the service, including the flow-down of sovereignty requirements.
6. **Technology Sovereignty (SML 6):** Assesses the physical or logical layout of the technical stack, the deployment of infrastructure in approved zones, and the use of open standards to prevent proprietary vendor lock-in.
7. **Security & Compliance Sovereignty (SML 7):** Evaluates the isolation, administrative control, and auditability of security configurations, and the isolation of high-risk or sensitive operational tasks.
8. **Environmental Sustainability (SML 8):** Evaluates long-term operational resilience, resource dependency profiles, and metric transparency regarding environmental constraints and energy autonomy.
9. **Artificial Intelligence (AI) Sovereignty (SML 9):** Evaluates organizational oversight, system explainability, lifecycle management, control of AI assets, and the protection of training data against unauthorized storage or reuse.

### The Assessment Methodology
* **Evidence-Based Evaluation:** High-level dimensions break down into specific control objectives and binary audit questions. Every answer must be substantiated by verifiable evidence, such as contractual clauses, system configurations, or architectural diagrams, ensuring reproducible results.
* **Maturity Classifications:** Services are assessed and mapped to one of four Sovereignty Maturity Levels: **Initial**, **Managed**, **Advanced**, or **Future-Proof**.
* **The "Weakest Link" Principle:** Digital sovereignty is only as strong as its weakest link. A service's overall SML corresponds to the lowest level achieved across all nine dimensions—meaning that a high score in one area cannot offset or compensate for a failure to meet mandatory requirements in another.

### 🛡️ Sovereignty Maturity Level (SML) Assessment Tool

This repository contains an interactive, user-friendly assessment tool in the form of a **Streamlit web application** for evaluating the digital sovereignty of services and service providers according to the official **Sovereignty Maturity Level (SML) Framework (v1.1)**. 

The tool enables organizations to conduct a comprehensive self-assessment across all **9 dimensions** of the SML framework, document evidence, calculate the overall maturity level in real-time, and visualize the results graphically in an **interactive radar chart (spider web diagram)**.

### 🚀 Key Features of the Web Application

*   **Complete Coverage:** All **9 dimensions** and **162 controls** of the SML Framework v1.1 are hierarchically integrated.
*   **Hierarchical Structure:** The user interface is logically structured by **Dimension** &rarr; **Control Objective** &rarr; **Control** &rarr; **Question** &rarr; **Evidence**.
*   **Interactive Dashboard:**
    *   **KPI Display:** Instant and dynamic calculation of the achieved overall SML maturity level (**Basic/None**, **Initial**, **Managed**, **Advanced**, or **Future-proof**).
    *   **Interactive Radar Chart:** Visualizes the fulfillment rate (in %) for each dimension in a direct comparison—with optimized scaling (0-100%) and clearly legible labels in solid black text.
    *   **Detailed view of the nine dimensions:** Detailed tabular overview with progress bars per dimension without distracting decimal places.
*   **Maturity Level Logic (Gatekeeper Mode):** Strict implementation of the official SML rule. A higher maturity level is only unlocked once **all** mandatory controls of the lower levels are fully met.
*   **Easy Data Management (Save & Load):**
    *   **Audit Metadata:** Record the specific scope (**`Scope`**, e.g., system or department) and service type (**`Service Type`**, e.g., SaaS, PaaS, IaaS) directly in the tool. This metadata is visualized on the dashboard and saved within your export.
    *   **Export Assessment:** Download your current assessment progress (answers, evidence, version, scope, and service type) as a structured `.json` file at any time.
    *   **Load Assessment:** Upload a previously saved JSON file to instantly restore your answers, documented evidence, and all metadata with zero UI delay.
    *   **Reset:** Reset the entire assessment with a single click.
*   **Documentation & Audit Readiness:** Each control features a large free-text field for detailed documentation of evidence (Evidence).

### 📘 Guide to Conducting the SML Assessment

The SML framework is a tool designed to establish transparency and trust in cloud and service infrastructures. To perform a successful assessment, we recommend the following workflow:

#### Step 1: Preparation
*   Gather all relevant documentation for the service being evaluated (e.g., contracts, SLAs, encryption concepts, shareholder structures, architecture diagrams, policies).
*   Identify the responsible subject matter experts (Security, Legal, Data Privacy, Strategy, AI Engineers) within your organization.

#### Step 2: Assess Dimension by Dimension
*   Use the left navigation menu to go through the 9 dimensions sequentially (SML 1 to SML 9).
*   **Response:** If a control is already fully implemented in your organization, check the box next to **`Fulfilled (Yes)`**.
*   **Documentation (Critical for Audits):** In the **`Evidence (Nachweise / Belege)`** field, describe precisely *why* the requirement is met. Reference specific documents (e.g., *\"Security Concept v2.1, Section 4.2\"*), internal processes, URLs, or owners. A "Yes" answer without documented evidence holds no value in a real audit.

#### Step 3: Save Progress & Maintain Metadata
*   If you need to pause your assessment, manage multiple versions, or evaluate different environments, use the **`Data Management`** section in the left sidebar.
*   **Maintain Audit Metadata:** Under **`Scope`**, enter the precise scope of your evaluation (e.g., *\"Enterprise Cloud Service\"* or *\"Customer CRM Instance\"*), and select the appropriate **`Service Type`** (e.g., SaaS, PaaS, IaaS). This information is displayed in real-time in the metadata card at the top-left of the dashboard.
*   **Versioning:** Enter a descriptive file name in **`Filename`** and the current version number in **`Version`** (e.g., `crm_sml_assessment` and `1.2`).
*   **Exporting:** Click **`Export Assessment (JSON)`**. The file will be downloaded as `crm_sml_assessment_v1.2.json` and contains all answers, evidence text, metadata, and version tags in plain text.
*   **Loading:** In your next session, upload this JSON file using the **`Load Assessment (JSON)`** file uploader. All answers, documented evidence, and audit metadata will be fully restored without latency.

#### Step 4: Analyze Dashboard & Remediate Gaps
*   Go to **Dashboard Overview**. The **Radar Chart** visually highlights your strongest and weakest dimensions.
*   Verify your **Overall Maturity Level**:
    *   If it shows **Basic / None**, look at the **`Overall open requirements for the next maturity level:`** card.
    *   To reach the next level, you must find the outstanding mandatory controls in the dimension tabs (identified by the ``🌱 Initial`` tag) and set them to "Yes".
*   Prioritize gap remediation from left to right: first satisfy *Initial* requirements, then move to *Managed*, *Advanced*, and finally *Future-proof*.

#### Step 5: Let´ go and [assess here](https://es3-sml.github.io/es3-sml/sml-assessment/)

---

## ES³ and NeoNephos
We plan to donate the **ES³ Sovereignty Maturity Level (SML) Framework** to the NeoNephos Foundation, a Linux Foundation initiative dedicated to advancing open-source projects, and are currently preparing the necessary steps.   
Learn more about NeoNephos and our role within it [here](https://neonephos.org/).

## Get Involved
We welcome contributions of all kinds! If you're interested in getting involved, check out our contribution guidelines (will come soon) and our open issues (will come soon).

## Learn More
To learn more about ES³, visit our official website at www.stackit.com/en/es3

## Documentation
Find [here the base documentation](./docs/assets/SDC_Katalog_ES3_EN.pdf) for this project.

## Contact
ES3@digits.schwarz  
Sofie Schönborn (Digital Sovereignty Manager)  
Jo-Ann Sophie Gosemann (ES³ Program Lead)

## License
Content in this repository is licensed under [CC BY-SA 4.0](LICENSE.md).