// Theme management system
document.addEventListener('DOMContentLoaded', function() {
    // Check for theme preference in localStorage or system preference
    function getInitialTheme() {
        // Check if theme is stored in localStorage
        const storedTheme = localStorage.getItem('theme');
        if (storedTheme) {
            return storedTheme;
        }
        
        // Otherwise check system preference
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    // Set the theme
    function setTheme(theme) {
        if (theme === 'dark') {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        
        // Update all theme toggles
        document.querySelectorAll('.theme-toggle').forEach(toggle => {
            toggle.setAttribute('aria-checked', theme === 'dark');
            
            // Update icons
            const moonIcon = toggle.querySelector('.moon-icon');
            const sunIcon = toggle.querySelector('.sun-icon');
            
            if (moonIcon && sunIcon) {
                if (theme === 'dark') {
                    moonIcon.classList.add('hidden');
                    sunIcon.classList.remove('hidden');
                } else {
                    moonIcon.classList.remove('hidden');
                    sunIcon.classList.add('hidden');
                }
            }
        });
        
        // Store in localStorage
        localStorage.setItem('theme', theme);
    }

    // Initialize theme
    setTheme(getInitialTheme());

    // Set up theme toggle event listeners
    document.querySelectorAll('.theme-toggle').forEach(toggle => {
        toggle.addEventListener('click', function() {
            const isDark = document.documentElement.classList.contains('dark');
            setTheme(isDark ? 'light' : 'dark');
        });
    });
    
    // Listen for system preference changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (!localStorage.getItem('theme')) { // Only if user hasn't manually set preference
            setTheme(e.matches ? 'dark' : 'light');
        }
    });
    
    // Theme Color Dropdown Toggle
    const themeColorToggle = document.getElementById('theme-color-toggle');
    const themeColorDropdown = document.getElementById('theme-color-dropdown');
    
    if (themeColorToggle && themeColorDropdown) {
        themeColorToggle.addEventListener('click', function() {
            themeColorDropdown.classList.toggle('hidden');
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!themeColorDropdown.contains(e.target) && !themeColorToggle.contains(e.target) && !themeColorDropdown.classList.contains('hidden')) {
                themeColorDropdown.classList.add('hidden');
            }
        });
    }
    
    // Theme Color Selection
    document.querySelectorAll('.theme-color-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const theme = this.getAttribute('data-theme');
            
            // Remove existing theme classes
            document.documentElement.classList.remove('theme-blue', 'theme-green', 'theme-orange');
            
            // Add selected theme class if not default
            if (theme !== 'default') {
                document.documentElement.classList.add(`theme-${theme}`);
            }
            
            // Store in localStorage
            localStorage.setItem('color-theme', theme);
            
            // Update UI
            document.querySelectorAll('.theme-color-btn').forEach(b => {
                b.classList.remove('ring-2', 'ring-offset-2', 'ring-gray-800', 'dark:ring-white');
            });
            this.classList.add('ring-2', 'ring-offset-2', 'ring-gray-800', 'dark:ring-white');
            
            // Close dropdown
            const dropdown = document.getElementById('theme-color-dropdown');
            if (dropdown) {
                dropdown.classList.add('hidden');
            }
        });
    });
    
    // Initialize color theme
    const storedColorTheme = localStorage.getItem('color-theme') || 'default';
    if (storedColorTheme !== 'default') {
        document.documentElement.classList.add(`theme-${storedColorTheme}`);
    }
    
    // Highlight the active theme button
    const activeThemeBtn = document.querySelector(`.theme-color-btn[data-theme="${storedColorTheme}"]`);
    if (activeThemeBtn) {
        activeThemeBtn.classList.add('ring-2', 'ring-offset-2', 'ring-gray-800', 'dark:ring-white');
    }
    
    // Mobile menu functionality
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenuCloseButton = document.getElementById('mobile-menu-close');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu && mobileMenuCloseButton) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.remove('hidden');
            document.body.classList.add('overflow-hidden');
        });
        
        mobileMenuCloseButton.addEventListener('click', function() {
            mobileMenu.classList.add('hidden');
            document.body.classList.remove('overflow-hidden');
        });
    }
});

// Add theme color selector functionality
document.addEventListener('DOMContentLoaded', function() {
    // After the basic theme code...
    
    // Theme selector panel toggle
    const themeToggle = document.getElementById('theme-selector-toggle');
    const themePanel = document.getElementById('theme-selector-panel');
    
    if (themeToggle && themePanel) {
        themeToggle.addEventListener('click', function() {
            themePanel.classList.toggle('hidden');
        });
        
        // Close when clicking outside
        document.addEventListener('click', function(e) {
            if (!themePanel.contains(e.target) && !themeToggle.contains(e.target) && !themePanel.classList.contains('hidden')) {
                themePanel.classList.add('hidden');
            }
        });
        
        // Color theme selection
        document.querySelectorAll('.theme-color-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const theme = this.getAttribute('data-theme');
                
                // Remove existing theme classes
                document.documentElement.classList.remove('theme-blue', 'theme-green', 'theme-orange');
                
                // Add selected theme class if not default
                if (theme !== 'default') {
                    document.documentElement.classList.add(`theme-${theme}`);
                }
                
                // Store in localStorage
                localStorage.setItem('color-theme', theme);
                
                // Update UI
                document.querySelectorAll('.theme-color-btn').forEach(b => {
                    b.classList.remove('ring-2', 'ring-offset-2', 'ring-gray-800', 'dark:ring-white');
                });
                this.classList.add('ring-2', 'ring-offset-2', 'ring-gray-800', 'dark:ring-white');
            });
        });
        
        // Initialize color theme
        const storedColorTheme = localStorage.getItem('color-theme') || 'default';
        if (storedColorTheme !== 'default') {
            document.documentElement.classList.add(`theme-${storedColorTheme}`);
        }
        
        // Highlight the active theme button
        const activeThemeBtn = document.querySelector(`.theme-color-btn[data-theme="${storedColorTheme}"]`);
        if (activeThemeBtn) {
            activeThemeBtn.classList.add('ring-2', 'ring-offset-2', 'ring-gray-800', 'dark:ring-white');
        }
    }

    // Theme color selector on hero section
    document.querySelectorAll('.theme-color-selector .theme-color-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const theme = this.getAttribute('data-theme');
            
            // Remove existing theme classes
            document.documentElement.classList.remove('theme-blue', 'theme-green', 'theme-orange');
            
            // Add selected theme class if not default
            if (theme !== 'default') {
                document.documentElement.classList.add(`theme-${theme}`);
            }
            
            // Store in localStorage
            localStorage.setItem('color-theme', theme);
            
            // Visual feedback - add pulse animation temporarily
            this.classList.add('scale-125');
            setTimeout(() => {
                this.classList.remove('scale-125');
            }, 300);
        });
    });

    // Initialize hero section theme buttons on load
    const storedColorThemeHero = localStorage.getItem('color-theme') || 'default';
    if (storedColorThemeHero !== 'default') {
        document.documentElement.classList.add(`theme-${storedColorThemeHero}`);
    }
}); 