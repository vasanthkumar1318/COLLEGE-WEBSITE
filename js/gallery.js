document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('gallery-grid');
    const filterBtns = document.querySelectorAll('.filter-btn');
    
    // Lightbox elements
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const closeBtn = document.getElementById('lightbox-close');
    const prevBtn = document.getElementById('lightbox-prev');
    const nextBtn = document.getElementById('lightbox-next');
    
    let currentImageIndex = 0;
    let filteredImages = [];

    function renderGallery(filter = 'all') {
        grid.innerHTML = '';
        
        filteredImages = filter === 'all' 
            ? GalleryManifest 
            : GalleryManifest.filter(img => img.category === filter);
            
        if(filteredImages.length === 0) {
            grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; color: gray;">No images available for this category yet.</p>';
            return;
        }

        filteredImages.forEach((img, index) => {
            const div = document.createElement('div');
            div.className = 'gallery-item';
            div.innerHTML = `
                <img src="${img.path}" alt="${img.title}" loading="lazy" onerror="this.src='images/adithya_college.png'; this.onerror=null;">
                <div class="gallery-info">
                    <h4>${img.title}</h4>
                    <p>${img.caption}</p>
                    <span class="category">${img.category.toUpperCase()}</span>
                </div>
            `;
            
            div.addEventListener('click', () => openLightbox(index));
            grid.appendChild(div);
        });
    }

    function openLightbox(index) {
        currentImageIndex = index;
        updateLightbox();
        lightbox.classList.remove('hidden');
    }

    function updateLightbox() {
        const img = filteredImages[currentImageIndex];
        lightboxImg.src = img.path;
        lightboxCaption.innerHTML = `<strong>${img.title}</strong><br>${img.caption}`;
    }

    function closeLightbox() {
        lightbox.classList.add('hidden');
    }

    // Listeners
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderGallery(btn.dataset.filter);
        });
    });

    closeBtn.addEventListener('click', closeLightbox);
    
    lightbox.addEventListener('click', (e) => {
        if(e.target === lightbox) closeLightbox();
    });

    prevBtn.addEventListener('click', () => {
        currentImageIndex = (currentImageIndex - 1 + filteredImages.length) % filteredImages.length;
        updateLightbox();
    });

    nextBtn.addEventListener('click', () => {
        currentImageIndex = (currentImageIndex + 1) % filteredImages.length;
        updateLightbox();
    });

    document.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('hidden')) {
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft') prevBtn.click();
            if (e.key === 'ArrowRight') nextBtn.click();
        }
    });

    // Initialize
    if(typeof GalleryManifest !== 'undefined') {
        renderGallery();
    }
});