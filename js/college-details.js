document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('dashboard-content');
    
    if (typeof CollegeInfo === 'undefined') return;

    // Render About
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-university"></i> About College</h3>
            <p><strong>${CollegeInfo.about.name}</strong></p>
            <p>${CollegeInfo.about.intro}</p>
            <a href="${CollegeInfo.about.website}" target="_blank" class="btn-primary">Official Website</a>
        </div>
    `;

    // Render Courses
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-book"></i> Courses Offered</h3>
            <p><strong>Undergraduate:</strong></p>
            <ul>${CollegeInfo.courses.ug.map(c => `<li>${c}</li>`).join('')}</ul>
            <p><strong>Postgraduate:</strong></p>
            <ul>${CollegeInfo.courses.pg.map(c => `<li>${c}</li>`).join('')}</ul>
        </div>
    `;

    // Render Admission & Fees
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-file-signature"></i> Admission & Fees</h3>
            <p><strong>Process:</strong> ${CollegeInfo.admission.process}</p>
            <p><strong>Eligibility:</strong> ${CollegeInfo.admission.eligibility}</p>
            <p><strong>Fees:</strong> ${CollegeInfo.admission.fees}</p>
            <p><em>* ${CollegeInfo.admission.note}</em></p>
        </div>
    `;

    // Render Facilities
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-building"></i> Facilities</h3>
            <ul>${CollegeInfo.facilities.map(f => `<li>${f}</li>`).join('')}</ul>
        </div>
    `;

    // Render Contact
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-address-book"></i> Contact & Location</h3>
            <p><i class="fas fa-map-marker-alt"></i> ${CollegeInfo.contact.address}</p>
            <p><i class="fas fa-phone"></i> ${CollegeInfo.contact.phone}</p>
            <p><i class="fas fa-envelope"></i> ${CollegeInfo.contact.email}</p>
            <div style="margin-top: 15px; display: flex; gap: 10px;">
                <a href="${CollegeInfo.contact.mapUrl}" target="_blank" class="btn-primary"><i class="fas fa-map"></i> Open Maps</a>
            </div>
        </div>
    `;
});