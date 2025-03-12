document.addEventListener('DOMContentLoaded', function() {
    // Initialize parallax effect
    const parallaxContainer = document.getElementById('parallax-hero');
    
    if (parallaxContainer) {
        const layers = document.querySelectorAll('.parallax-layer');
        
        // Function to update parallax positions
        const handleParallax = (e) => {
            const centerX = window.innerWidth / 2;
            const centerY = window.innerHeight / 2;
            const mouseX = e.clientX;
            const mouseY = e.clientY;
            
            // Calculate mouse position relative to center (in percentage)
            const posX = (mouseX - centerX) / centerX;
            const posY = (mouseY - centerY) / centerY;
            
            // Apply transform to each layer based on depth
            layers.forEach(layer => {
                const depth = parseFloat(layer.getAttribute('data-depth'));
                const moveX = posX * depth * 100;
                const moveY = posY * depth * 100;
                
                layer.style.transform = `translate3d(${moveX}px, ${moveY}px, 0)`;
            });
        };
        
        // Apply parallax effect on mousemove
        window.addEventListener('mousemove', handleParallax);
        
        // Apply reveal animations
        const revealTexts = document.querySelectorAll('.reveal-text .reveal-line');
        revealTexts.forEach((text, index) => {
            text.style.animationDelay = `${0.2 + index * 0.1}s`;
        });
        
        const revealItems = document.querySelectorAll('.reveal-item');
        revealItems.forEach(item => {
            const delay = item.getAttribute('data-delay') || 0;
            item.style.animationDelay = `${delay}s`;
        });
    }
}); 