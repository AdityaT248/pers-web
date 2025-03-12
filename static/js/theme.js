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
}); 