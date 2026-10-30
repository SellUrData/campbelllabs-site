import sys
DOMAIN=sys.argv[1] if len(sys.argv)>1 else "campbelllabsllc.com"
def page(path,title,desc,body,on="",depth=0):
    r="../"*depth
    items=[("home","","Company"),("hopps","hopps/","Hopps"),("support","support.html","Contact")]
    nav="".join('<a href="%s%s"%s>%s</a>'%(r,h,' class="on"' if k==on else '',t) for k,h,t in items)
    home=r or './'
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{r}styles.css">
</head>
<body>
<header><div class="wrap"><a class="brand" href="{home}"><img src="{r}assets/logo.svg" alt=""><span>Campbell Labs</span></a><nav>{nav}</nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><span>&copy; 2026 Campbell Labs LLC. All rights reserved.</span><span><a href="{r}privacy.html">Privacy</a><a href="{r}terms.html">Terms</a><a href="{r}support.html">Contact</a></span></div></footer>
</body>
</html>
'''
    open(path,"w").write(html)

page("index.html","Campbell Labs LLC — Software for athletes","Campbell Labs LLC builds mobile software that helps athletes measure and improve performance.",f'''
<div class="wrap hero">
  <div class="eyebrow">Campbell Labs LLC</div>
  <h1>Software that turns your phone into a performance lab.</h1>
  <p class="lead">We build mobile apps that measure athletic performance using on-device computer vision. They need no extra hardware and don't use the cloud, and they're accurate enough to train with.</p>
  <a class="btn" href="hopps/">Meet Hopps</a><a class="btn ghost" href="support.html">Contact us</a>
</div>
<section><div class="wrap">
  <h2>What we do</h2>
  <div class="grid">
    <div class="card"><h3>Computer vision on device</h3><p>Pose estimation runs directly on your phone. Video never leaves the device.</p></div>
    <div class="card"><h3>Measurement grounded in physics</h3><p>Our metrics come from established sports-science methods, such as flight-time jump height.</p></div>
    <div class="card"><h3>Built for athletes</h3><p>Fast capture, clear analytics and progress tracking, made for real training sessions.</p></div>
  </div>
</div></section>
<section><div class="wrap product">
  <img src="assets/hopps-icon.png" alt="Hopps app icon">
  <div class="txt">
    <div class="eyebrow">Our app</div>
    <h2>Hopps — vertical jump tracker</h2>
    <p class="muted">Hopps measures vertical jump height with your phone's camera and tracks your progress in an analytics dashboard. Coming soon to iPhone.</p>
    <a href="hopps/">Learn more &rarr;</a>
  </div>
</div></section>
<section><div class="wrap">
  <h2>Company</h2>
  <div class="facts">
    <b>Legal name</b><span>Campbell Labs LLC</span>
    <b>Type</b><span>Limited liability company, New York, USA</span>
    <b>Founded</b><span>2026</span>
    <b>Contact</b><span><a href="mailto:hello@{DOMAIN}">hello@{DOMAIN}</a></span>
  </div>
</div></section>''',on="home")

page("hopps/index.html","Hopps — Vertical jump tracker by Campbell Labs","Hopps measures your vertical jump with your phone camera and tracks your progress.",f'''
<div class="wrap hero product">
  <img src="../assets/hopps-icon.png" alt="Hopps app icon">
  <div class="txt">
    <div class="eyebrow">Hopps</div>
    <h1>Measure your vertical jump with your phone.</h1>
    <p class="lead">Set your phone on the floor, stand in frame and jump. Hopps tracks your body on the device and works out your jump height from flight time.</p>
    <a class="btn" href="../support.html">Get updates</a>
  </div>
</div>
<section><div class="wrap">
  <div class="grid">
    <div class="card"><h3>Camera-based measurement</h3><p>Live camera or slow-motion video. Uses no wearables, mats or sensors.</p></div>
    <div class="card"><h3>Analytics dashboard</h3><p>Personal bests, averages, consistency, goals and progress charts, with every session saved.</p></div>
    <div class="card"><h3>Private by design</h3><p>Video is processed on your phone and never uploaded. Your data stays on your device.</p></div>
    <div class="card"><h3>Every jump type</h3><p>Countermovement, squat, approach and single-leg jumps, in inches or centimeters.</p></div>
  </div>
