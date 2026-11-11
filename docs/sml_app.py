# ********************************************************************************
#  Copyright (c) 2026 Schwarz Digits Cloud GmbH & Co. KG
# 
#  This program and the accompanying materials are made available under the
#  terms of the Creative Commons Attribution-ShareAlike 4.0 International Public License
#  which is available at https://creativecommons.org/licenses/by-sa/4.0/.
# 
#  SPDX-License-Identifier: CC-BY-SA-4.0
# 
#  Contributors:
#    Andy Riexinger - initial contribution
# *******************************************************************************

import streamlit as st
import json
import plotly.graph_objects as go
import pandas as pd

# Page config
st.set_page_config(
    page_title="Sovereignty Maturity Level (SML) Assessment Tool",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Embedded SML Framework Data (SML v1.1)
# Dynamic SML Framework Data Loader (SML v1.1)
import os

@st.cache_data
def load_sml_data():
    # Priority list of possible paths for SML data file
    possible_paths = [
        "sml_data.json",
        os.path.join("assets", "sml_data.json")
    ]
    
    # Scan the current directory for any other matching JSON files
    try:
        for f in os.listdir("."):
            if f.startswith("sml_data") and f.endswith(".json") and f not in possible_paths:
                possible_paths.append(f)
    except Exception:
        pass

    for path in possible_paths:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict) and len(data) > 0:
                        return data
            except Exception:
                continue
    return None

SML_DATA = load_sml_data()

if SML_DATA is not None:
    # Dynamically extract and remove metadata keys from SML_DATA dictionary
    default_scope = SML_DATA.pop('scope', 'Enterprise Cloud Service')
    default_service_type = SML_DATA.pop('service_type', 'SaaS (Software as a Service)')
    default_version = SML_DATA.pop('version', '1.1')
else:
    default_scope = "Enterprise Cloud Service"
    default_service_type = "SaaS (Software as a Service)"
    default_version = "1.1"

if SML_DATA is None:
    st.error("❌ **SML Data file not found!** Please ensure that **sml_data.json** (or a matching `sml_data*.json` file) is present in your application directory or in an `assets/` folder.")
    st.info("💡 You can download the **sml_data-v4.json** file from your SML Assessment Tool workspace and place it in the same folder as this script under the name **sml_data.json**.")
    st.stop()

# Color constants for SML Levels
SML_LEVEL_COLORS = {
    "Basic / None": {"bg": "#F8D7DA", "text": "#721C24", "border": "#F5C6CB", "emoji": "⚠️"},
    "Initial": {"bg": "#CCE5FF", "text": "#004085", "border": "#B8DAFF", "emoji": "🌱"},
    "Managed": {"bg": "#D4EDDA", "text": "#155724", "border": "#C3E6CB", "emoji": "⚙️"},
    "Advanced": {"bg": "#E2D9F3", "text": "#383D41", "border": "#D6D8DB", "emoji": "🚀"},
    "Future-proof": {"bg": "#FFF3CD", "text": "#856404", "border": "#FFEEBA", "emoji": "💎"}
}

# Initialize session state for answers and evidence
if 'answers' not in st.session_state:
    st.session_state.answers = {}
    for dim_id, dim_data in SML_DATA.items():
        for obj in dim_data['objectives']:
            for ctrl in obj['controls']:
                st.session_state.answers[ctrl['id']] = False

if 'evidence' not in st.session_state:
    st.session_state.evidence = {}
    for dim_id, dim_data in SML_DATA.items():
        for obj in dim_data['objectives']:
            for ctrl in obj['controls']:
                st.session_state.evidence[ctrl['id']] = ""

# Initialize metadata fields in session state
if 'assessment_scope' not in st.session_state:
    st.session_state.assessment_scope = default_scope

if 'service_type' not in st.session_state:
    st.session_state.service_type = default_service_type

if 'export_version' not in st.session_state:
    st.session_state.export_version = default_version

if 'export_filename' not in st.session_state:
    st.session_state.export_filename = "sml_assessment_results"

