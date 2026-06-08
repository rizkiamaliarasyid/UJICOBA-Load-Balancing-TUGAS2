from flask import Flask
import os
import time
import random
import socket

app = Flask(__name__)

@app.route('/')
def home():
    ip_kontainer = socket.gethostbyname(socket.gethostname())
    container_id = socket.gethostname()
    
    if ip_kontainer.endswith('.2'):
        nama_web = "WEB SERVER 1 (web-1)"
        warna_aksen = "#4facfe"
    elif ip_kontainer.endswith('.3'):
        nama_web = "WEB SERVER 2 (web-2)"
        warna_aksen = "#00f2fe"
    elif ip_kontainer.endswith('.4'):
        nama_web = "WEB SERVER 3 (web-3)"
        warna_aksen = "#00ffd0"
    else:
        nama_web = f"WEB SERVER TEMPLATE ({container_id})"
        warna_aksen = "#ff9a9e"

    waktu_proses = 0.1
    time.sleep(waktu_proses)
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scalable Systems Design - Monitor</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #141e30 0%, #243b55 100%);
                color: #fff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
                border: 1px solid rgba(255, 255, 255, 0.1);
                text-align: center;
                width: 460px;
            }}
            h1 {{
                font-size: 26px;
                margin-bottom: 5px;
                text-transform: uppercase;
                letter-spacing: 1.5px;
                color: #ffffff;
            }}
            h2 {{
                font-size: 13px;
                font-weight: 400;
                color: #a0aec0;
                margin-bottom: 35px;
                letter-spacing: 1px;
            }}
            .card {{
                background: rgba(0, 0, 0, 0.3);
                border-radius: 14px;
                padding: 22px;
                margin-bottom: 22px;
                border-left: 6px solid {warna_aksen};
                text-align: left;
                transition: all 0.3s ease;
            }}
            .card-label {{
                font-size: 11px;
                color: #a0aec0;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            .card-value {{
                font-size: 22px;
                font-weight: 700;
                letter-spacing: 0.5px;
                margin-top: 5px;
            }}
            .small-text {{
                font-size: 12px;
                color: #718096;
                font-family: monospace;
                margin-top: 4px;
            }}
            .footer {{
                font-size: 11px;
                color: #a0aec0;
                margin-top: 30px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                padding-top: 20px;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Load Balancing Monitor</h1>
            <h2>SCALABLE SYSTEMS DESIGN</h2>
            
            <div class="card">
                <div class="card-label">Target Routing</div>
                <div class="card-value" style="color: {warna_aksen};">{nama_web}</div>
                <div class="small-text">Container ID: {container_id} | IP: {ip_kontainer}</div>
            </div>

            <div class="card" style="border-left-color: #cbd5e0;">
                <div class="card-label">Execution Performance</div>
                <div class="card-value" style="color: #fff;">{waktu_proses} Seconds</div>
                <div class="small-text">Simulated Dynamic Workload</div>
            </div>

            <div class="footer">
                <strong>RIZKI AMALIA RASYID RIDHA</strong><br>
                NIM: 105841121223 | Kelas: 6rpl-A<br>
                Informatika - Universitas Muhammadiyah Makassar
            </div>
        </div>
    </body>
    </html>
    """
    return html_template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)