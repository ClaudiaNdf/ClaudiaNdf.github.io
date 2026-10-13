function toggleSection(sectionId) {
    var section = document.getElementById(sectionId);
    var isVisible = section.style.display === 'block';

    // Toggle visibility
    section.style.display = isVisible ? 'none' : 'block';

    // Update the arrow
    var arrow = section.previousElementSibling.querySelector('span');
    arrow.innerHTML = isVisible ? '&#x25BC;' : '&#x25B2;';
}