# Helper to calculate maturity
def calculate_metrics():
    dim_metrics = {}
    
    # Global counters for unfulfilled required controls
    global_unf = {
        "initial": 0,
        "managed": 0,
        "advanced": 0,
        "future_proof": 0
    }
    
    for dim_id, dim_data in SML_DATA.items():
        total_controls = 0
        yes_count = 0
        
        unf_init = 0
        unf_man = 0
        unf_adv = 0
        unf_fut = 0
        
        for obj in dim_data['objectives']:
            for ctrl in obj['controls']:
                total_controls += 1
                # Read from widget state if present, fallback to answers dictionary
                widget_key = f"ans_{ctrl['id']}"
                ans = st.session_state.get(widget_key, st.session_state.answers.get(ctrl['id'], False))
                
                if ans:
                    yes_count += 1
                
                reqs = ctrl['requirements']
                if reqs.get('initial') and not ans:
                    unf_init += 1
                if reqs.get('managed') and not ans:
                    unf_man += 1
                if reqs.get('advanced') and not ans:
                    unf_adv += 1
                if reqs.get('future_proof') and not ans:
                    unf_fut += 1
        
        # SML Level Achieved for this specific dimension
        dim_level = "Future-proof"
        if unf_init > 0:
            dim_level = "Basic"
        elif unf_man > 0:
            dim_level = "Initial"
        elif unf_adv > 0:
            dim_level = "Managed"
        elif unf_fut > 0:
            dim_level = "Advanced"
            
        rate = (yes_count / total_controls * 100) if total_controls > 0 else 0
        
        dim_metrics[dim_id] = {
            "name": dim_data['dimension_title'],
            "total": total_controls,
            "yes": yes_count,
            "rate": rate,
            "level": dim_level,
            "unf_init": unf_init,
            "unf_man": unf_man,
            "unf_adv": unf_adv,
            "unf_fut": unf_fut
        }
        
        global_unf["initial"] += unf_init
        global_unf["managed"] += unf_man
        global_unf["advanced"] += unf_adv
        global_unf["future_proof"] += unf_fut

    # Global SML level calculation
    global_level = "Future-proof"
    if global_unf["initial"] > 0:
        global_level = "Basic / None"
    elif global_unf["managed"] > 0:
        global_level = "Initial"
    elif global_unf["advanced"] > 0:
        global_level = "Managed"
    elif global_unf["future_proof"] > 0:
        global_level = "Advanced"

    return dim_metrics, global_unf, global_level

# Sidebar Content
import os

# Logo Integration with title and subtitle
logo_filename = "assets/SDT_ES3_Logo_4c_neg_RGB.svg"
logo_root_path = logo_filename
logo_assets_path = os.path.join("assets", logo_filename)

# Logo Integration mit abwärtskompatiblem Parameter-Check (stlite & local)
import inspect

# Prüfe zur Laufzeit die Signatur von st.image, um TypeError vorzubeugen
has_container_width = False
try:
    sig = inspect.signature(st.image)
    if "use_container_width" in sig.parameters:
        has_container_width = True
except Exception:
    pass

if os.path.exists(logo_root_path):
    if has_container_width:
        st.sidebar.image(logo_root_path, use_container_width=True)
    else:
        st.sidebar.image(logo_root_path, use_column_width=True)
elif os.path.exists(logo_assets_path):
    if has_container_width:
        st.sidebar.image(logo_assets_path, use_container_width=True)
    else:
        st.sidebar.image(logo_assets_path, use_column_width=True)

st.sidebar.title("Sovereignty Maturity Level (SML) Assessment")
st.sidebar.markdown("#### Sovereignty Maturity Level Tool")

st.sidebar.markdown("---")

# Navigation
pages = ["📊 Dashboard Overview"] + list(SML_DATA.keys())
selected_page = st.sidebar.radio("Navigation", pages)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💾 Data Management")

