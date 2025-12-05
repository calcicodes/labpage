---
title: "Contribute Data"
layout: single
permalink: /data/calcification/contribute/
classes: wide
author: Orlando Timmerman
author_profile: true
---

{: .notice--warning}
**Demo Mode - Online Submission Coming Soon**

The online submission form is currently under development. For now, please download the template below, fill it in with your data, and email it to us at **[rt582@cam.ac.uk](mailto:rt582@cam.ac.uk?subject=Calcification Database Submission&body=Please find attached my data submission for the Global Database of Benthic Calcification Rates.)**.

## Step 1: Download Template

Download a CSV template file for data submission. Fill it in with your data following the format shown in the example row within the file and the column descriptions below.

<div style="margin: 2rem 0;">
  <a href="{{ '/assets/data/data_template.csv' | relative_url }}" 
     class="btn btn--primary"
     download="data_template.csv">
    📥 Download Template
  </a>
</div>

## Column Descriptions

<details>
  <summary style="cursor: pointer; font-weight: bold; margin: 1rem 0; padding: 0.5rem; background-color: #f8f9fa; border-radius: 0.25rem;">Click to expand column descriptions</summary>
  
  <p style="color: #666; margin: 1rem 0;">
    Please only enter values that you have <strong>measured</strong>. The remaining fields will be populated automatically where possible using the <a href="https://github.com/oscarbranson/cbsyst" target="_blank">CBSyst</a> Python package.
  </p>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 2rem 0;">
    <div>
      <dl style="margin: 0;">
        {% include column-definition.html name="doi" type="str" description="Digital Object Identifier (DOI) of the publication from which the data originates. We are currently only accepting data associated with peer-reviewed publications." example='"10.1002/ece3.11316"' %}

        {% include column-definition.html name="authors" type="str" description="Names of the authors of the publication, separated by commas." example='"John Doe, Jane Smith"' %}
        
        {% include column-definition.html name="species_binomial" type="str" description="Scientific name of the species (genus and species) in binomial nomenclature." example='"Lithothamnion sp." or "Corallina officinalis"' %}
        
        {% include column-definition.html name="year" type="int" description="Year in which the study or data collection was conducted. Four-digit year." example="2024" %}
        
        {% include column-definition.html name="sample_location" type="str" description="Geographic location where the sample was collected. Include as much detail as appropriate." example='"Heron Island, Great Barrier Reef, Queensland, Australia"' %}
        
        {% include column-definition.html name="latitude" type="float" description="Latitude coordinate of the sampling location in decimal degrees. Use negative values for Southern Hemisphere." example="-33.868" %}
        
        {% include column-definition.html name="longitude" type="float" description="Longitude coordinate of the sampling location in decimal degrees. Use negative values for Western Hemisphere." example="151.215" %}
        
        {% include column-definition.html name="sample_type" type="str" description="Type of sample used in the study." example='"colony", "fragment"' %}
        
        {% include column-definition.html name="days_duration" type="int" description="Duration of the experimental treatment in days." example="10" %}
        
        {% include column-definition.html name="notes" type="str" description="Additional notes or methodological information about the measurement. Free text." example='"Buoyant weight method"' %}
        
        {% include column-definition.html name="pco2" type="float" description="Partial pressure of CO₂ in the water (ppm)." example="420" %}
        
        {% include column-definition.html name="pco2_sd" type="float" description="Standard deviation of pCO₂ measurements." %}
        
        {% include column-definition.html name="pco2_se" type="float" description="Standard error of pCO₂ measurements." %}
        
        {% include column-definition.html name="phnbs" type="float" description="pH measured on the NBS (National Bureau of Standards) scale." %}
        
        {% include column-definition.html name="phnbs_sd" type="float" description="Standard deviation of pH (NBS scale) measurements." %}
        
        {% include column-definition.html name="phnbs_se" type="float" description="Standard error of pH (NBS scale) measurements." %}
        
        {% include column-definition.html name="phsws" type="float" description="pH measured on the SWS (Seawater Scale)." %}
        
        {% include column-definition.html name="phsws_sd" type="float" description="Standard deviation of pH (SWS scale) measurements." %}
        
        {% include column-definition.html name="phsws_se" type="float" description="Standard error of pH (SWS scale) measurements." %}
        
        {% include column-definition.html name="phtot" type="float" description="pH measured on the total scale." %}
        
        {% include column-definition.html name="phtot_sd" type="float" description="Standard deviation of pH (total scale) measurements." %}
        
        {% include column-definition.html name="phtot_se" type="float" description="Standard error of pH (total scale) measurements." %}
        
        {% include column-definition.html name="temp" type="float" description="Temperature of the water in degrees Celsius (°C)." example="25.5" %}
        
        {% include column-definition.html name="temp_sd" type="float" description="Standard deviation of temperature measurements." %}
        
        {% include column-definition.html name="temp_se" type="float" description="Standard error of temperature measurements." %}
        
        {% include column-definition.html name="sal" type="float" description="Salinity of the water (practical salinity units, PSU). Float typically between 30-40." %}
        
        {% include column-definition.html name="sal_sd" type="float" description="Standard deviation of salinity measurements." %}
        
        {% include column-definition.html name="sal_se" type="float" description="Standard error of salinity measurements." %}
      </dl>
    </div>
    
    <div>
      <dl style="margin: 0;">
        {% include column-definition.html name="ta" type="float" description="Total alkalinity (μmol kg⁻¹)." example="2300" %}
        
        {% include column-definition.html name="ta_sd" type="float" description="Standard deviation of total alkalinity measurements." %}
        
        {% include column-definition.html name="ta_se" type="float" description="Standard error of total alkalinity measurements." %}
        
        {% include column-definition.html name="omegaa" type="float" description="Aragonite saturation state (Ωar). Float typically between 0-5." %}
        
        {% include column-definition.html name="omegaa_sd" type="float" description="Standard deviation of aragonite saturation state." %}
        
        {% include column-definition.html name="omegaa_se" type="float" description="Standard error of aragonite saturation state." %}
        
        {% include column-definition.html name="omegac" type="float" description="Calcite saturation state (Ωcal). Float typically between 0-5." %}
        
        {% include column-definition.html name="omegac_sd" type="float" description="Standard deviation of calcite saturation state." %}
        
        {% include column-definition.html name="omegac_se" type="float" description="Standard error of calcite saturation state." %}
        
        {% include column-definition.html name="dic" type="float" description="Dissolved inorganic carbon (μmol kg⁻¹)." example="2000" %}
        
        {% include column-definition.html name="dic_sd" type="float" description="Standard deviation of dissolved inorganic carbon." %}
        
        {% include column-definition.html name="dic_se" type="float" description="Standard error of dissolved inorganic carbon." %}
        
        {% include column-definition.html name="co3" type="float" description="Carbonate ion concentration (μmol kg⁻¹)." example="200" %}
        
        {% include column-definition.html name="co3_sd" type="float" description="Standard deviation of carbonate ion concentration." %}
        
        {% include column-definition.html name="co3_se" type="float" description="Standard error of carbonate ion concentration." %}
        
        {% include column-definition.html name="hco3" type="float" description="Bicarbonate ion concentration (μmol kg⁻¹)." example="1800" %}
        
        {% include column-definition.html name="hco3_sd" type="float" description="Standard deviation of bicarbonate ion concentration." %}
        
        {% include column-definition.html name="hco3_se" type="float" description="Standard error of bicarbonate ion concentration." %}
        
        {% include column-definition.html name="do" type="float" description="Dissolved oxygen concentration (μmol kg⁻¹ or mg L⁻¹)." example="250" %}
        
        {% include column-definition.html name="do_sd" type="float" description="Standard deviation of dissolved oxygen." %}
        
        {% include column-definition.html name="do_se" type="float" description="Standard error of dissolved oxygen." %}
        
        {% include column-definition.html name="irr" type="float" description="Irradiance (μmol photons m⁻² s⁻¹)." example="150" %}
        
        {% include column-definition.html name="irr_sd" type="float" description="Standard deviation of irradiance." %}
        
        {% include column-definition.html name="irr_se" type="float" description="Standard error of irradiance." %}
        
        {% include column-definition.html name="irr_total" type="float" description="Total irradiance integrated over the day (μmol photons m⁻² day⁻¹)." example="200" %}
        
        {% include column-definition.html name="irr_total_sd" type="float" description="Standard deviation of total irradiance." %}
        
        {% include column-definition.html name="irr_total_se" type="float" description="Standard error of total irradiance." %}
        
        {% include column-definition.html name="n" type="int" description="Sample size (number of replicates or measurements)." example="5" %}
        
        {% include column-definition.html name="calcification_rate" type="float" description="Calcification rate measurement. Units specified in calcification_rate_unit column." %}
        
        {% include column-definition.html name="calcification_rate_sd" type="float" description="Standard deviation of calcification rate." %}
        
        {% include column-definition.html name="calcification_rate_se" type="float" description="Standard error of calcification rate." %}
        
        {% include column-definition.html name="calcification_rate_unit" type="str" description='Units for the calcification rate measurement.' example='"mgCaCO3 m-2d-1", "umol CaCO3 m-2 h-1", "g m-2 d-1"' %}
      </dl>
    </div>
  </div>
</details>

## Step 2: Submit Your Data

**Submission Instructions:**

1. Download and fill in the CSV template
2. Check that your data follows the correct format
3. Email your completed CSV file to: **[rt582@cam.ac.uk](mailto:rt582@cam.ac.uk?subject=Calcification Database Submission&body=Please find attached my data submission for the Global Database of Benthic Calcification Rates.)**
4. Include your name and contact information in the email
5. Your submission will be reviewed before being added to the database

{: .notice--success}
**Coming Soon:** An online submission form will be available soon, allowing you to upload your CSV file directly through this website.

