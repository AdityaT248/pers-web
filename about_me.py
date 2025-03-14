from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

#@app.get("/", response_class=HTMLResponse)
#@app.api_route("/", methods=["GET", "HEAD"])
@app.api_route("/", methods=["GET", "HEAD"], response_class=HTMLResponse)
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
            /* Ensure Navbar is Responsive */
            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px 20px;
                background: #FF6B35;
                position: sticky;
                top: 0;
                z-index: 1000;
            }

            .nav-links {
                display: flex;
                gap: 15px;
            }

            .nav-links a {
                color: #fff;
                text-decoration: none;
                padding: 10px 15px;
                transition: color 0.3s ease;
            }

            .nav-links a:hover {
                color: #FFD166;
            }
            /* Responsive Text Sizes */
            h1 {
                font-size: 3em;
            }

            h2 {
                font-size: 2em;
            }

            p {
                font-size: 1.1em;
            }

            /* Mobile Adjustments */
            @media (max-width: 768px) {
                h1 {
                    font-size: 2em;
                }

                h2 {
                    font-size: 1.6em;
                }

                p {
                    font-size: 1em;
                }
            }
            img {
                max-width: 100%;
                height: auto;
                display: block;
            }
            button, .resume-button, .resume-nav-button {
                padding: 14px 20px;
                font-size: 1.2em;
            }

            /* Mobile Adjustments */
            @media (max-width: 768px) {
                button, .resume-button, .resume-nav-button {
                    padding: 16px 24px;
                    font-size: 1.4em;
                }
            }
            @media (max-width: 768px) {
                .content {
                    display: flex;
                    flex-direction: column;
                }

                .card {
                    width: 90%;
                    margin: 0 auto 20px;
                }
            }
            @media (max-width: 768px) {
                .hero, .content, .skills, .contact, .card {
                    animation: none !important;
                }
            }






            /* Mobile Menu (Hidden by Default) */
            .menu-toggle {
                display: none;
                background: none;
                color: white;
                font-size: 1.8em;
                border: none;
                cursor: pointer;
            }

            /* Mobile Mode */
            @media (max-width: 768px) {
                .menu-toggle {
                    display: block;
                }

                .nav-links {
                    display: none;
                    flex-direction: column;
                    background: #FF6B35;
                    position: absolute;
                    top: 60px;
                    left: 0;
                    width: 100%;
                    text-align: center;
                    padding: 10px 0;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                }

                .nav-links a {
                    display: block;
                    padding: 15px;
                }

                .nav-links.show {
                    display: flex;
                }
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
                animation: fadeIn 1s ease-in-out, slideInFromLeft 1s ease-in-out;
            }
            .hero h1 {
                margin: 0;
                font-size: 5em;
                font-weight: bold;
                z-index: 1;
                position: relative;
                animation: popUp 1s ease-in-out, bounce 2s infinite;
            }
            .hero p {
                font-size: 2em;
                z-index: 1;
                position: relative;
                animation: popUp 1.2s ease-in-out, fadeIn 2s ease-in-out;
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
                cursor: button;
                transition: background 0.3s ease;
            }
            .dark-mode-toggle:hover {
                background: #FDE047;
            }
            .dark-mode {
                background: #121212;
                color: #e0e0e0;
                transition: background 0.3s ease, color 0.3s ease;
            }
            .dark-mode nav {
                background: #1f1f1f;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
            }
            .dark-mode .hero {
                background: linear-gradient(rgba(31, 31, 31, 0.7), rgba(31, 31, 31, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
                color: #e0e0e0;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            }
            .dark-mode .card {
                background: #1f1f1f;
                color: #e0e0e0;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            }
            .dark-mode .skills, .dark-mode .contact {
                background: #1f1f1f;
                color: #e0e0e0; /* This will not affect the .skills li elements */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            }
            .dark-mode footer {
                background: #1f1f1f;
                color: #e0e0e0;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            }
            .dark-mode .footer-links a {
                color: #bb86fc;
                transition: color 0.3s ease;
            }
            .dark-mode .footer-links a:hover {
                color: #e0e0e0;
            }
            .dark-mode .scroll-to-top {
                background: #bb86fc;
                color: #121212;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            }
            .dark-mode .scroll-to-top:hover {
                background: #3700b3;
            }
            .dark-mode .color-scheme-toggle {
                background: #bb86fc;
                color: #121212;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
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
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.5); /* Increased shadow */
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
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5); /* Increased shadow */
            }
            .dark-mode .go-back-button:active {
                transform: scale(0.95);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
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
            @keyframes slideInFromLeft {
                0% {
                    transform: translateX(-100%);
                    opacity: 0;
                }
                100% {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            @keyframes bounce {
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
            .resume-section {
                text-align: center;
                background: linear-gradient(135deg, #FF6B35, #FFD700);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
                margin-top: 40px;
                cursor: pointer; /* Make entire section clickable */
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }

            .resume-section h2 {
                color: #FFFFFF;
                font-size: 2em;
                font-weight: bold;
                margin-bottom: 10px;
            }

            .resume-section p {
                color: #FFFBEA;
                font-size: 1.2em;
                margin-bottom: 20px;
            }

            /* Resume Button */
            .resume-button {
                display: inline-block;
                padding: 12px 24px;
                background-color: #FFD700;
                color: #000;
                font-weight: bold;
                text-decoration: none;
                font-size: 1.2em;
                border-radius: 8px;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }

            .resume-button:hover {
                background-color: #FF6B35;
                color: #fff;
                transform: scale(1.1);
            }

            /* Hover Effect for Entire Resume Section */
            .resume-section:hover {
                transform: scale(1.03);
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
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
            .dark-mode .highlighted {
                position: relative;
                animation: pulse 1.5s infinite, glow 1.5s ease-in-out infinite alternate, bounce 2s infinite;
            }
            @keyframes pulse {
                0% {
                    box-shadow: 0 0 0 0 rgba(187, 134, 252, 0.4);
                }
                70% {
                    box-shadow: 0 0 30px 30px rgba(187, 134, 252, 0);
                }
                100% {
                    box-shadow: 0 0 0 0 rgba(187, 134, 252, 0);
                }
            }
            @keyframes glow {
                from {
                    box-shadow: 0 0 10px #bb86fc, 0 0 20px #bb86fc, 0 0 30px #bb86fc, 0 0 40px #bb86fc;
                }
                to {
                    box-shadow: 0 0 20px #3700b3, 0 0 30px #3700b3, 0 0 40px #3700b3, 0 0 50px #3700b3;
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
            .dark-mode .highlighted::before {
                content: '';
                position: absolute;
                top: -20px;
                left: -20px;
                right: -20px;
                bottom: -20px;
                border: 6px dashed #bb86fc;
                border-radius: 20px;
                animation: dash 2s linear infinite, glow 1.5s ease-in-out infinite alternate;
                z-index: -1; /* Ensure the pseudo-element is behind the content */
            }
            @keyframes dash {
                to {
                    stroke-dashoffset: 1000;
                }
            }
            .red {
                background: #FFEBEE;
                color: #D32F2F;
            }
            .red nav {
                background: #D32F2F;
            }
            .red .hero {
                background: linear-gradient(rgba(211, 47, 47, 0.7), rgba(211, 47, 47, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .red .card {
                background: #FFCDD2;
                color: #D32F2F;
            }
            .red .skills, .red .contact {
                background: #FFCDD2;
                color: #D32F2F;
            }
            .red footer {
                background: #D32F2F;
            }

            .purple {
                background: #F3E5F5;
                color: #7B1FA2;
            }
            .purple nav {
                background: #7B1FA2;
            }
            .purple .hero {
                background: linear-gradient(rgba(123, 31, 162, 0.7), rgba(123, 31, 162, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .purple .card {
                background: #E1BEE7;
                color: #7B1FA2;
            }
            .purple .skills, .purple .contact {
                background: #E1BEE7;
                color: #7B1FA2;
            }
            .purple footer {
                background: #7B1FA2;
            }
            .night {
                background: #1a1a1a;
                color: #f0f0f0;
            }
            .night nav {
                background: #333;
            }
            .night .hero {
                background: linear-gradient(rgba(26, 26, 26, 0.7), rgba(26, 26, 26, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .night .card {
                background: #2a2a2a;
                color: #f0f0f0;
            }
            .night .skills, .night .contact {
                background: #2a2a2a;
                color: #f0f0f0; /* This will not affect the .skills li elements */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            }
            .night footer {
                background: #333;
            }

            .high-contrast {
                background: #000;
                color: #fff;
            }
            .high-contrast nav {
                background: #000;
            }
            .high-contrast .hero {
                background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
                color: #fff;
            }
            .high-contrast .card {
                background: #000;
                color: #fff;
            }
            .high-contrast .skills, .high-contrast .contact {
                background: #000;
                color: #fff; /* This will not affect the .skills li elements */
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5);
            }
            .high-contrast footer {
                background: #000;
                color: #fff;
            }
            .high-contrast .footer-links a {
                color: #ff0;
                transition: color 0.3s ease;
            }
            .high-contrast .footer-links a:hover {
                color: #fff;
            }
            .high-contrast .scroll-to-top {
                background: #ff0;
                color: #000;
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5);
            }
            .high-contrast .scroll-to-top:hover {
                background: #ff0;
            }
            .high-contrast .color-scheme-toggle {
                background: #ff0;
                color: #000;
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5);
            }
            .high-contrast .color-scheme-toggle:hover {
                background: #ff0;
            }
            .high-contrast .go-back-button {
                background: linear-gradient(135deg, #ff0, #000);
                color: #000;
                border: none;
                padding: 16px 32px; /* Increased padding */
                font-size: 1.2em; /* Increased font size */
                border-radius: 24px; /* More rounded corners */
                cursor: pointer;
                transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
                box-shadow: 0 6px 12px rgba(255, 255, 255, 0.5); /* Increased shadow */
                position: relative;
                overflow: hidden;
            }
            .high-contrast .go-back-button::before {
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
            .high-contrast .go-back-button:hover::before {
                opacity: 1;
            }
            .high-contrast .go-back-button:hover {
                background: linear-gradient(135deg, #000, #ff0);
                transform: scale(1.1); /* Increased scale */
                box-shadow: 0 10px 20px rgba(255, 255, 255, 0.5); /* Increased shadow */
            }
            .high-contrast .go-back-button:active {
                transform: scale(0.95);
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5);
            }
            .high-contrast .go-back-button span {
                position: relative;
                z-index: 1;
                margin-left: -10px; /* Move the arrow to the left */
            }
            .high-contrast .go-back-button::after {
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
            .high-contrast .go-back-button:hover::after {
                width: 100%;
                height: 100%;
                top: 50%;
                left: 50%;
                opacity: 1;
            }
            .high-contrast .highlighted::before {
                border-color: #ff0;
            }
            .high-contrast .highlighted {
                box-shadow: 0 0 20px #ff0;
            }
            .high-contrast .highlighted::before {
                box-shadow: 0 0 20px #ff0;
            }
            .skills li {
                color: #3D3D3D; /* Set a specific color that does not change in dark mode */
            }
            .skills li {
                cursor: pointer;
                position: relative;
                transition: background-color 0.3s ease, color 0.3s ease, transform 0.3s ease;
            }

            .skills li:hover {
                background-color: #FDE047;
                color: #3D3D3D;
                transform: scale(1.05);
            }

            .skills li::after {
                content: '▼';
                position: absolute;
                right: 10px;
                font-size: 0.8em;
                transition: transform 0.3s ease;
            }

            .skills li.expand::after {
                transform: rotate(180deg);
            }
            .color-scheme-toggle {
                transition: background 0.3s ease, color 0.3s ease;
            }
            @keyframes expandAnimation {
                from {
                    max-height: 0;
                    opacity: 0;
                }
                to {
                    max-height: 500px; /* Adjust as needed */
                    opacity: 1;
                }
            }

            @keyframes collapseAnimation {
                from {
                    max-height: 500px; /* Adjust as needed */
                    opacity: 1;
                }
                to {
                    max-height: 0;
                    opacity: 0;
                }
            }

            .expand {
                animation: expandAnimation 0.5s ease-out forwards;
            }

            .collapse {
                animation: collapseAnimation 0.5s ease-out forwards;
            }

            .emphasize {
                font-weight: bold;
                background-color: #FFF3CD;
                padding: 10px;
                border-radius: 5px;
                transition: background-color 0.3s ease, font-weight 0.3s ease;
            }
            
        </style>
        <!-- Add this inside the <head> tag, within the <script> section -->
        <script>
            function toggleLeadershipDetails() {
                const details = document.getElementById('leadership-details');
                const listItem = details.previousElementSibling;
                if (details.style.display === 'none' || details.style.display === '') {
                    details.style.display = 'block';
                    details.classList.add('expand', 'emphasize');
                    details.classList.remove('collapse');
                    listItem.classList.add('expand');
                } else {
                    details.style.display = 'none';
                    details.classList.add('collapse');
                    details.classList.remove('expand', 'emphasize');
                    listItem.classList.remove('expand');
                }
            }
        </script>
        <script>
            function toggleProgrammingDetails() {
                const details = document.getElementById('programming-details');
                const listItem = details.previousElementSibling;
                if (details.style.display === 'none' || details.style.display === '') {
                    details.style.display = 'block';
                    details.classList.add('expand', 'emphasize');
                    details.classList.remove('collapse');
                    listItem.classList.add('expand');
                } else {
                    details.style.display = 'none';
                    details.classList.add('collapse');
                    details.classList.remove('expand', 'emphasize');
                    listItem.classList.remove('expand');
                }
            }
        </script>
        
        <script>
            function toggleRoboticsDetails() {
                const details = document.getElementById('robotics-details');
                const listItem = details.previousElementSibling;
                if (details.style.display === 'none' || details.style.display === '') {
                    details.style.display = 'block';
                    details.classList.add('expand', 'emphasize');
                    details.classList.remove('collapse');
                    listItem.classList.add('expand');
                } else {
                    details.style.display = 'none';
                    details.classList.add('collapse');
                    details.classList.remove('expand', 'emphasize');
                    listItem.classList.remove('expand');
                }
            }
        </script>
        <script>
            function toggleProblemSolvingDetails() {
                const details = document.getElementById('problem-solving-details');
                const listItem = details.previousElementSibling;
                if (details.style.display === 'none' || details.style.display === '') {
                    details.style.display = 'block';
                    details.classList.add('expand', 'emphasize');
                    details.classList.remove('collapse');
                    listItem.classList.add('expand');
                } else {
                    details.style.display = 'none';
                    details.classList.add('collapse');
                    details.classList.remove('expand', 'emphasize');
                    listItem.classList.remove('expand');
                }
            }
        </script>
        <script>
            function toggleTeamworkDetails() {
                const details = document.getElementById('teamwork-details');
                const listItem = details.previousElementSibling;
                if (details.style.display === 'none' || details.style.display === '') {
                    details.style.display = 'block';
                    details.classList.add('expand', 'emphasize');
                    details.classList.remove('collapse');
                    listItem.classList.add('expand');
                } else {
                    details.style.display = 'none';
                    details.classList.add('collapse');
                    details.classList.remove('expand', 'emphasize');
                    listItem.classList.remove('expand');
                }
            }
        </script>
    </head>
    <body class="animated-background">
        <select class="color-scheme-toggle" onchange="changeColorScheme(this.value)">
            <option value="default">Default</option>
            <option value="dark">Dark Mode</option>
            <option value="blue">Blue Theme</option>
            <option value="green">Green Theme</option>
            <option value="red">Red Theme</option>
            <option value="purple">Purple Theme</option>
            <option value="night">Night Mode</option>
            <option value="high-contrast">High Contrast</option>
        </select>
        <button class="scroll-to-top" onclick="scrollToTop()">Scroll to Top</button>
        <nav>
            <div class="logo">Aditya Thakkar</div>
            <button class="menu-toggle" onclick="toggleMenu()">☰</button>
            <div class="nav-links">
                <a href="#skills">Skills</a>
                <a href="#contact">Contact</a>
                <a href="https://docs.google.com/document/d/1eDl1R1TwxLU_MODMobd-a4FZJ1Yaai50viUtW1_HA5M/edit?usp=sharing" target="_blank" class="resume-nav-button">Resume</a>
            </div>
        </nav>

        <div class="container">
            <div class="hero">
                <h1>"First, learn the system. Then, break the system. Finally, build a better one." ― Aditya Thakkar</h1>
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
                <div class="card" style="margin-bottom: 40px;">
                    <h2>My Opinion on AI</h2>
                    <p>For the past few years, AI has become crucial in today's world, and here are my views on it. </p>
                    <a href="#AI-opinion" class="animated-button" onclick="highlightSection('AI-opinion')">Learn More</a>
                </div>
                <div class="card" style="margin-bottom: 40px;">
                    <h2>What Sets Me Apart</h2>
                    <p>My reflection on what makes me different from the others. </p>
                    <a href="#difference" class="animated-button" onclick="highlightSection('difference')">Learn More</a>
                </div>
            </div>
            <div class="parallax">
                <h2>Explore More</h2>
            </div>
            <div class="skills" id="skills" style="margin-bottom: 40px;">
                <h2>Skills</h2>
                <ul>
                    <li onclick="toggleLeadershipDetails()">Leadership</li>
                    <div id="leadership-details" class="collapse" style="display: none; margin-top: 10px;">
                        I’ve built leadership skills by being a Patrol Leader, and using EDGE training to guide my troop. In FRC robotics, I mentor freshmen, and I’ve led volunteer projects at campouts, strengthening my ability to organize and support a team.
                    </div>
                    <li onclick="toggleProgrammingDetails()">Programming (Python, Java, fastHTML)</li>
                    <div id="programming-details" class="collapse" style="display: none; margin-top: 10px;">
                        I’m a USACO Silver competitor and a key programmer for my FRC robotics team. I have experience with multiple languages and constantly seek to expand my coding skills.
                    </div>
                    <li onclick="toggleRoboticsDetails()">Robotics</li>
                    <div id="robotics-details" class="collapse" style="display: none; margin-top: 10px;">
                        I am part of the software team for the #1 FRC robotics team in the world, where I write code, develop tools like a 2D robot visualizer, and collaborate to improve robot functionality.
                    </div>
                    <li onclick="toggleProblemSolvingDetails()">Problem Solving</li>
                    <div id="problem-solving-details" class="collapse" style="display: none; margin-top: 10px;">
                        I excel at problem-solving, using logical and analytical thinking to find solutions to complex issues. My experience in competitive programming and robotics has honed my ability to tackle challenges effectively.
                    </div>
                    <li onclick="toggleTeamworkDetails()">Teamwork</li>
                    <div id="teamwork-details" class="collapse" style="display: none; margin-top: 10px;">
                        I have been working in teams since 5th grade, from FLL to my current role in FRC’s software division. In scouting, I collaborate closely with my patrol, building strong teamwork skills.
                    </div>
                </ul>
            </div>
            <div class="scouting-details card" id="scouting-details" style="margin-bottom: 40px;">
                <h2>Scouting Achievements</h2>
                <p>As a Life Scout nearing Eagle Scout, I’ve developed strong leadership and problem-solving skills through hands-on experiences. During a 7-day campout at Camp Oljato, I led a project to dig up an exposed water pipe, coordinating a team of scouts and keeping morale high despite the heat and tough conditions. Seeing the campsite transformed after all our hard work was incredibly rewarding. On another occasion, I organized a beach cleanup during a 3-day campout, where we had to adapt to unexpected challenges like bad weather and a shortage of supplies. These experiences taught me resilience, adaptability, and the importance of giving back to the community. Scouting has shaped my ability to lead, work as a team, and stay determined even when things don’t go as planned.</p>
                <button class="go-back-button" onclick="revertHighlight('scouting-details')">Go Back</button>
            </div>
            <div class="volunteering-details card" id="volunteering-details" style="margin-bottom: 40px;">
                <h2>Volunteering Experience</h2>
                <p>Over the summer, I had the opportunity to volunteer at ATRIA Senior Living, where I assisted seniors with their daily activities and helped organize events to enrich their lives. This experience allowed me to develop strong communication and interpersonal skills as I engaged with residents, listened to their stories, and ensured they felt valued and supported. I also learned the importance of patience, empathy, and adaptability while assisting individuals with varying needs. Through event planning and coordination, I honed my organizational and leadership abilities, ensuring activities ran smoothly and were enjoyable for everyone. This experience not only deepened my appreciation for community service but also reinforced my ability to work in a team-oriented environment while making a meaningful impact on others’ lives.</p>
                <button class="go-back-button" onclick="revertHighlight('volunteering-details')">Go Back</button>
            </div>
            <div class="usaco-details card" id="usaco-details" style="margin-bottom: 40px;">
                <h2>USACO Achievements</h2>
                <p>I reached the USACO Silver level, which was a big milestone in my competitive programming journey. Getting there took a lot of problem-solving, persistence, and creative thinking. Along the way, I sharpened my skills in algorithms and data structures, learning how to break down complex problems and find efficient solutions under time constraints. Competing in USACO also taught me how to think critically and approach challenges methodically, which has helped me in both academics and real-world coding projects. It’s been a rewarding experience, and I’m excited to keep pushing my skills further.</p>
                <button class="go-back-button" onclick="revertHighlight('usaco-details')">Go Back</button>
            </div>
            <div class="frc-details card" id="frc-details" style="margin-bottom: 40px;">
                <h2>FRC Robotics</h2>
                <p>Being part of the software team on the world’s #1 FRC robotics team, the Cheesy Poofs, has been one of the most defining experiences in my STEM journey. Robotics isn’t just about building machines—it’s about innovation, teamwork, and solving real-world problems under pressure. I’ve contributed to programming autonomous routines and teleoperated functions, ensuring our robot performs at the highest level in competition. Seeing our code come to life on the field and play a role in our success at the world championships has been incredibly rewarding.

                Through FRC, I’ve learned to collaborate with a team of highly skilled engineers, troubleshoot complex issues under tight deadlines, and think critically about software-hardware integration. The fast-paced, high-stakes environment of robotics competitions has strengthened my ability to work under pressure, debug efficiently, and continuously improve my coding skills. Beyond just technical knowledge, FRC has taught me the importance of communication and teamwork—working alongside mechanical and electrical teams to ensure seamless robot performance.</p>
                <button class="go-back-button" onclick="revertHighlight('frc-details')">Go Back</button>
            </div>
            <div class="AI-opinion card" id="AI-opinion" style="margin-bottom: 40px;">
                <h2>My opinion on AI</h2>
                <p>Academic integrity today isn’t just copying answers, it’s about using tools like AI responsibly. AI can be incredibly helpful for brainstorming ideas or debugging code, but I learned that relying on it too much takes away the real experience. This is similar to how tools like mobile phones and the internet changed the way we learn and communicate. At first, they seemed like shortcuts, but over time, people realized their true value came from using them thoughtfully. In competitive programming and FRC robotics, I know that just looking up a solution won’t actually help me improve, it will just get me past the problem faster. If I get stuck, I’ll use it to help me understand a concept or help me develop a strategy for the problem, but I always make sure I can solve the problem and write the code on my own.</p>
                <button class="go-back-button" onclick="revertHighlight('AI-opinion')">Go Back</button>
            </div>
            <div class="Difference card" id="difference" style="margin-bottom: 40px;">
                <h2>What Sets Me Apart</h2>
                <p>What sets me apart is the combination of leadership, teamwork, and perseverance I’ve developed through diverse experiences. As a Life Scout nearing Eagle Scout, I’ve built a strong foundation in leadership and community service. During a 7-day campout at Camp Oljato, I led a project to dig up an exposed water pipe, coordinating scouts and keeping morale high despite tough conditions such as the hot weather. Seeing the campsite transformed after all of our hard work was incredibly rewarding. On another occasion, I organized a beach cleanup during a 3-day campout, overcoming challenges like weather and limited supplies such as trash bags or trash grabbers. From organizing the project to learning how to manage with fewer than expected supplies, these experiences taught me resilience, adaptability, and the value of giving back.
                    Being part of the software team on the world’s #1 FRC robotics team has further shaped my passion for STEM. Robotics isn’t just about building machines—it’s about innovation, teamwork, and solving real-world problems. Contributing to our success at the world championships has honed my technical skills and collaborative abilities.
                    Achieving USACO Silver exemplifies my dedication to problem-solving and continuous learning. The journey from Bronze to Silver was challenging, requiring months of mastering algorithms and building resilience. I’ll never forget the moment I solved my first tough USACO problem after hours of frustration—it fueled my determination to keep improving. </p>
                <button class="go-back-button" onclick="revertHighlight('difference')">Go Back</button>
            </div>
            <div class="contact" id="contact">
                <h2>Contact</h2>
                <ul>
                    <li>Email: <a href="mailto:aditya.thakkar.2020@gmail.com">aditya.thakkar.2020@gmail.com</a></li>
                    <li>Github: <a href="https://github.com/AdityaT248">https://github.com/AdityaT248</a></li>
                    <li>LinkedIn: <a href="https://www.linkedin.com/in/adityathakkar-dev/" target="_blank">https://www.linkedin.com/in/adityathakkar-dev/</a></li>
                </ul>
            </div>
            <div class="resume-section" onclick="window.open('https://docs.google.com/document/d/1eDl1R1TwxLU_MODMobd-a4FZJ1Yaai50viUtW1_HA5M/edit?usp=sharing', '_blank')">
                <h2>My Resume</h2>
                <p>Click anywhere below to view my resume.</p>
                <a href="https://docs.google.com/document/d/1eDl1R1TwxLU_MODMobd-a4FZJ1Yaai50viUtW1_HA5M/edit?usp=sharing" target="_blank" class="resume-button">View Resume</a>
            </div>

            <footer>
                <p>&copy; 2025 Aditya Thakkar. All rights reserved.</p>
                <div class="footer-links">
                    <a href="https://github.com/AdityaT248">Github</a>
                    <a href="https://www.linkedin.com/in/adityathakkar-dev/" target="_blank">Connect on LinkedIn</a>
                </div>
            </footer>
         <script>
            function changeColorScheme(scheme) {
                document.body.className = scheme;
            }
            function scrollToTop() {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }

            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault(); // Prevent instant jump

                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth' });
                    }
                });
            });

            // Function for smooth scroll to top
            function scrollToTop() {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
            function highlightSection(id) {
                const section = document.getElementById(id);

                // Remove any existing transition effects before applying new ones
                section.style.transition = 'none';

                // Force reflow (trick to reset styles)
                void section.offsetWidth;

                // Apply only the highlighting effect (no movement)
                section.style.transition = 'background-color 0.5s ease, box-shadow 0.5s ease, border 0.5s ease, font-size 0.5s ease, font-weight 0.5s ease';
                section.style.backgroundColor = '#FFF3CD';
                section.style.boxShadow = '0 0 30px rgba(0, 0, 0, 0.5)';
                section.style.border = '6px solid #F97316';
                section.style.borderRadius = '20px';
                section.style.fontSize = '1.2em';
                section.style.fontWeight = 'bold';
                section.style.padding = '40px'; // Increased padding

                // Remove transform effect if it was previously applied
                section.style.transform = 'none';
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
            .red {
                background: #FFEBEE;
                color: #D32F2F;
            }
            .red nav {
                background: #D32F2F;
            }
            .red .hero {
                background: linear-gradient(rgba(211, 47, 47, 0.7), rgba(211, 47, 47, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .red .card {
                background: #FFCDD2;
                color: #D32F2F;
            }
            .red .skills, .red .contact {
                background: #FFCDD2;
                color: #D32F2F;
            }
            .red footer {
                background: #D32F2F;
            }

            .purple {
                background: #F3E5F5;
                color: #7B1FA2;
            }
            .purple nav {
                background: #7B1FA2;
            }
            .purple .hero {
                background: linear-gradient(rgba(123, 31, 162, 0.7), rgba(123, 31, 162, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .purple .card {
                background: #E1BEE7;
                color: #7B1FA2;
            }
            .purple .skills, .purple .contact {
                background: #E1BEE7;
                color: #7B1FA2;
            }
            .purple footer {
                background: #7B1FA2;
            }
            .night {
                background: #1a1a1a;
                color: #f0f0f0;
            }
            .night nav {
                background: #333;
            }
            .night .hero {
                background: linear-gradient(rgba(26, 26, 26, 0.7), rgba(26, 26, 26, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
            }
            .night .card {
                background: #2a2a2a;
                color: #f0f0f0;
            }
            .night .skills, .night .contact {
                background: #2a2a2a;
                color: #f0f0f0;
            }
            .night footer {
                background: #333;
            }

            .high-contrast {
                background: #000;
                color: #fff;
            }
            .high-contrast nav {
                background: #000;
            }
            .high-contrast .hero {
                background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://via.placeholder.com/1200x400') no-repeat center center/cover;
                color: #fff;
            }
            .high-contrast .card {
                background: #000;
                color: #fff;
            }
            .high-contrast .skills, .high-contrast .contact {
                background: #000;
                color: #fff; /* This will not affect the .skills li elements */
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5);
            }
            .high-contrast footer {
                background: #000;
                color: #fff;
            }
            .high-contrast .footer-links a {
                color: #ff0;
                transition: color 0.3s ease;
            }
            .high-contrast .footer-links a:hover {
                color: #fff;
            }
            .high-contrast .scroll-to-top {
                background: #ff0;
                color: #000;
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5);
            }
            .high-contrast .scroll-to-top:hover {
                background: #ff0;
            }
            .high-contrast .color-scheme-toggle {
                background: #ff0;
                color: #000;
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5);
            }
            .high-contrast .color-scheme-toggle:hover {
                background: #ff0;
            }
            .high-contrast .go-back-button {
                background: linear-gradient(135deg, #ff0, #000);
                color: #000;
                border: none;
                padding: 16px 32px; /* Increased padding */
                font-size: 1.2em; /* Increased font size */
                border-radius: 24px; /* More rounded corners */
                cursor: pointer;
                transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
                box-shadow: 0 6px 12px rgba(255, 255, 255, 0.5); /* Increased shadow */
                position: relative;
                overflow: hidden;
            }
            .high-contrast .go-back-button::before {
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
            .high-contrast .go-back-button:hover::before {
                opacity: 1;
            }
            .high-contrast .go-back-button:hover {
                background: linear-gradient(135deg, #000, #ff0);
                transform: scale(1.1); /* Increased scale */
                box-shadow: 0 10px 20px rgba(255, 255, 255, 0.5); /* Increased shadow */
            }
            .high-contrast .go-back-button:active {
                transform: scale(0.95);
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.5);
            }
            .high-contrast .go-back-button span {
                position: relative;
                z-index: 1;
                margin-left: -10px; /* Move the arrow to the left */
            }
            .high-contrast .go-back-button::after {
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
            .high-contrast .go-back-button:hover::after {
                width: 100%;
                height: 100%;
                top: 50%;
                left: 50%;
                opacity: 1;
            }
            .high-contrast .highlighted::before {
                border-color: #ff0;
            }
            .high-contrast .highlighted {
                box-shadow: 0 0 20px #ff0;
            }
            .high-contrast .highlighted::before {
                box-shadow: 0 0 20px #ff0;
            }
        </style>
    </body>
    </html>
    """
    return content