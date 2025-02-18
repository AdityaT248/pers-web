from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Aditya Thakkar - Personal website showcasing achievements in coding, robotics, and scouting.">
        <title>Aditya Thakkar</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #FEF3C7;
                color: #3D3D3D;
                scroll-behavior: smooth;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            nav {
                background: #F97316;
                padding: 15px 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                color: #fff;
                position: sticky;
                top: 0;
                z-index: 1000;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            nav a {
                color: #fff;
                text-decoration: none;
                margin: 0 10px;
                transition: color 0.3s ease;
            }
            nav a:hover {
                color: #FDE047;
            }
            .hero {
                background: linear-gradient(rgba(249, 115, 22, 0.7), rgba(249, 115, 22, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
                padding: 100px 20px;
                text-align: center;
                color: #fff;
                border-radius: 15px;
                margin-bottom: 40px;
                position: relative;
                overflow: hidden;
                animation: fadeIn 1s ease-in-out;
            }
            .hero h1 {
                margin: 0;
                font-size: 5em;
                font-weight: bold;
                z-index: 1;
                position: relative;
                animation: popUp 1s ease-in-out;
            }
            .hero p {
                font-size: 2em;
                z-index: 1;
                position: relative;
                animation: popUp 1.2s ease-in-out;
            }
            .content {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                justify-content: center;
                animation: fadeIn 1s ease-in-out;
            }
            .card {
                background: #ffffff;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                text-align: center;
                position: relative;
                overflow: hidden;
                animation: popUp 1.4s ease-in-out;
            }
            .card:hover {
                transform: translateY(-10px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            }
            .card h2 {
                margin-top: 0;
                color: #F97316;
            }
            .card p {
                margin: 0;
                color: #666;
            }
            .card a {
                display: inline-block;
                margin-top: 10px;
                padding: 12px 24px;
                background-color: #FDE047;
                color: #fff;
                text-decoration: none;
                border-radius: 8px;
                transition: background-color 0.3s ease;
            }
            .card a:hover {
                background-color: #F97316;
            }
            .skills, .contact {
                background: #ffffff;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 40px;
                text-align: center;
                animation: fadeIn 1s ease-in-out;
            }
            .skills h2, .contact h2 {
                color: #F97316;
            }
            .skills ul, .contact ul {
                list-style: none;
                padding: 0;
                margin: 0;
            }
            .skills li, .contact li {
                background: #FEF3C7;
                margin: 10px 0;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .skills li:hover, .contact li:hover {
                transform: translateY(-5px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            .contact a {
                color: #F97316;
                text-decoration: none;
            }
            .contact a:hover {
                text-decoration: underline;
            }
            footer {
                text-align: center;
                padding: 20px;
                background: #F97316;
                color: #fff;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 40px;
                animation: fadeIn 1s ease-in-out;
            }
            .footer-links {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-top: 10px;
            }
            .footer-links a {
                color: #fff;
                text-decoration: none;
                transition: color 0.3s ease;
            }
            .footer-links a:hover {
                color: #EAB308;
            }
            .dark-mode-toggle {
                position: fixed;
                top: 80px; /* Adjusted from 60px to 80px */
                right: 20px;
                background: #F97316;
                color: #fff;
                border: none;
                padding: 10px;
                border-radius: 5px;
                cursor: pointer;
                transition: background 0.3s ease;
            }
            .dark-mode-toggle:hover {
                background: #FDE047;
            }
            .dark-mode {
                background: #000;
                color: #f0f4f8;
            }
            .dark-mode nav {
                background: #000;
            }
            .dark-mode .hero {
                background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .dark-mode .card {
                background: #222;
                color: #f0f4f8;
            }
            .dark-mode .skills, .dark-mode .contact {
                background: #222;
                color: #f0f4f8;
            }
            .dark-mode footer {
                background: #000;
            }
            @keyframes fadeIn {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }
            @keyframes popUp {
                0% {
                    transform: scale(0.8);
                    opacity: 0;
                }
                100% {
                    transform: scale(1);
                    opacity: 1;
                }
            }
            @keyframes slideIn {
                from {
                    transform: translateX(-100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            @keyframes rotateIn {
                from {
                    transform: rotate(-360deg);
                    opacity: 0;
                }
                to {
                    transform: rotate(0);
                    opacity: 1;
                }
            }
            @keyframes bounceIn {
                0%, 20%, 50%, 80%, 100% {
                    transform: translateY(0);
                }
                40% {
                    transform: translateY(-30px);
                }
                60% {
                    transform: translateY(-15px);
                }
            }
            .hero, .content, .skills, .contact, footer {
                animation: fadeIn 1s ease-in-out;
            }
            .card {
                animation: slideIn 1s ease-in-out;
            }
            .logo {
                font-size: 1.5em;
                font-weight: bold;
                animation: popUp 1s ease-in-out;
            }
            .nav-links a {
                animation: popUp 1.2s ease-in-out;
            }
            .hero h1, .hero p {
                animation: popUp 1.4s ease-in-out;
            }
            .skills, .contact {
                animation: fadeIn 1.6s ease-in-out;
            }
            .footer-links a {
                animation: popUp 1.8s ease-in-out;
            }
            .scroll-to-top {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background: #F97316;
                color: #fff;
                border: none;
                padding: 10px;
                border-radius: 5px;
                cursor: pointer;
                transition: background 0.3s ease;
                display: none;
                animation: bounceIn 2s infinite;
            }
            .scroll-to-top:hover {
                background: #FDE047;
            }
            .parallax {
                background: url('https://via.placeholder.com/1200x800') no-repeat center center/cover;
                height: 400px;
                position: relative;
                background-attachment: fixed;
                background-size: cover;
                animation: fadeIn 1s ease-in-out;
            }
            .parallax h2 {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: #fff;
                font-size: 3em;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
                animation: popUp 1.5s ease-in-out;
            }
            .animated-button {
                display: inline-block;
                padding: 12px 24px;
                margin-top: 20px;
                font-size: 1em;
                font-weight: bold;
                color: #fff;
                background-color: #FDE047;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.3s ease;
                animation: rotateIn 1s ease-in-out;
            }
            .animated-button:hover {
                background-color: #F97316;
                transform: scale(1.1);
            }
            .animated-background {
                background: linear-gradient(270deg, #F97316, #FDE047, #38BDF8);
                background-size: 600% 600%;
                animation: gradientShift 10s ease infinite;
            }
            @keyframes gradientShift {
                0% {
                    background-position: 0% 50%;
                }
                50% {
                    background-position: 100% 50%;
                }
                100% {
                    background-position: 0% 50%;
                }
            }
            .animated-text {
                display: inline-block;
                font-size: 2em;
                font-weight: bold;
                color: #FDE047;
                animation: textGlow 1.5s ease-in-out infinite alternate;
            }
            @keyframes textGlow {
                from {
                    text-shadow: 0 0 10px #FDE047, 0 0 20px #FDE047, 0 0 30px #FDE047, 0 0 40px #FDE047, 0 0 50px #FDE047, 0 0 60px #FDE047, 0 0 70px #FDE047;
                }
                to {
                    text-shadow: 0 0 20px #38BDF8, 0 0 30px #38BDF8, 0 0 40px #38BDF8, 0 0 50px #38BDF8, 0 0 60px #38BDF8, 0 0 70px #38BDF8, 0 0 80px #38BDF8;
                }
            }
        </style>
    </head>
    <body class="animated-background">
        <button class="dark-mode-toggle" onclick="toggleDarkMode()">Toggle Dark Mode</button>
        <button class="scroll-to-top" onclick="scrollToTop()">Scroll to Top</button>
        <nav>
            <div class="logo">Aditya Thakkar</div>
            <div class="nav-links">
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#contact">Contact</a>
            </div>
        </nav>
        <div class="container">
            <div class="hero">
                <h1>Welcome to My Personal Website</h1>
                <p>A glimpse into my journey in coding, robotics, and leadership.</p>
                <button class="animated-button">Learn More</button>
            </div>
            <div class="content">
                <div class="card">
                    <h2>Scouting Achievements</h2>
                    <p>I am a Life Scout and almost an Eagle Scout. Scouting has taught me valuable skills and leadership qualities.</p>
                    <a href="https://www.scouting.org/" target="_blank">Visit the scouting website</a>
                </div>
                <div class="card">
                    <h2>USACO Achievements</h2>
                    <p>I have achieved the USACO Silver level, showcasing my skills in competitive programming and problem-solving.</p>
                    <a href="http://www.usaco.org/" target="_blank">Visit usaco.org</a>
                </div>
                <div class="card">
                    <h2>FRC Robotics</h2>
                    <p>I am part of Bellarmine's world champion FRC Team, the Cheesy Poofs. (software division)</p>
                    <a href="https://www.team254.com/" target="_blank">Learn More</a>
                </div>
            </div>
            <div class="parallax">
                <h2>Explore More</h2>
            </div>
            <div class="skills" id="skills">
                <h2>Skills</h2>
                <ul>
                    <li>Leadership</li>
                    <li>Programming (Python, Java, fastHTML)</li>
                    <li>Robotics</li>
                    <li>Problem Solving</li>
                    <li>Teamwork</li>
                </ul>
            </div>
            <div class="contact" id="contact">
                <h2>Contact</h2>
                <ul>
                    <li>Email: <a href="mailto:aditya.thakkar.2020@gmail.com">aditya.thakkar.2020@gmail.com</a></li>
                    <li>Phone: <a href="tel:+16508614105">(650) 861-4105</a></li>
                    <li>LinkedIn: <a href="https://www.linkedin.com/in/aditya-thakkar-37206a27a/" target="_blank">https://www.linkedin.com/in/aditya-thakkar-37206a27a/</a></li>
                </ul>
            </div>
            <footer>
                <p>&copy; 2025 Aditya Thakkar. All rights reserved.</p>
                <div class="footer-links">
                    <a href="mailto:aditya.thakkar.2020@gmail.com">Email me</a>
                    <a href="tel:+16508614105">Call</a>
                    <a href="https://www.linkedin.com/in/aditya-thakkar-37206a27a/" target="_blank">Connect on LinkedIn</a>
                </div>
            </footer>
        </div>
        <script>
            function toggleDarkMode() {
                document.body.classList.toggle('dark-mode');
            }
            function scrollToTop() {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
            window.addEventListener('scroll', function() {
                const scrollToTopButton = document.querySelector('.scroll-to-top');
                if (window.scrollY > 300) {
                    scrollToTopButton.style.display = 'block';
                } else {
                    scrollToTopButton.style.display = 'none';
                }
            });
        </script>
    </body>
    </html>
    """
    return content