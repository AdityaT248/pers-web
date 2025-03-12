document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate on Scroll)
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        mirror: false
    });
    
    // Header scroll behavior
    const header = document.getElementById('main-header');
    const backToTop = document.getElementById('back-to-top');
    
    window.addEventListener('scroll', function() {
        // Header behavior
        if (window.scrollY > 50) {
            header.classList.add('bg-white', 'dark:bg-gray-800', 'shadow-md');
            header.classList.remove('bg-transparent');
        } else {
            header.classList.remove('bg-white', 'dark:bg-gray-800', 'shadow-md');
            header.classList.add('bg-transparent');
        }
        
        // Back to top button behavior
        if (window.scrollY > 500) {
            backToTop.classList.add('scale-100');
            backToTop.classList.remove('scale-0');
        } else {
            backToTop.classList.remove('scale-100');
            backToTop.classList.add('scale-0');
        }
    });
    
    // Back to top button click
    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuBackdrop = document.getElementById('mobile-menu-backdrop');
    const mobileMenuClose = document.getElementById('mobile-menu-close');
    const menuIcon = document.getElementById('menu-icon');
    const closeIcon = document.getElementById('close-icon');
    
    function openMobileMenu() {
        mobileMenu.classList.remove('translate-x-full');
        mobileMenuBackdrop.classList.remove('opacity-0', 'pointer-events-none');
        menuIcon.classList.add('hidden');
        closeIcon.classList.remove('hidden');
        document.body.classList.add('overflow-hidden');
    }
    
    function closeMobileMenu() {
        mobileMenu.classList.add('translate-x-full');
        mobileMenuBackdrop.classList.add('opacity-0', 'pointer-events-none');
        menuIcon.classList.remove('hidden');
        closeIcon.classList.add('hidden');
        document.body.classList.remove('overflow-hidden');
    }
    
    mobileMenuButton.addEventListener('click', openMobileMenu);
    mobileMenuClose.addEventListener('click', closeMobileMenu);
    mobileMenuBackdrop.addEventListener('click', closeMobileMenu);
    
    // Close mobile menu on window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth >= 768) {
            closeMobileMenu();
        }
    });
    
    // Mobile menu links
    const mobileMenuLinks = document.querySelectorAll('#mobile-menu a[href^="#"]');
    mobileMenuLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });
    
    // Initialize 3D tilt effect for project cards
    if (typeof VanillaTilt !== 'undefined') {
        VanillaTilt.init(document.querySelectorAll(".project-card-3d"), {
            max: 10,
            speed: 400,
            glare: true,
            "max-glare": 0.3,
        });
    }
    
    // Preloader
    const preloader = document.getElementById('preloader');
    if (preloader) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                preloader.classList.add('opacity-0');
                setTimeout(function() {
                    preloader.style.display = 'none';
                }, 500);
            }, 500);
        });
    }
    
    // Smooth scrolling for anchor links with header offset
    const headerHeight = document.querySelector('header').offsetHeight;
    
    // Select all anchor links that point to an ID on the same page
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Get the target element
            const targetId = this.getAttribute('href');
            if (targetId === '#') return; // Skip empty anchors
            
            const targetElement = document.querySelector(targetId);
            if (!targetElement) return; // Skip if target doesn't exist
            
            // Calculate position with header offset
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
            
            // Smooth scroll to target
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            
            // Update URL if needed (optional)
            history.pushState(null, null, targetId);
        });
    });
    
    // NEW CODE: Make sections clickable to scroll to next section
    const mainSections = document.querySelectorAll('section[id]');
    
    mainSections.forEach(section => {
        // Add a clickable class and cursor pointer to indicate clickability
        section.classList.add('section-clickable');
        
        section.addEventListener('click', function(e) {
            // Don't trigger if clicking on an interactive element
            if (e.target.closest('a, button, input, select, textarea, .no-section-click')) {
                return;
            }
            
            // Find the next section
            let nextSection = null;
            let foundCurrent = false;
            
            mainSections.forEach(sect => {
                if (foundCurrent && !nextSection) {
                    nextSection = sect;
                }
                if (sect === section) {
                    foundCurrent = true;
                }
            });
            
            // If found, scroll to the next section
            if (nextSection) {
                const targetPosition = nextSection.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Update URL (optional)
                history.pushState(null, null, `#${nextSection.id}`);
            }
        });
    });
}); 