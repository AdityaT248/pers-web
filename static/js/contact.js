// Remove or comment out any existing form submission code
// Let the native HTML form handle the submission to Formspree

document.addEventListener('DOMContentLoaded', function() {
    console.log('Contact form initialized - using direct Formspree submission');
    
    // Remove any existing event listeners on form submit
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        const clonedForm = contactForm.cloneNode(true);
        contactForm.parentNode.replaceChild(clonedForm, contactForm);
    }
}); 