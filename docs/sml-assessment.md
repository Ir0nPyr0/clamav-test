---
hide:
  - toc
---

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

# 🛡️ Sovereignty Maturity Level (SML) Assessment Tool

This interactive tool allows you to perform a complete self-assessment of your digital sovereignty based on the official **SML Framework (v1.1)** with all 162 controls.

## 📊 Interactive Assessment Dashboard

The tool runs completely inside your browser using **WebAssembly (stlite/Pyodide)**. No data is sent to an external server—your entries, evidence, and compliance results remain entirely private within your browser session.

<!-- 
=============================================================================
  SELBSTTRAGENDES INLINE-STYLE FÜR MAXIMALE BROWSER-KOMPATIBILITÄT (SAFARI & FIREFOX)
  Dieses Style-Block lädt sich direkt mit dem HTML und umgeht jegliche CSS-Caching-Probleme.
=============================================================================
-->
<style>
  /* 1. Iframe-Container erzwingen (Verhindert den Null-Höhen-Kollaps in Safari/Firefox) */
  .sml-container {
      position: relative !important;
      width: 100% !important;
      height: 82vh !important;
      min-height: 650px !important;
      border-radius: 8px !important;
      border: 1px solid #e0e0e0 !important;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.075) !important;
      overflow: hidden !important;
      margin: 1.5rem 0 !important;
      background-color: #ffffff !important;
      display: block !important; /* Wichtig für Firefox/Safari */
  }

  /* 2. Iframe vollständig einpassen */
  .sml-iframe {
      width: 100% !important;
      height: 100% !important;
      border: none !important;
      display: block !important;
  }

  /* 3. Widescreen-Optimierung direkt auf dieser Seite erzwingen */
  @media screen and (min-width: 76.25em) {
      .md-grid, 
      .md-main__inner {
          max-width: 95% !important; /* Layout weiten */
      }
      .md-content {
          width: 100% !important;
      }
      .md-content__inner {
          max-width: 100% !important;
      }
  }

  /* Spezifisch für Ihren 34-Zoll-Monitor */
  @media screen and (min-width: 120em) {
      .md-grid, 
      .md-main__inner {
          max-width: 98% !important;
      }
      .sml-container {
          height: 86vh !important; /* Mehr vertikale Höhe schenken */
      }
  }
</style>

<div class="sml-container">
  <iframe class="sml-iframe" src="../sml-tool.html"></iframe>
</div>

---

## 📘 Quick Start Guide

### Step 1: Preparation
* Gather all relevant documentation for the service being evaluated (e.g., contracts, SLAs, encryption concepts, corporate structure, architecture diagrams).
* Identify key subject matter experts (Security, Legal, Data Privacy, Strategy, AI Engineers) within your organization.

### Step 2: Assess Dimension by Dimension
* Use the sidebar navigation within the tool to go through the **9 SML dimensions** (SML 1 to SML 9).
* Check **`Fulfilled (Yes)`** if a control is fully met.
* **Document your findings**: Fill out the **`Evidence`** free-text field with precise details (such as document titles, internal SOPs, or roles). *Unsubstantiated "Yes" answers hold no compliance value during audits!*

### Step 3: Save & Resume Progress
* **Export**: At any point, navigate to the **`Data Management`** panel in the sidebar, fill in your audit metadata (Scope, Service Type, Version), and click **`Export Assessment (JSON)`** to download your progress in plain text.
* **Resume**: Next time you open the docs, use **`Load Assessment (JSON)`** to upload your saved file. All answers, evidence texts, and metadata will be restored instantly with zero UI latency.

### Step 4: Evaluate Gaps
* Analyze the **Radar Chart** on the **`Dashboard Overview`** to identify gaps.
* Check the **`Overall open requirements for the next maturity level`** card.
* To elevate your maturity level, satisfy all outstanding mandatory controls marked with a badge of the next level (e.g., `🌱 Initial`).
