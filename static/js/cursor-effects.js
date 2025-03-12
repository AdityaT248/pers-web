document.addEventListener('DOMContentLoaded', function() {
    // Create cursor elements
    const cursorOuter = document.createElement('div');
    cursorOuter.classList.add('cursor-outer');
    const cursorInner = document.createElement('div');
    cursorInner.classList.add('cursor-inner');
    
    document.body.appendChild(cursorOuter);
    document.body.appendChild(cursorInner);
    
    // Track mouse movement
    document.addEventListener('mousemove', function(e) {
        cursorOuter.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
        cursorInner.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
    });
    
    // Add hover effect for interactive elements
    const interactiveElements = document.querySelectorAll('a, button, .interactive');
    interactiveElements.forEach(element => {
        element.addEventListener('mouseenter', () => {
            cursorOuter.classList.add('cursor-hover');
            cursorInner.classList.add('cursor-hover');
        });
        
        element.addEventListener('mouseleave', () => {
            cursorOuter.classList.remove('cursor-hover');
            cursorInner.classList.remove('cursor-hover');
        });
    });
}); 