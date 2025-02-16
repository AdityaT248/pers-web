from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aditya Thakkar</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f0f4f8;
                color: #333;
                scroll-behavior: smooth;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            nav {
                background: #0071e3;
                padding: 10px 20px;
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
                color: #ccc;
            }
            .hero {
                background: url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
                padding: 100px 20px;
                text-align: center;
                color: #fff;
                border-radius: 15px;
                margin-bottom: 40px;
                position: relative;
                overflow: hidden;
            }
            .hero::after {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.5);
                pointer-events: none;
            }
            .hero h1 {
                margin: 0;
                font-size: 4em;
                z-index: 1;
                position: relative;
            }
            .hero p {
                font-size: 1.5em;
                z-index: 1;
                position: relative;
            }
            .content {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                justify-content: center;
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
            }
            .card:hover {
                transform: translateY(-10px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            }
            .card h2 {
                margin-top: 0;
                color: #0071e3;
            }
            .card p {
                margin: 0;
                color: #666;
            }
            .card a {
                display: inline-block;
                margin-top: 10px;
                padding: 10px 20px;
                background-color: #0071e3;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            .card a:hover {
                background-color: #005bb5;
            }
            .skills, .contact {
                background: #ffffff;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 40px;
                text-align: center;
            }
            .skills h2, .contact h2 {
                color: #0071e3;
            }
            .skills ul, .contact ul {
                list-style: none;
                padding: 0;
                margin: 0;
            }
            .skills li, .contact li {
                background: #f0f4f8;
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
                color: #0071e3;
                text-decoration: none;
            }
            .contact a:hover {
                text-decoration: underline;
            }
            footer {
                text-align: center;
                padding: 20px;
                background: #0071e3;
                color: #fff;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 40px;
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
                color: #ccc;
            }
        </style>
    </head>
    <body>
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
                <p>Discover my achievements, skills, and how to contact me.</p>
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
    </body>
    </html>
    """
    return content