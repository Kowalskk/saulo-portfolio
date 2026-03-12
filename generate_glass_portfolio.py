import re
import os

input_file = r'c:\Users\torra\OneDrive\Documentos\Curriculum\saulo_torrado_portfolio v2.html'
output_file = r'c:\Users\torra\OneDrive\Documentos\Curriculum\saulo_torrado_portfolio_glass.html'

with open(input_file, 'r', encoding='utf-8') as f:
    html = f.read()

new_bg = '''
<!-- GLASS BACKGROUND AND TROVE VISUALS -->
<div class="video-bg-container">
  <img src="../../.gemini/antigravity/brain/0db16d90-6510-43e2-8727-23ec0654d68d/saulo_bg_nodes_1773246053463.png" id="bg-video" alt="Deep web3 abstract nodes background">
  <div class="glass-overlay"></div>
</div>

<div class="glass-obj obj-1">
  <img src="../../.gemini/antigravity/brain/0db16d90-6510-43e2-8727-23ec0654d68d/saulo_sphere_green_1773246070879.png" alt="Glowing green liquid sphere">
</div>
<div class="glass-obj obj-2">
  <img src="../../.gemini/antigravity/brain/0db16d90-6510-43e2-8727-23ec0654d68d/saulo_abstract_data_1773246086960.png" alt="Crystal neon purple and cyan structure">
</div>
<div class="glass-obj obj-3">
  <img src="Trove visuals/G_C-NUbWkAEnG4W.jpg" alt="">
</div>
<div class="noise-overlay" style="opacity: 0.2;"></div>
'''

enhanced_glass_css = """
/* ═══════════ TROVE VISUALS & ENHANCED GLASS ═══════════ */
:root {
  --bg: #050507;
  --glass-bg: rgba(20, 20, 30, 0.25);
  --glass-bg-strong: rgba(40, 40, 60, 0.45);
  --glass-border: rgba(255, 255, 255, 0.2);
  --glass-border-subtle: rgba(255, 255, 255, 0.08);
  --glass-shadow: rgba(0, 0, 0, 0.5);
  --glass-inner-glow: rgba(255, 255, 255, 0.15);
  --text: #ffffff;
  --text-mid: #e2e2e5;
  --text-dim: #b0b0b8;
  --text-muted: #80808a;
  --accent: #7af5c0;
}

body {
  background: var(--bg) !important;
  color: var(--text) !important;
}

.video-bg-container {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  z-index: 0;
  pointer-events: none;
}

#bg-video {
  width: 100%; height: 100%;
  object-fit: cover;
  opacity: 0.6;
  filter: saturate(1.2) contrast(1.1);
}

.glass-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, transparent 0%, rgba(5,5,7,0.85) 100%);
}

/* Floating Trove Objects */
.glass-obj {
  position: fixed;
  z-index: 0;
  border-radius: 40px;
  overflow: hidden;
  opacity: 0.8;
  mix-blend-mode: screen;
  pointer-events: none;
  filter: blur(1px);
  border: 1px solid rgba(255,255,255,0.1);
  animation: floatHover 15s ease-in-out infinite alternate;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}
.glass-obj video, .glass-obj img {
  width: 100%; height: 100%;
  object-fit: cover;
}

.obj-1 { width: 400px; height: 400px; top: -100px; right: -50px; animation-duration: 25s; filter: blur(3px); }
.obj-2 { width: 280px; height: 280px; bottom: 5%; left: -60px; animation-duration: 20s; animation-direction: alternate-reverse; border-radius: 50%; }
.obj-3 { width: 180px; height: 180px; top: 40%; right: 10%; animation-duration: 22s; border-radius: 20px;}

@keyframes floatHover {
  0% { transform: translateY(0) rotate(0deg) scale(1); }
  100% { transform: translateY(-40px) rotate(10deg) scale(1.05); }
}

.glass {
  backdrop-filter: blur(45px) saturate(1.8) !important;
  -webkit-backdrop-filter: blur(45px) saturate(1.8) !important;
  border: 1px solid var(--glass-border) !important;
  box-shadow: 
    0 12px 40px var(--glass-shadow), 
    inset 0 1px 0 var(--glass-inner-glow), 
    inset 0 0 20px rgba(255,255,255,0.03) !important;
  background: var(--glass-bg) !important;
}

.glass:hover {
  background: var(--glass-bg-strong) !important;
  border: 1px solid rgba(255,255,255,0.4) !important;
  box-shadow: 
    0 16px 50px rgba(0,0,0,0.6), 
    inset 0 1px 0 rgba(255,255,255,0.5), 
    inset 0 0 20px rgba(255,255,255,0.08) !important;
  transform: translateY(-4px);
}

nav {
  background: rgba(10, 10, 15, 0.4) !important;
  backdrop-filter: blur(30px) saturate(1.2) !important;
  border: 1px solid rgba(255,255,255,0.15) !important;
}

.nav-links a { color: var(--text-dim) !important; }
.nav-links a:hover { color: #fff !important; }
.nav-logo, .hero-name, .section-title { color: #fff !important; }

.hero-avatar {
  background: rgba(255,255,255,0.05) !important;
  border: 1px solid rgba(255,255,255,0.2) !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 0 20px rgba(255,255,255,0.08) !important;
}
.hero-avatar span { color: #fff; }

.social-pill, .stat-chip, .contact-btn-glass {
  background: rgba(255,255,255,0.05) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
  color: var(--text-mid) !important;
  backdrop-filter: blur(16px) !important;
}
.social-pill:hover, .contact-btn-glass:hover {
  background: rgba(255,255,255,0.15) !important;
  color: #fff !important;
  border: 1px solid rgba(255,255,255,0.3) !important;
}

.tl-item:hover { background: rgba(255,255,255,0.05) !important; }
.tag { background: rgba(255,255,255,0.05) !important; color: var(--text-dim) !important; border-color: rgba(255,255,255,0.1) !important; }
.project-card h3, .exp-card h3, .value-card h3, .tool-card h3, .contact-card h2 { color: #fff !important; }

hr { background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent) !important; }

/* Keep the card colored borders/accents slightly visible */
.glass-green { background: linear-gradient(135deg, rgba(86,196,154,0.08), rgba(20,20,30,0.3)) !important; border-top-color: rgba(86,196,154,0.3) !important; }
.glass-blue { background: linear-gradient(135deg, rgba(100,140,255,0.08), rgba(20,20,30,0.3)) !important; border-top-color: rgba(100,140,255,0.3) !important; }
.glass-purple { background: linear-gradient(135deg, rgba(160,120,255,0.08), rgba(20,20,30,0.3)) !important; border-top-color: rgba(160,120,255,0.3) !important; }

.pv-label { color: rgba(255,255,255,0.1) !important; }
.pv-terminal { color: rgba(255,255,255,0.4) !important; }

.about-text strong { color: #fff !important; }
"""

html = re.sub(r'<!-- BACKGROUNDS -->.*?<div class="noise-overlay"></div>', new_bg, html, flags=re.DOTALL)
html = html.replace('</style>', enhanced_glass_css + '\n</style>')
# clean up the old matrix logic
html = re.sub(r'// ═══════════ MATRIX BACKGROUND ═══════════.*?\}\)\(\);', '', html, flags=re.DOTALL)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated new portfolio successfully!")