# Filename and version input fields
export_filename = st.sidebar.text_input("📁 Filename", value=st.session_state.get("export_filename", "sml_assessment_results"), help="Name of the downloaded JSON file (without extension)")
st.session_state.export_filename = export_filename

export_version = st.sidebar.text_input("🏷️ Version", value=st.session_state.get("export_version", "1.0"), help="Version number of the assessment")
st.session_state.export_version = export_version

# Export functionality
dim_metrics, global_unf, global_level = calculate_metrics()

export_data = {
    "answers": st.session_state.answers,
    "evidence": st.session_state.evidence,
    "version": export_version,
    "global_level": global_level,
    "global_unfulfilled": global_unf
}

export_json = json.dumps(export_data, indent=4, ensure_ascii=False)

# Construct final filename
clean_filename = export_filename.strip() if export_filename.strip() else "sml_assessment_results"
if clean_filename.endswith(".json"):
    clean_filename = clean_filename[:-5]
    
if export_version.strip():
    clean_filename = f"{clean_filename}_v{export_version.strip()}"
    
final_filename = f"{clean_filename}.json"

st.sidebar.download_button(
    label="📥 Export Assessment (JSON)",
    data=export_json,
    file_name=final_filename,
    mime="application/json"
)

# Import functionality
uploaded_file = st.sidebar.file_uploader("📤 Load Assessment (JSON)", type=["json"])
if uploaded_file is not None:
    try:
        import_data = json.load(uploaded_file)
        if "answers" in import_data and "evidence" in import_data:
            st.session_state.answers.update(import_data["answers"])
            st.session_state.evidence.update(import_data["evidence"])
            # Synchronize Streamlit's internal widget state keys to prevent stale UI widgets
            for k, v in import_data["answers"].items():
                st.session_state[f"ans_{k}"] = v
            for k, v in import_data["evidence"].items():
                st.session_state[f"ev_{k}"] = v
            # Load metadata fields if present
            if "scope" in import_data:
                st.session_state.assessment_scope = import_data["scope"]
            if "service_type" in import_data:
                st.session_state.service_type = import_data["service_type"]
            if "version" in import_data:
                st.session_state.export_version = import_data["version"]
            st.sidebar.success("✅ Assessment loaded successfully!")
            st.rerun()
        else:
            st.sidebar.error("❌ Invalid file format!")
    except Exception as e:
        st.sidebar.error(f"❌ Error: {str(e)}")

# Reset functionality
if st.sidebar.button("🗑️ Reset", use_container_width=True):
    for k in st.session_state.answers.keys():
        st.session_state.answers[k] = False
        if f"ans_{k}" in st.session_state:
            st.session_state[f"ans_{k}"] = False
    for k in st.session_state.evidence.keys():
        st.session_state.evidence[k] = ""
        if f"ev_{k}" in st.session_state:
            st.session_state[f"ev_{k}"] = ""
    # Reset metadata fields
    st.session_state.assessment_scope = default_scope
    st.session_state.service_type = default_service_type
    st.session_state.export_version = default_version
    st.session_state.export_filename = "sml_assessment_results"
    st.sidebar.warning("⚠️ All inputs have been reset!")
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("Generated with ❤️ for digital sovereignty.")

