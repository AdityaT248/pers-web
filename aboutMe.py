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
                animation: fadeIn 1s ease-in-out, glow 1.5s ease-in-out infinite alternate;
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
                transform: translateY(-10px) scale(1.05);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
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
                cursor: button;
                transition: background 0.3s ease;
            }
            .dark-mode-toggle:hover {
                background: #FDE047;
            }
            .dark-mode {
                background: #121212;
                color: #e0e0e0;
            }
            .dark-mode nav {
                background: #1f1f1f;
            }
            .dark-mode .hero {
                background: linear-gradient(rgba(31, 31, 31, 0.7), rgba(31, 31, 31, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
                color: #e0e0e0;
            }
            .dark-mode .card {
                background: #1f1f1f;
                color: #e0e0e0;
            }
            .dark-mode .skills, .dark-mode .contact {
                background: #1f1f1f;
                color: #e0e0e0;
            }
            .dark-mode footer {
                background: #1f1f1f;
                color: #e0e0e0;
            }
            .dark-mode .footer-links a {
                color: #bb86fc;
            }
            .dark-mode .footer-links a:hover {
                color: #e0e0e0;
            }
            .dark-mode .scroll-to-top {
                background: #bb86fc;
                color: #121212;
            }
            .dark-mode .scroll-to-top:hover {
                background: #3700b3;
            }
            .dark-mode .color-scheme-toggle {
                background: #bb86fc;
                color: #121212;
            }
            .dark-mode .color-scheme-toggle:hover {
                background: #3700b3;
            }
            .dark-mode .go-back-button {
                background: linear-gradient(135deg, #bb86fc, #3700b3);
                color: #121212;
                border: none;
                padding: 16px 32px; /* Increased padding */
                font-size: 1.2em; /* Increased font size */
                border-radius: 24px; /* More rounded corners */
                cursor: pointer;
                transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* Increased shadow */
                position: relative;
                overflow: hidden;
            }
            .dark-mode .go-back-button::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(255, 255, 255, 0.1);
                opacity: 0;
                transition: opacity 0.3s ease;
            }
            .dark-mode .go-back-button:hover::before {
                opacity: 1;
            }
            .dark-mode .go-back-button:hover {
                background: linear-gradient(135deg, #3700b3, #bb86fc);
                transform: scale(1.1); /* Increased scale */
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* Increased shadow */
            }
            .dark-mode .go-back-button:active {
                transform: scale(0.95);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            .dark-mode .go-back-button span {
                position: relative;
                z-index: 1;
                margin-left: -10px; /* Move the arrow to the left */
            }
            .dark-mode .go-back-button::after {
                content: '';
                position: absolute;
                top: 50%;
                left: 50%;
                width: 300%;
                height: 300%;
                background: radial-gradient(circle, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0));
                transition: width 0.3s ease, height 0.3s ease, top 0.3s ease, left 0.3s ease;
                transform: translate(-50%, -50%);
                opacity: 0;
            }
            .dark-mode .go-back-button:hover::after {
                width: 100%;
                height: 100%;
                top: 50%;
                left: 50%;
                opacity: 1;
            }
            .dark-mode .highlighted::before {
                border-color: #bb86fc;
            }
            .dark-mode .highlighted {
                box-shadow: 0 0 20px #bb86fc;
            }
            .dark-mode .highlighted::before {
                box-shadow: 0 0 20px #bb86fc;
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
                    text-shadow: 0 0 20px #38BDF8, 0 0 30px #38BDF8, 0 0 40px #38BDF8, 0 0 50px #38BDF8, 0 0 60px #38BDF8, 0 0 70px #38BDF8;
                }
            }
            .card-link {
                display: block;
                color: inherit;
                text-decoration: none;
            }
            .card-link:hover {
                text-decoration: none;
            }
            .usaco-details {
                background: #ffffff;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 40px;
                text-align: center;
                animation: fadeIn 1s ease-in-out;
            }
            .usaco-details h2 {
                color: #F97316;
            }
            .highlighted {
                position: relative;
                animation: pulse 1.5s infinite, glow 1.5s ease-in-out infinite alternate, bounce 2s infinite;
            }
            @keyframes pulse {
                0% {
                    box-shadow: 0 0 0 0 rgba(249, 115, 22, 0.4);
                }
                70% {
                    box-shadow: 0 0 30px 30px rgba(249, 115, 22, 0);
                }
                100% {
                    box-shadow: 0 0 0 0 rgba(249, 115, 22, 0);
                }
            }
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% {
                    transform: translateY(0);
                }
                40% {
                    transform: translateY(-20px);
                }
                60% {
                    transform: translateY(-10px);
                }
            }
            .highlighted::before {
                content: '';
                position: absolute;
                top: -20px;
                left: -20px;
                right: -20px;
                bottom: -20px;
                border: 6px dashed #F97316;
                border-radius: 20px;
                animation: dash 2s linear infinite, glow 1.5s ease-in-out infinite alternate;
                z-index: -1; /* Ensure the pseudo-element is behind the content */
            }
            @keyframes dash {
                to {
                    stroke-dashoffset: 1000;
                }
            }
            @keyframes glow {
                from {
                    box-shadow: 0 0 10px #F97316, 0 0 20px #F97316, 0 0 30px #F97316, 0 0 40px #F97316;
                }
                to {
                    box-shadow: 0 0 20px #FDE047, 0 0 30px #FDE047, 0 0 40px #FDE047, 0 0 50px #FDE047;
                }
            }
            .go-back-button {
                display: inline-block;
                padding: 10px 20px;
                margin-top: 20px;
                font-size: 1em;
                font-weight: bold;
                color: #fff;
                background-color: #F97316;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.3s ease;
                z-index: 1; /* Ensure the button is above other elements */
                position: relative; /* Ensure z-index works */
            }
            .go-back-button:hover {
                background-color: #FDE047;
                transform: scale(1.1);
            }
            .default {
                background: #FEF3C7;
                color: #3D3D3D;
            }
            .dark {
                background: #000;
                color: #f0f4f8;
            }
            .dark nav {
                background: #000;
            }
            .dark .hero {
                background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .dark .card {
                background: #222;
                color: #f0f4f8;
            }
            .dark .skills, .dark .contact {
                background: #222;
                color: #f0f4f8;
            }
            .dark footer {
                background: #000;
            }
            .blue {
                background: #E0F7FA;
                color: #00796B;
            }
            .blue nav {
                background: #00796B;
            }
            .blue .hero {
                background: linear-gradient(rgba(0, 121, 107, 0.7), rgba(0, 121, 107, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .blue .card {
                background: #B2EBF2;
                color: #00796B;
            }
            .blue .skills, .blue .contact {
                background: #B2EBF2;
                color: #00796B;
            }
            .blue footer {
                background: #00796B;
            }
            .green {
                background: #E8F5E9;
                color: #388E3C;
            }
            .green nav {
                background: #388E3C;
            }
            .green .hero {
                background: linear-gradient(rgba(56, 142, 60, 0.7), rgba(56, 142, 60, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .green .card {
                background: #C8E6C9;
                color: #388E3C;
            }
            .green .skills, .green .contact {
                background: #C8E6C9;
                color: #388E3C;
            }
            .green footer {
                background: #388E3C;
            }
            /* Add a glowing effect to the hero section */
            .hero {
                animation: glow 1.5s ease-in-out infinite alternate;
            }

            @keyframes glow {
                from {
                    box-shadow: 0 0 10px #F97316, 0 0 20px #F97316, 0 0 30px #F97316, 0 0 40px #F97316;
                }
                to {
                    box-shadow: 0 0 20px #FDE047, 0 0 30px #FDE047, 0 0 40px #FDE047, 0 0 50px #FDE047;
                }
            }

            /* Add a hover effect to the cards */
            .card:hover {
                transform: translateY(-10px) scale(1.05);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }

            /* Add a smooth scroll effect */
            html {
                scroll-behavior: smooth;
            }

            /* Add a fade-in effect to the sections */
            .fade-in {
                opacity: 0;
                animation: fadeIn 1s forwards;
            }

            @keyframes fadeIn {
                to {
                    opacity: 1;
                }
            }

            /* Ensure skills section is readable in dark mode */
            .dark-mode .skills {
                color: #ff0000; /* Change font color to red */
            }
        </style>
    </head>
    <body class="animated-background">
        <select class="color-scheme-toggle" onchange="changeColorScheme(this.value)">
            <option value="default">Default</option>
            <option value="dark">Dark Mode</option>
            <option value="blue">Blue Theme</option>
            <option value="green">Green Theme</option>
        </select>
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
                <h1>"First, learn the system. Then, break the system. Finally, build a better one." - Aditya Thakkar</h1>
                <p>A glimpse into my journey in coding, robotics, and leadership.</p>
            </div>
            <div class="content">
                <div class="card" style="margin-bottom: 40px;">
                    <h2>Scouting Achievements</h2>
                    <p>I am a Life Scout and almost an Eagle Scout. Scouting has taught me valuable skills and leadership qualities.</p>
                    <a href="#scouting-details" class="animated-button" onclick="highlightSection('scouting-details')">Learn More</a>
                    <a href="https://www.scouting.org/" target="_blank">Visit scouting.org</a>
                </div>
                <div class="card" style="margin-bottom: 40px;">
                    <h2>Volunteering</h2>
                    <p>I have actively participated in various volunteering activities, contributing to community service and development.</p>
                    <a href="#volunteering-details" class="animated-button" onclick="highlightSection('volunteering-details')">Learn More</a>
                    <a href="https://www.atriaseniorliving.com/" target="_blank">Atria Senior Living</a>
                </div>
                <div class="card" style="margin-bottom: 40px;">
                    <h2>USACO Achievements</h2>
                    <p>I have achieved the USACO Silver level, showcasing my skills in competitive programming and problem-solving.</p>
                    <a href="#usaco-details" class="animated-button" onclick="highlightSection('usaco-details')">Learn More</a>
                    <a href="http://www.usaco.org/" target="_blank">Visit usaco.org</a>
                </div>
                <div class="card" style="margin-bottom: 40px;">
                    <h2>FRC Robotics</h2>
                    <p>I am part of Bellarmine's world champion FRC Team, the Cheesy Poofs. (software division)</p>
                    <a href="#frc-details" class="animated-button" onclick="highlightSection('frc-details')">Learn More</a>
                    <a href="https://www.team254.com/" target="_blank">Visit team254.com</a>
                </div>
            </div>
            <div class="parallax">
                <h2>Explore More</h2>
            </div>
            <div class="skills fade-in" id="skills" style="margin-bottom: 40px;">
                <h2>Skills</h2>
                <ul>
                    <li>Leadership</li>
                    <li>Programming (Python, Java, fastHTML)</li>
                    <li>Robotics</li>
                    <li>Problem Solving</li>
                    <li>Teamwork</li>
                </ul>
            </div>
            <div class="scouting-details card fade-in" id="scouting-details" style="margin-bottom: 40px;">
                <h2>Scouting Achievements</h2>
                <p>As a Life Scout nearing Eagle Scout, I’ve developed strong leadership and problem-solving skills through hands-on experiences. During a 7-day campout at Camp Oljato, I led a project to dig up an exposed water pipe, coordinating a team of scouts and keeping morale high despite the heat and tough conditions. Seeing the campsite transformed after all our hard work was incredibly rewarding. On another occasion, I organized a beach cleanup during a 3-day campout, where we had to adapt to unexpected challenges like bad weather and a shortage of supplies. These experiences taught me resilience, adaptability, and the importance of giving back to the community. Scouting has shaped my ability to lead, work as a team, and stay determined even when things don’t go as planned.</p>
                <button class="go-back-button" onclick="revertHighlight('scouting-details')">Go Back</button>
            </div>
            <div class="volunteering-details card fade-in" id="volunteering-details" style="margin-bottom: 40px;">
                <h2>Volunteering Experience</h2>
                <p>Over the summer, I had the opportunity to volunteer at ATRIA Senior Living, where I assisted seniors with their daily activities and helped organize events to enrich their lives. This experience allowed me to develop strong communication and interpersonal skills as I engaged with residents, listened to their stories, and ensured they felt valued and supported. I also learned the importance of patience, empathy, and adaptability while assisting individuals with varying needs. Through event planning and coordination, I honed my organizational and leadership abilities, ensuring activities ran smoothly and were enjoyable for everyone. This experience not only deepened my appreciation for community service but also reinforced my ability to work in a team-oriented environment while making a meaningful impact on others’ lives.</p>
                <button class="go-back-button" onclick="revertHighlight('volunteering-details')">Go Back</button>
            </div>
            <div class="usaco-details card fade-in" id="usaco-details" style="margin-bottom: 40px;">
                <h2>USACO Achievements</h2>
                <p>I reached the USACO Silver level, which was a big milestone in my competitive programming journey. Getting there took a lot of problem-solving, persistence, and creative thinking. Along the way, I sharpened my skills in algorithms and data structures, learning how to break down complex problems and find efficient solutions under time constraints. Competing in USACO also taught me how to think critically and approach challenges methodically, which has helped me in both academics and real-world coding projects. It’s been a rewarding experience, and I’m excited to keep pushing my skills further.</p>
                <button class="go-back-button" onclick="revertHighlight('usaco-details')">Go Back</button>
            </div>
            <div class="frc-details card fade-in" id="frc-details" style="margin-bottom: 40px;">
                <h2>FRC Robotics</h2>
                <p>Being part of the software team on the world’s #1 FRC robotics team, the Cheesy Poofs, has been one of the most defining experiences in my STEM journey. Robotics isn’t just about building machines—it’s about innovation, teamwork, and solving real-world problems under pressure. I’ve contributed to programming autonomous routines and teleoperated functions, ensuring our robot performs at the highest level in competition. Seeing our code come to life on the field and play a role in our success at the world championships has been incredibly rewarding.

Through FRC, I’ve learned to collaborate with a team of highly skilled engineers, troubleshoot complex issues under tight deadlines, and think critically about software-hardware integration. The fast-paced, high-stakes environment of robotics competitions has strengthened my ability to work under pressure, debug efficiently, and continuously improve my coding skills. Beyond just technical knowledge, FRC has taught me the importance of communication and teamwork—working alongside mechanical and electrical teams to ensure seamless robot performance.

This experience has fueled my passion for AI and machine learning, as I’ve seen firsthand how automation and intelligent systems can make a difference in competitive robotics. Whether it’s optimizing motion paths or improving sensor-based decision-making, I’m excited to continue exploring the intersection of robotics and artificial intelligence in the future.</p>
                <button class="go-back-button" onclick="revertHighlight('frc-details')">Go Back</button>
            </div>
            <div class="contact fade-in" id="contact">
                <h2>Contact</h2>
                <ul>
                    <li>Email: <a href="mailto:aditya.thakkar.2020@gmail.com">aditya.thakkar.2020@gmail.com</a></li>
                    <li>Github: <a href="https://github.com/AdityaT248">https://github.com/AdityaT248</a></li>
                    <li>LinkedIn: <a href="https://www.linkedin.com/in/aditya-thakkar-37206a27a/" target="_blank">https://www.linkedin.com/in/aditya-thakkar-37206a27a/</a></li>
                </ul>
            </div>
            <footer>
                <p>&copy; 2025 Aditya Thakkar. All rights reserved.</p>
                <div class="footer-links">
                    <a href="mailto:aditya.thakkar.2020@gmail.com">Email me</a>
                    <a href="https://github.com/AdityaT248">Github</a>
                    <a href="https://www.linkedin.com/in/aditya-thakkar-37206a27a/" target="_blank">Connect on LinkedIn</a>
                </div>
            </footer>
         <script>
            function changeColorScheme(scheme) {
                document.body.className = scheme;
            }
            function scrollToTop() {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
            function highlightSection(id) {
                const section = document.getElementById(id);
                section.style.transition = 'background-color 0.5s ease, box-shadow 0.5s ease, border 0.5s ease, font-size 0.5s ease, font-weight 0.5s ease, transform 0.5s ease';
                section.style.backgroundColor = '#FFF3CD';
                section.style.boxShadow = '0 0 30px rgba(0, 0, 0, 0.5)';
                section.style.border = '6px solid #F97316';
                section.style.borderRadius = '20px';
                section.style.fontSize = '1.2em';
                section.style.fontWeight = 'bold';
                section.style.padding = '40px'; // Increased padding
                section.style.transform = 'scale(1.05)';
                section.classList.add('highlighted');
            }
            function revertHighlight(id) {
                const section = document.getElementById(id);
                section.style.backgroundColor = '';
                section.style.boxShadow = '';
                section.style.border = '';
                section.style.fontSize = '';
                section.style.fontWeight = '';
                section.style.padding = '20px'; // Reset padding
                section.style.transform = 'scale(1)';
                section.classList.remove('highlighted');
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

            // Add a fade-in effect to the sections when they come into view
            const sections = document.querySelectorAll('.fade-in');
            const options = {
                threshold: 0.1
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, options);

            sections.forEach(section => {
                observer.observe(section);
            });

            // Add a smooth scroll effect to the navigation links
            document.querySelectorAll('nav a').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
        </script>
        <style>
            .color-scheme-toggle {
                position: fixed;
                top: 80px;
                right: 20px;
                background: #F97316;
                color: #fff;
                border: none;
                padding: 10px;
                border-radius: 5px;
                cursor: pointer;
                transition: background 0.3s ease;
            }
            .color-scheme-toggle:hover {
                background: #FDE047;
            }
            .highlighted {
                position: relative;
                animation: pulse 1.5s infinite, glow 1.5s ease-in-out infinite alternate, bounce 2s infinite;
            }
            @keyframes pulse {
                0% {
                    box-shadow: 0 0 0 0 rgba(249, 115, 22, 0.4);
                }
                70% {
                    box-shadow: 0 0 30px 30px rgba(249, 115, 22, 0);
                }
                100% {
                    box-shadow: 0 0 0 0 rgba(249, 115, 22, 0);
                }
            }
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% {
                    transform: translateY(0);
                }
                40% {
                    transform: translateY(-20px);
                }
                60% {
                    transform: translateY(-10px);
                }
            }
            .highlighted::before {
                content: '';
                position: absolute;
                top: -20px;
                left: -20px;
                right: -20px;
                bottom: -20px;
                border: 6px dashed #F97316;
                border-radius: 20px;
                animation: dash 2s linear infinite, glow 1.5s ease-in-out infinite alternate;
                z-index: -1; /* Ensure the pseudo-element is behind the content */
            }
            @keyframes dash {
                to {
                    stroke-dashoffset: 1000;
                }
            }
            @keyframes glow {
                from {
                    box-shadow: 0 0 10px #F97316, 0 0 20px #F97316, 0 0 30px #F97316, 0 0 40px #F97316;
                }
                to {
                    box-shadow: 0 0 20px #FDE047, 0 0 30px #FDE047, 0 0 40px #FDE047, 0 0 50px #FDE047;
                }
            }
            .go-back-button {
                display: inline-block;
                padding: 10px 20px;
                margin-top: 20px;
                font-size: 1em;
                font-weight: bold;
                color: #fff;
                background-color: #F97316;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.3s ease;
                z-index: 1; /* Ensure the button is above other elements */
                position: relative; /* Ensure z-index works */
            }
            .go-back-button:hover {
                background-color: #FDE047;
                transform: scale(1.1);
            }
        </style>
    </body>
    </html>
    """
    return content