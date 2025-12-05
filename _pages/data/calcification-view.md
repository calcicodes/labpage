---
title: "View Data"
layout: single
permalink: /data/calcification/view/
classes: wide
author: Orlando Timmerman
author_profile: true
---

{: .notice--warning}
**Demo Mode:** This is a static snapshot of the database for demonstration purposes. Interactive features including column selection, sorting, filtering, and live updates will be available when the full system launches.

<div style="text-align: right; margin-bottom: 1rem;">
  <a href="{{ '/assets/data/calcification_database_demo.csv' | relative_url }}" 
     class="btn btn--primary" 
     download="calcification_database_demo.csv">
    📥 Download Data
  </a>
</div>


## Database Contents

<div style="overflow-x: auto; max-height: 80vh; margin: 2rem 0;">
  <table style="width: 100%; border-collapse: collapse;">
    <thead style="position: sticky; top: 0; background-color: #333; color: white; z-index: 10;">
      <tr>
        <th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">ID</th>
        <th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">DOI</th>
        <th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Authors</th>
        <th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Species</th>
        <th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Year</th>
        <th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Location</th>
        <th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Calcification Rate</th>
        <th style="padding: 0.75rem; text-align: left; border: 1px solid #ddd;">Unit</th>
      </tr>
    </thead>
    <tbody>
      {% assign demo_data = site.data.demo_records.data | limit: 50 %}
      {% for row in demo_data %}
      <tr style="border-bottom: 1px solid #ddd;">
        <td style="padding: 0.75rem; border: 1px solid #ddd;">{{ row.id }}</td>
        <td style="padding: 0.75rem; border: 1px solid #ddd;">{{ row.doi | default: "N/A" }}</td>
        <td style="padding: 0.75rem; border: 1px solid #ddd;">{{ row.authors | default: "N/A" | truncate: 50 }}</td>
        <td style="padding: 0.75rem; border: 1px solid #ddd;">{{ row.species_binomial | default: "N/A" }}</td>
        <td style="padding: 0.75rem; border: 1px solid #ddd;">{{ row.year | default: "N/A" }}</td>
        <td style="padding: 0.75rem; border: 1px solid #ddd;">{{ row.sample_location | default: "N/A" | truncate: 40 }}</td>
        <td style="padding: 0.75rem; border: 1px solid #ddd;">{{ row.calcification_rate | default: "N/A" }}</td>
        <td style="padding: 0.75rem; border: 1px solid #ddd;">{{ row.calcification_rate_unit | default: "N/A" }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<div style="padding: 2rem; border: 1px solid #ddd; border-radius: 0.25rem; text-align: center;">
  <h3>Contribute a Dataset</h3>
  <p>Download a CSV template and submit your data. Online submission form coming soon - for now, please email your completed CSV.</p>
  <a href="/data/calcification/contribute/" class="btn btn--primary">Contribute Dataset</a>
</div>