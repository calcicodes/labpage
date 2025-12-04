---
title: "Global Database of Benthic Calcification Rates"
layout: single
permalink: /databases/calcification/
classes: wide
author: Orlando Timmerman
author_profile: true
---

{: .notice--warning}
**Demo Mode:** This is a static demonstration version. Dynamic features including live database updates, interactive filtering, and real-time statistics will be available when the full system launches.

This database is open access and free to everyone to use for education and research.

## Database Statistics

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; margin: 2rem 0;">
  <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 0.25rem;">
    <h3 style="margin: 0; color: #3463a4;">160</h3>
    <small style="color: #666;">Studies</small>
  </div>
  <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 0.25rem;">
    <h3 style="margin: 0; color: #3463a4;">1</h3>
    <small style="color: #666;">Contributor</small>
  </div>
  <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 0.25rem;">
    <h3 style="margin: 0; color: #3463a4;">130</h3>
    <small style="color: #666;">Species</small>
  </div>
  <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 0.25rem;">
    <h3 style="margin: 0; color: #3463a4;">4518</h3>
    <small style="color: #666;">Records</small>
  </div>
  <div style="text-align: center; padding: 1rem; border: 1px solid #ddd; border-radius: 0.25rem;">
    <h3 style="margin: 0; color: #3463a4;">16910</h3>
    <small style="color: #666;">Samples</small>
  </div>
</div>

<small style="color: #666; display: block; text-align: center; margin-top: 1rem;">These statistics are from a static snapshot. Live statistics coming soon.</small>

## Sample Locations

<div id="map" style="height: 500px; width: 100%; border-radius: 0.25rem; margin: 2rem 0;" data-map-url="{{ '/assets/databases/data/map_points.json' | relative_url }}"></div>

## Explore the Database

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 2rem 0;">
  <div style="padding: 2rem; border: 1px solid #ddd; border-radius: 0.25rem; text-align: center;">
    <h3>View Data</h3>
    <p>Browse a static snapshot of the database. Full interactive features including sorting, filtering, and live updates coming soon.</p>
    <a href="/databases/calcification/view/" class="btn btn--primary">View Database</a>
  </div>
  
  <div style="padding: 2rem; border: 1px solid #ddd; border-radius: 0.25rem; text-align: center;">
    <h3>Contribute a Dataset</h3>
    <p>Download a CSV template and submit your data. Online submission form coming soon - for now, please email your completed CSV.</p>
    <a href="/databases/calcification/contribute/" class="btn btn--primary">Contribute Dataset</a>
  </div>
</div>

<!-- Leaflet CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
     integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
     crossorigin=""/>

<!-- Leaflet JavaScript -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
     integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
     crossorigin=""></script>

<!-- Map initialization script -->
<script>
    // Initialize map when DOM is ready
    document.addEventListener('DOMContentLoaded', function() {
        // Initialize map
        var map = L.map('map').setView([0, 0], 2);
        
        // Add OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            maxZoom: 19
        }).addTo(map);
        
        // Create custom icon
        var customIcon = L.divIcon({
            className: 'custom-marker',
            html: '<div style="background-color: #3463a4; width: 20px; height: 20px; border-radius: 50% 50% 50% 0; transform: rotate(-45deg); border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.3);"></div>',
            iconSize: [20, 20],
            iconAnchor: [10, 20],
            popupAnchor: [0, -20]
        });
        
        // Load map points from static JSON file
        var mapElement = document.getElementById('map');
        var mapDataUrl = mapElement.getAttribute('data-map-url');
        fetch(mapDataUrl)
            .then(response => response.json())
            .then(mapPoints => {
                if (mapPoints.length > 0) {
                    var bounds = [];
                    
                    mapPoints.forEach(function(point) {
                        var marker = L.marker([point.lat, point.lng], { icon: customIcon }).addTo(map);
                        
                        // Create popup content
                        var popupContent = '<strong>' + (point.location || 'Unknown location') + '</strong><br>';
                        if (point.species && point.species !== 'Unknown species') {
                            popupContent += 'Species: ' + point.species + '<br>';
                        }
                        if (point.doi) {
                            popupContent += 'DOI: ' + point.doi;
                        }
                        
                        marker.bindPopup(popupContent);
                        bounds.push([point.lat, point.lng]);
                    });
                    
                    // Fit map to show all markers
                    if (bounds.length > 0) {
                        map.fitBounds(bounds, { padding: [50, 50] });
                    }
                } else {
                    // If no points, show a message
                    map.setView([20, 0], 2);
                    L.popup()
                        .setLatLng([20, 0])
                        .setContent('No location data available yet.')
                        .openOn(map);
                }
            })
            .catch(error => {
                console.error('Error loading map data:', error);
                // Show error message on map
                map.setView([20, 0], 2);
                L.popup()
                    .setLatLng([20, 0])
                    .setContent('Error loading map data.')
                    .openOn(map);
            });
    });
</script>