</div></section>
<section><div class="wrap"><p class="muted">Read the <a href="../privacy.html">privacy policy</a> or <a href="../support.html">contact support</a>.</p></div></section>''',on="hopps",depth=1)

page("privacy.html","Privacy Policy — Campbell Labs LLC","Privacy policy for Campbell Labs LLC and the Hopps app.",f'''
<div class="wrap doc">
<h1>Privacy Policy</h1>
<p class="muted">Effective October 30, 2026</p>
<p>This policy explains how Campbell Labs LLC ("we", "us") handles information in the Hopps mobile app and on this website.</p>
<h2>Camera and video</h2>
<p>Hopps uses your device's camera, or videos you choose from your photo library, only to detect body position and measure jump height. All video is processed on your device. We do not record, upload, store or transmit your camera feed or videos.</p>
<h2>Data you create</h2>
<p>Jump results, goals and settings are stored locally on your device. We do not operate servers that collect this data, and we cannot access it. You can export or delete it at any time in the app's Settings. Deleting the app removes it.</p>
<h2>Information we collect</h2>
<p>Hopps does not require an account. It does not collect personal information, and it contains no advertising or third-party tracking. If you email us, we use your email address and message only to respond to you.</p>
<h2>Children</h2>
<p>Hopps is not directed to children under 13, and we do not knowingly collect personal information from children.</p>
<h2>Changes</h2>
<p>If this policy changes, we will post the updated version on this page with a new effective date.</p>
<h2>Contact</h2>
<p>Campbell Labs LLC, New York, USA &mdash; <a href="mailto:privacy@{DOMAIN}">privacy@{DOMAIN}</a></p>
</div>''')

page("terms.html","Terms of Use — Campbell Labs LLC","Terms of use for Campbell Labs LLC software.",f'''
<div class="wrap doc">
<h1>Terms of Use</h1>
<p class="muted">Effective October 30, 2026</p>
<p>By using software published by Campbell Labs LLC, including Hopps, you agree to these terms.</p>
<h2>Use of the app</h2>
<p>Hopps gives jump-height estimates for training and informational purposes. Measurements depend on camera placement, lighting and frame rate, and may not match laboratory equipment. Hopps is not a medical device.</p>
<h2>Safety</h2>
<p>Jumping and other exercise carry a risk of injury. Exercise within your abilities, use a safe space, and consult a professional if you have health concerns. You are responsible for your own safety while using the app.</p>
<h2>Disclaimer</h2>
<p>The app is provided "as is", without warranties of any kind. To the extent permitted by law, Campbell Labs LLC is not liable for indirect or consequential damages arising from use of the app.</p>
<h2>Apple App Store</h2>
<p>If you download Hopps from the App Store, Apple's Standard Licensed Application End User License Agreement also applies.</p>
<h2>Contact</h2>
<p><a href="mailto:hello@{DOMAIN}">hello@{DOMAIN}</a></p>
</div>''')

page("support.html","Contact & Support — Campbell Labs LLC","Contact Campbell Labs LLC and get support for Hopps.",f'''
<div class="wrap doc">
<h1>Contact &amp; Support</h1>
<p>We usually reply within two business days.</p>
<div class="grid" style="margin-top:28px">
  <div class="card"><h3>General inquiries</h3><p><a href="mailto:hello@{DOMAIN}">hello@{DOMAIN}</a></p></div>
  <div class="card"><h3>Hopps support</h3><p><a href="mailto:support@{DOMAIN}">support@{DOMAIN}</a></p></div>
</div>
<h2>Hopps tips</h2>
<ul>
  <li>Place the phone on the floor 2&ndash;3 m (7&ndash;10 ft) away, with your whole body in frame.</li>
  <li>Stand still for a moment until Hopps shows <em>Ready</em>, then jump.</li>
  <li>For the most accurate results, record slow-motion video (120 or 240 fps) and analyze it in the app.</li>
  <li>Your data is stored on your device. Use Settings &rarr; Backup before switching phones.</li>
</ul>
<p class="muted" style="margin-top:32px">Campbell Labs LLC &middot; New York, USA</p>
</div>''',on="support")