# Page Rendering
if selected_page == "📊 Dashboard Overview":
    st.title("🛡️ Sovereignty Maturity Level (SML) Assessment")
    st.markdown("##### A structured and interactive framework for assessing digital sovereignty.")
    
    # Top KPI Metrics row
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.subheader("Overall Maturity Level")
        color_info = SML_LEVEL_COLORS[global_level]
        st.markdown(f"""
        <div style="background-color: {color_info['bg']}; padding: 25px; border-radius: 12px; border: 2px solid {color_info['border']}; text-align: center; margin-bottom: 20px;">
            <span style="font-size: 3rem;">{color_info['emoji']}</span>
            <h2 style="color: {color_info['text']}; margin: 10px 0 0 0; font-weight: bold;">{global_level}</h2>
            <p style="color: {color_info['text']}; margin: 5px 0 0 0; font-size: 1.1rem;">Achieved Sovereignty Maturity Level</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display breakdown of missing required controls
        st.write("##### Overall open requirements for the next maturity level:")
        
        c_init, c_man, c_adv, c_fut = st.columns(4)
        c_init.metric("Initial", global_unf["initial"], delta=None, help="Remaining mandatory controls for the 'Initial' level")
        c_man.metric("Managed", global_unf["managed"], delta=None, help="Remaining mandatory controls for the 'Managed' level")
        c_adv.metric("Advanced", global_unf["advanced"], delta=None, help="Remaining mandatory controls for the 'Advanced' level")
        c_fut.metric("Future-proof", global_unf["future_proof"], delta=None, help="Remaining mandatory controls for the 'Future-proof' level")
        
        # Short explanation of SML gatekeeper logic
        st.info("**SML Maturity Level Rule (Gatekeeper Logic):** A maturity level is only considered achieved when **all** controls of this and all lower maturity levels have been successfully fulfilled ('Yes'). If even a single required control for 'Initial' is missing, the overall maturity level remains at 'Basic / None'.")

    with col2:
        st.subheader("Radar-Chart")
        
        # Radar Chart Data
        categories = []
        fulfillment_rates = []
        for dim_id, m in dim_metrics.items():
            # Extract shortened name (e.g., Strategic, Legal)
            short_name = m["name"].split(":")[0].replace("Dimension", "").strip()
            categories.append(f"{dim_id}: {short_name}")
            fulfillment_rates.append(m["rate"])
            
        # Append first item again to close the radar loop
        categories_closed = categories + [categories[0]]
        rates_closed = fulfillment_rates + [fulfillment_rates[0]]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=rates_closed,
            theta=categories_closed,
            fill='toself',
            fillcolor='rgba(47, 84, 150, 0.2)',
            line=dict(color='#2F5496', width=2),
            name='Fulfillment Rate (%)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    ticksuffix="%",
                    tickfont=dict(color='black', size=10)
                )
            ),
            showlegend=False,
            margin=dict(l=80, r=80, t=30, b=30),
            height=320,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detailed view of the nine dimensions")
    
    # Build a DataFrame for nice rendering
    table_data = []
    for dim_id, m in dim_metrics.items():
        table_data.append({
            "ID": dim_id,
            "Dimension Name": m["name"],
            "Fulfillment rate": m["rate"],
            "Fulfilled (Count)": f"{m['yes']} of {m['total']}",
            "Maturity Level": m["level"]
        })
    df = pd.DataFrame(table_data)
    
    # Style and show table
    st.dataframe(
        df,
        column_config={
            "ID": st.column_config.TextColumn("ID", width="small"),
            "Dimension Name": st.column_config.TextColumn("Dimension", width="large"),
            "Fulfillment rate": st.column_config.ProgressColumn(
                "Fulfillment rate",
                help="Percentage of controls set to 'Yes'",
                format="%.0f%%",
                min_value=0,
                max_value=100
            ),
            "Fulfilled (Count)": st.column_config.TextColumn("Fulfilled (Count)"),
            "Maturity Level": st.column_config.TextColumn("Dimension Level")
        },
        hide_index=True,
        use_container_width=True
    )

    # General SML Framework description
    with st.expander("📖 About the SML Framework (Sovereignty Maturity Level)"):
        st.markdown("""
        The **Sovereignty Maturity Level (SML)** framework is a structured reference model designed to evaluate and ensure the digital sovereignty of services and service providers.
        The model is divided into **9 essential dimensions** and utilizes four clearly defined maturity levels:
        
        *   🌱 **Initial (SML 1):** The most fundamental requirements, such as transparency over organizational structures, basic contracts, and data control.
        *   ⚙️ **Managed (SML 2):** Processes and responsibilities are defined, and controls are actively managed and documented.
        *   🚀 **Advanced (SML 3):** High degree of autonomy, advanced encryption methods, extensive independence from third-party providers, and auditability.
        *   💎 **Future-proof (SML 4):** Highest security and resilience standards, complete portability, and future-readiness, e.g., in the usage of AI.
        """)

else:
    # Dimension Detail Page
    dim_id = selected_page
    dim_data = SML_DATA[dim_id]
    m = dim_metrics[dim_id]
    
    st.title(f"🛡️ {dim_data['dimension_title']}")
    st.markdown(f"*{dim_data['dimension_desc']}*")
    
    # Dimension KPI header
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Controls fulfilled", f"{m['yes']} / {m['total']}")
    col_b.metric("Fulfillment Rate", f"{m['rate']:.1f}%")
    col_c.metric("Dimension Maturity Level", m["level"])
    
    st.markdown("---")
    
    # Render hierarchically: Objectives -> Controls
    for obj in dim_data['objectives']:
        st.subheader(f"🎯 {obj['title']}")
        if "sovereignty_contribution" in obj and obj["sovereignty_contribution"]:
            st.markdown(f"""
            <div style="background-color: #E6F4EA; padding: 12px; border-radius: 6px; border-left: 5px solid #2F5496; margin-bottom: 15px; font-size: 0.95rem; color: #137333;">
                🛡️ <b>Sovereignty Contribution:</b> {obj['sovereignty_contribution']}
            </div>
            """, unsafe_allow_html=True)
        
        for ctrl in obj['controls']:
            # Create a card border like style
            with st.container():
                st.markdown(f"""
                <div style="border-left: 5px solid #2F5496; padding-left: 15px; margin-bottom: 15px; margin-top: 15px;">
                    <strong style="font-size: 1.1rem; color: #2F5496;">{ctrl['id']}</strong> - {ctrl['desc']}
                </div>
                """, unsafe_allow_html=True)
                
                # Scope 
                st.markdown(f"**Scope:** *{ctrl['control_scope']}*")

                # Service Type
                st.markdown(f"**Service Type:** *{ctrl['service_type']}*")

                # Question
                st.markdown(f"**Question:** *{ctrl['question']}*")
                
                # Badges for requirements
                req_badges = []
                reqs = ctrl['requirements']
                if reqs.get('initial'): req_badges.append("🌱 Initial")
                if reqs.get('managed'): req_badges.append("⚙️ Managed")
                if reqs.get('advanced'): req_badges.append("🚀 Advanced")
                if reqs.get('future_proof'): req_badges.append("💎 Future-proof")
                
                if req_badges:
                    st.markdown("**Required for:** " + ", ".join([f"`{b}`" for b in req_badges]))
                
                # Interactive Columns for Checkbox (Yes/No) and Evidence
                ans_col, ev_col = st.columns([1, 4])
                
                with ans_col:
                    # Checkbox for Yes/No (True/False)
                    current_ans = st.session_state.answers.get(ctrl['id'], False)
                    # Unique key for Streamlit
                    is_yes = st.checkbox("Fulfilled (Yes)", value=current_ans, key=f"ans_{ctrl['id']}")
                    st.session_state.answers[ctrl['id']] = is_yes
                    
                    if is_yes:
                        st.markdown("<span style='color:green; font-weight:bold;'>✔️ Yes</span>", unsafe_allow_html=True)
                    else:
                        st.markdown("<span style='color:red; font-weight:bold;'>❌ No</span>", unsafe_allow_html=True)
                        
                with ev_col:
                    # Text Area for Evidence
                    current_ev = st.session_state.evidence.get(ctrl['id'], "")
                    ev_text = st.text_area(
                        "Evidence", 
                        value=current_ev, 
                        placeholder="e.g., document reference, point of contact, process description, ...",
                        key=f"ev_{ctrl['id']}",
                        height=68
                    )
                    st.session_state.evidence[ctrl['id']] = ev_text
                    
                st.markdown("<hr style='border: 0.5px solid #f0f2f6; margin-top: 15px; margin-bottom: 15px;'>", unsafe_allow_html=True)
