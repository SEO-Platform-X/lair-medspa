"""Builds dispensaries/index.html from plastic-surgeons/index.html."""
import re, html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "plastic-surgeons" / "index.html").read_text()
L = src.split("\n")

def find(pred, start=0):
    for i in range(start, len(L)):
        if pred(L[i]):
            return i
    raise ValueError("not found")

FONT_B = "font-family: 'Bricolage Grotesque', sans-serif"

def face(initials, size=72, fs=23, dark=False, ring=False):
    if ring:
        bg, fg, border = "#FFFFFF", "#1F4FE0", "2px solid #1F4FE0"
    elif dark:
        bg, fg, border = "#0B1A2E", "#F4F1EA", "none"
    else:
        bg, fg, border = "#1F4FE0", "#FFFFFF", "none"
    return (f'<span class="face" style="position: relative; overflow: hidden; flex: 0 0 {size}px; width: {size}px; '
            f'height: {size}px; border-radius: 50%; background: {bg}; color: {fg}; border: {border}; box-sizing: border-box; '
            f'display: flex; align-items: center; justify-content: center; {FONT_B}; font-weight: 700; font-size: {fs}px">{initials}</span>')

def initials(name):
    words = [w for w in re.sub(r"[^A-Za-z0-9 ]", " ", name).split() if w.lower() not in ("the", "of", "on", "s")]
    if words[0].isdigit():
        return words[0]
    return (words[0][0] + (words[1][0] if len(words) > 1 else "")).upper()

# ---------------------------------------------------------------- data
WM = "https://images.weedmaps.com/"
# (name, place, logo url or None, plate background, logo fit: "wide" or "square")
CUSTOMERS = [
    ("42 Degrees", "Omaha and Lincoln, NE", "https://42degrees.com/wp-content/uploads/2020/08/42-degrees-logo-plain.svg", "#FFFFFF", "wide"),
    ("Atrium", "Los Angeles, CA", WM + "dispensaries/000/059/771/avatar/1676931388-screenshot_2023-02-20_at_20952_pm.png", "#000000", "square"),
    ("The Grove", "Las Vegas, NV", WM + "dispensaries/000/047/292/avatar/1716335074-grove_lib_-_png.png", "#0B0B0B", "square"),
    ("Farmhouse", "Petaluma, CA", WM + "dispensaries/000/404/585/avatar/1773258723-farmhouse_artisan_market_seal_green.png", "#FFFFFF", "square"),
    ("Green Mart", "Santa Ana, CA", "https://images.prismic.io/green-mart/Z06aQ5bqstJ97-TZ_ExtendedLogo.png?auto=format%2Ccompress&fit=max&w=384", "#FFFFFF", "wide"),
    ("Catalyst", "Southern California", "https://catalyst-cannabis.com/logos/Catalyst-Logo.webp", "#0B1A2E", "wide"),
    ("Herb", "Cannabis platform, Toronto", "https://herb.co/icons/icon-512x512.png", "#000000", "square"),
    ("Green Qween", "Los Angeles, CA", None, None, None),
    ("Essential Torrance", "Torrance, CA", WM + "dispensaries/000/027/468/avatar/1787687088-weedmaps_banner__800_x_800_px___5_.png", "#1A1030", "square"),
    ("Reefer Madness", "Denver, CO", WM + "dispensaries/000/049/502/avatar/1704831771-v2_weedmaps_avatar_logo.png", "#FFFFFF", "square"),
    ("Buds Garage", "Everett, WA", "https://budsgarage.com/wp-content/uploads/Logo-01.png", "#FFFFFF", "wide"),
    ("Greenstop Wellness", "Houston, TX", "https://leafly-public.imgix.net/dispensary/photos/gallery384904/iG3vvlZESJS6vd6ZCMBD_c0386457-446c-4145-96fb-30f5ff349edf?w=240", "#000000", "square"),
    ("Westside420 Recreational", "Longview, WA", "https://westside420.com/wp-content/uploads/westside420-logo-1-1.png", "#FFFFFF", "wide"),
    ("Remedy", "Tulalip, WA", WM + "dispensaries/000/061/331/avatar/1791494629-circle_flame__512_x_512_px_.jpg", "#000000", "square"),
    ("CannaCon", "Cannabis business expo", "https://cannacon.org/assets/brand/cannacon-wordmark.png", "#FFFFFF", "wide"),
    ("Lucky Leaf Co.", "Spokane, WA", WM + "dispensaries/000/046/922/avatar/1691609850-luckyleaf-800x800.png", "#1F4FE0", "square"),
    ("The Dispensary on Main", "Galesburg, IL", "https://thedispensaryonmain.com/wp-content/uploads/Logo.svg", "#0B1A2E", "wide"),
    ("Alamo Botanicals", "San Antonio, TX", "https://alamobotanicals.com/wp-content/uploads/alamobotanicalsWhiteGreen.svg", "#0B1A2E", "wide"),
    ("Green Mountain Cannabis Works", "Manchester, VT", "https://greenmountaincannabisworks.com/wp-content/uploads/GMCW-green-web.png", "#FFFFFF", "wide"),
    ("Highnorth", "Cottage Grove, MN", "https://highnorthmn.com/cdn/shop/files/Highnorth_Logo_Black_No_Background_2_637x150.png?v=1640737268", "#FFFFFF", "wide"),
    ("Hot Springs Hemp Company", "Hot Springs, AR", "https://hotspringshemp.com/wp-content/uploads/yootheme/cache/f0/hot-springs-hemp-logo-f0ae48e8.webp", "#FFFFFF", "square"),
    ("Lake Daze", "Hopkins, MN", "https://lakedaze.com/wp-content/uploads/lake_daze_dispensary_3.png", "#FFFFFF", "wide"),
    ("Pot Mama's", "Edina, MN", "https://static.wixstatic.com/media/00146e_02d41810ffa944aa8e916f977fb917a8%7Emv2.png/v1/fill/w_180%2Ch_180%2Clg_1%2Cusm_0.66_1.00_0.01/00146e_02d41810ffa944aa8e916f977fb917a8%7Emv2.png", "#FFFFFF", "square"),
]

FAV = "https://www.google.com/s2/favicons?sz=64&domain="
# (name, bio, [(company, domain or None)])
PEOPLE = [
    ("Luna Stower", "Chief Impact Officer, Ispire. Longtime cannabis activist.", [("Ispire", "ispiretechnology.com")]),
    ("Parisa Mansouri-Rad", "Co-founder, Blunt Brunch. Executive Cannabis Consultant, IMA.", [("Blunt Brunch", "bluntbrunch.com"), ("IMA", "imacorp.com")]),
    ("Adelia Fakhri", "Cannabis events and community builder. EventHi.", [("EventHi", "eventhi.io")]),
    ("Jessica Ferranti", "Founder, The Mycelia Group. NJ Cannabis Chamber of Commerce.", [("The Mycelia Group", "myceliagroup.com"), ("NJ Cannabis Chamber", "njcannabischamber.com")]),
    ("Stella Morrison", "Founder, CannaContent. Cannabis content and SEO.", [("CannaContent", "cannacontent.co")]),
    ("Jocelyn Sheltraw", "Budist, the cannabis review app.", [("Budist", None)]),
    ("Angela Pih", "CMO, Statehouse Holdings. Ex-CannaCraft. Founder, BrandTrust.", [("Statehouse", None), ("CannaCraft", "cannacraft.com"), ("BrandTrust", None)]),
    ("Rachelle Gordon", "Cannabis journalist for GreenState and DoubleBlind.", [("GreenState", "greenstate.com"), ("DoubleBlind", "doubleblindmag.com")]),
    ("Rachel Wright, CPA", "Cannabis CPA. Beard Bros Media correspondent.", [("Beard Bros Media", "beardbrospharms.com")]),
    ("JM Balbuena", "Author, The Successful Canna-preneur. Synergy Studio.", [("Synergy Studio", None)]),
    ("David Tran", "Cannabis industry.", []),
    ("Justin Johnson", "Cannabis industry.", []),
    ("Doreen Sullivan", "Founder, My Bud Vase. Cannabis products.", [("My Bud Vase", "mybudvase.com")]),
    ("Aubrey Amatelli", "CEO and founder, Payrio. Cannabis payments.", [("Payrio", "payrio.com")]),
    ("Dan Serard", "VP Business Development, Cannabis Creative Group.", [("Cannabis Creative", "cannabiscreative.com")]),
    ("Kristin McFarland", "Host, Market Like a Badass podcast.", [("Market Like a Badass", None)]),
    ("Caron Cooper", "SVP Web Development, Local AI Registry. Builds dispensary sites.", [("Local AI Registry", "localairegistry.com")]),
    ("Tony Van Pelt", "Founder, Chronic Candy.", [("Chronic Candy", None)]),
    ("Krysta Jones", "Founder, THC Girls (The High Country Girls).", [("THC Girls", "thehighcountrygirls.com")]),
    ("Champelli", "Josef, Bay Area grower and artist. Champelli.", [("Champelli", None)]),
]

def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower().split(",")[0]).strip("-")

def chip(name, domain):
    icon = (f'<img src="{FAV}{domain}" alt="" style="width:16px;height:16px;border-radius:3px;flex:0 0 16px">' if domain else "")
    return (f'<span style="display:inline-flex;align-items:center;gap:6px;{FONT_B};font-weight:700;font-size:12px;letter-spacing:.01em;'
            f'color:#0B1A2E;background:#F2EFE9;border-radius:6px;padding:4px 8px;white-space:nowrap">{icon}{html.escape(name)}</span>')

def customer_card(i, name, place, logo, bg, fit):
    if logo:
        pad = "8px" if fit == "square" else "10px 14px"
        plate = (f'<div style="height: 76px; border-radius: 12px; background: {bg}; display: flex; align-items: center; justify-content: center; '
                 f'padding: {pad}; box-sizing: border-box; border: 1px solid rgba(11,26,46,.08)">'
                 f'<img src="{logo}" alt="{html.escape(name)} logo" loading="lazy" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block"></div>')
    else:
        plate = (f'<div style="height: 76px; border-radius: 12px; background: #0B1A2E; display: flex; align-items: center; justify-content: center">'
                 f'<span style="{FONT_B}; font-weight: 800; font-size: 20px; color: #F4F1EA">{html.escape(name)}</span></div>')
    return ('<div style="background: #FFFFFF; border-radius: 16px; padding: 12px; display: flex; flex-direction: column; gap: 12px">\n'
            + plate + "\n"
            + f'<div style="padding: 0 4px 4px"><div style="{FONT_B}; font-weight: 700; font-size: 16px; line-height: 1.2">{html.escape(name)}</div>'
              f'<div style="font-size: 14px; color: #3D4A5C; line-height: 1.3; margin-top: 2px">{html.escape(place)}</div></div>\n</div>')

def person_face(name):
    ini = initials(name)
    return ('<span class="face" style="position: relative; overflow: hidden; flex: 0 0 72px; width: 72px; height: 72px; border-radius: 50%; '
            f'background: #FFFFFF; color: #1F4FE0; border: 2px solid #1F4FE0; box-sizing: border-box; display: flex; align-items: center; '
            f'justify-content: center; {FONT_B}; font-weight: 700; font-size: 23px">{ini}<img data-slug="{slug(name)}" alt="" '
            'style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center center; opacity: 0; transition: opacity .3s"></span>')

def person_card(name, bio, cos):
    t = "".join(chip(n, d) for n, d in cos)
    return ('<div style="background: #FFFFFF; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 12px">\n'
            + person_face(name) + "\n"
            + f'<div><div style="{FONT_B}; font-weight: 700; font-size: 16px; line-height: 1.2">{html.escape(name)}</div>'
              f'<div style="font-size: 14px; color: #3D4A5C; line-height: 1.3; margin-top: 2px">{html.escape(bio)}</div></div>\n'
            + (f'<div style="margin-top:auto;display:flex;flex-wrap:wrap;gap:6px">{t}</div>\n' if t else "")
            + '</div>')

GRID = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 12px">'
PLUS = ('<div style="background: #1F4FE0; color: #FFFFFF; border-radius: 16px; padding: 22px 20px; display: flex; flex-direction: column; '
        f'justify-content: center; gap: 6px; min-height: 120px"><div style="{FONT_B}; font-weight: 800; font-size: 52px; line-height: 1">+100</div>'
        f'<div style="{FONT_B}; font-weight: 700; font-size: 16px; line-height: 1.25">more local businesses trust our team</div></div>')

JOIN = ('<a href="https://localairegistry.com/signup" style="background: #0B1A2E; color: #F4F1EA; border-radius: 16px; padding: 22px 20px; display: flex; flex-direction: column; '
        f'justify-content: center; gap: 8px; min-height: 120px; text-decoration: none"><div style="{FONT_B}; font-weight: 800; font-size: 19px; line-height: 1.15">Work in cannabis?</div>'
        f'<div style="{FONT_B}; font-weight: 600; font-size: 15px; line-height: 1.3; color: #A9B3C4">Join our partner network</div></a>')
DGRID_CSS = ('<style>.dgrid{display:grid;gap:12px;grid-template-columns:repeat(2,minmax(0,1fr))}'
             '@media(min-width:600px){.dgrid{grid-template-columns:repeat(4,minmax(0,1fr))}}'
             '@media(min-width:900px){.dgrid6{grid-template-columns:repeat(6,minmax(0,1fr))}}'
             '.pgrid{display:flex;flex-wrap:wrap;justify-content:center;gap:12px}.pgrid>*{box-sizing:border-box;flex:0 0 calc((100% - 12px)/2)}'
             '@media(min-width:600px){.pgrid>*{flex-basis:calc((100% - 36px)/4)}}@media(min-width:900px){.pgrid>*{flex-basis:calc((100% - 48px)/5)}}</style>')
trust = DGRID_CSS + f"""<section style="background: #F4F1EA; padding: 56px 20px">
<div style="max-width: 1040px; margin: 0 auto">
<h2 style="font-family: 'Cormorant', Georgia, serif; font-weight: 600; font-size: 36px; line-height: 1.05; margin: 0 0 8px">Dispensaries that trust our team</h2>
<p style="margin: 0 0 28px; color: #3D4A5C">Dispensaries, cannabis platforms and industry events across the US and Canada have worked with the people behind Local AI Registry.</p>
<div class="dgrid dgrid6">
{chr(10).join(customer_card(i, *c) for i, c in enumerate(CUSTOMERS))}
{PLUS}
</div>
<h3 style="{FONT_B}; font-weight: 700; font-size: 18px; margin: 36px 0 14px">Backed by people who built the cannabis industry</h3>
<div class="pgrid">
{chr(10).join(person_card(*p) for p in PEOPLE)}
{JOIN}
</div>
</div>
</section>
"""

def tile(inner, bg="#FFFFFF"):
    return (f'<span style="display: flex; align-items: center; justify-content: center; min-height: 72px; padding: 0 14px; '
            f'border-radius: 18px; background: {bg}; border: 1px solid rgba(11,26,46,.07)">{inner}</span>')

def word(text, sub=None, color="#0B1A2E", size=24, weight=800, spacing=".01em"):
    s = f'<span style="{FONT_B};font-weight:{weight};font-size:{size}px;letter-spacing:{spacing};color:{color} !important;line-height:1">{text}</span>'
    if sub:
        s = (f'<span style="display:flex;flex-direction:column;align-items:center;gap:3px">{s}'
             f'<span style="font-family:\'Hanken Grotesk\',sans-serif;font-weight:600;font-size:10px;letter-spacing:.2em;color:{color} !important">{sub}</span></span>')
    return s

EYEBROW = "margin: 40px 0 16px; font-family: 'Hanken Grotesk', sans-serif; font-weight: 600; font-size: 12px; letter-spacing: 0.22em; text-transform: uppercase; color: #5B6577"
TWO = '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px">'
built = f"""<section style="background: #F4F1EA; padding: 36px 20px 40px">
<div style="max-width: 1040px; margin: 0 auto">
<h2 style="font-family: 'Cormorant', Georgia, serif; font-weight: 600; font-size: 34px; line-height: 1.05; margin: 0 0 22px">Built by former leaders from</h2>
<p style="{EYEBROW}">Search and AI</p>
{TWO}
{tile('<img src="../logos/google.svg" alt="Google" style="height: 30px; width: auto; max-width: 100%">')}
{tile('<img src="../logos/microsoft.svg" alt="Microsoft" style="height: 24px; width: auto; max-width: 100%">')}
</div>
<p style="{EYEBROW}">Cannabis</p>
{TWO}
{tile('<img src="https://mita.us/wp-content/uploads/2021/10/cropped-mita-outlined--768x256.png" alt="Marijuana Industry Trade Association" style="height: 50px; width: auto; max-width: 100%">')}
{tile('<img src="../logos/cannabis/herb.svg" alt="Herb" style="height: 30px; width: auto; max-width: 100%">', bg="#D9F99D")}
{tile('<img src="https://canopygrowth.com/wp-content/uploads/2026/06/Canopy_Logo-768x288.png" alt="Canopy Growth" style="height: 40px; width: auto; max-width: 100%">')}
{tile('<img src="https://womenemployedincannabis.com/wp-content/uploads/yootheme/cache/df/weic-new2-dfb1672d.webp" alt="Women Employed in Cannabis" style="height: 44px; width: auto; max-width: 100%">', bg="#0B1A2E")}
</div>
<p style="{EYEBROW}">Dispensary websites</p>
{TWO}
<span style="grid-column: 1 / -1; display: flex">{tile('<img src="https://cannasite.com/wp-content/uploads/CannaSiteCo.svg" alt="CannaSite" style="height: 30px; width: auto; max-width: 100%">').replace('display: flex;', 'display: flex; flex: 1;', 1)}</span>
</div>
<p style="margin: 48px 0 0; font-family: 'Hanken Grotesk', sans-serif; font-size: 17px; line-height: 1.55; color: #4A5567">We know how AI decides which dispensaries to recommend, and how a store turns first visits into regulars.</p>
</div>
</section>
"""


# ---------------------------------------------------------------- founder card (replaces the Venn card)
def ctile(logo, role):
    return (f'<div style="background:#F2EFE9;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:8px;align-items:flex-start">'
            f'<span style="background:#FFFFFF;border:1px solid rgba(11,26,46,.1);border-radius:8px;padding:6px 10px;display:inline-flex;align-items:center;gap:6px;height:34px;box-sizing:border-box">{logo}</span>'
            f'<span style="font-size:13px;line-height:1.35;color:#3D4A5C">{role}</span></div>')
def limg(src, h=20, alt=""):
    return f'<img src="{src}" alt="{alt}" style="height:{h}px;width:auto;display:block">'
def ficon(domain, name, color="#0B1A2E"):
    return (f'<img src="https://www.google.com/s2/favicons?sz=64&domain={domain}" alt="" style="width:18px;height:18px">'
            f'<b style="{FONT_B};font-size:14px;color:{color} !important">{name}</b>')
career = [
    (limg("../logos/google.svg", 20, "Google"), "Executive in Search"),
    (limg("../logos/microsoft.svg", 18, "Microsoft"), "Executive, Microsoft HoloLens"),
    (limg("../logos/evolus.svg", 16, "Evolus"), "Head of Digital through the 2018 Nasdaq&nbsp;IPO"),
    (limg("../logos/revance.png", 14, "Revance"), "VP, grew a global team to&nbsp;100"),
    (ficon("spotify.com", "Spotify"), "Head of Digital"),
    (ficon("chase.com", "Chase"), "VP, Digital"),
    (f'<b style="{FONT_B};font-size:18px;color:#7B2FF7 !important;letter-spacing:-.01em">razorfish</b>', "Amazon and Google Glass&nbsp;work"),
    (f'<b style="{FONT_B};font-size:13px;color:#0B1A2E !important">UX Laboratory</b>', "Founded it.&nbsp;Acquired."),
]
def stat(n, label):
    return (f'<div style="background:#F2EFE9;border-radius:14px;padding:12px 14px"><div style="{FONT_B};font-weight:800;font-size:26px;line-height:1;color:#1F4FE0 !important">{n}</div>'
            f'<div style="font-size:13px;line-height:1.35;color:#3D4A5C;margin-top:4px">{label}</div></div>')
FOUNDER = f"""<div class="fcard" style="grid-column: 1 / -1; background: #FFFFFF; border: 1px solid #D9DEE7; border-radius: 20px; padding: 22px; display: grid; gap: 22px">
<style>.fcard{{grid-template-columns:1fr}}@media(min-width:860px){{.fcard{{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr)}}}}.fcard .cg{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;align-content:start}}.fcard .sg{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:18px}}</style>
<div>
<div style="display:flex;gap:16px;align-items:center;margin-bottom:14px">
<span class="face" style="position: relative; overflow: hidden; flex: 0 0 88px; width: 88px; height: 88px; border-radius: 50%; background: #1F4FE0; color: #FFFFFF; border: 3px solid #E8ECF4; box-sizing: border-box; display: flex; align-items: center; justify-content: center; {FONT_B}; font-weight: 700; font-size: 26px">SL<img data-slug="steve-lee" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center center; opacity: 0; transition: opacity .3s; filter: grayscale(1)"></span>
<div><div style="font-family:'Hanken Grotesk',sans-serif;font-weight:700;font-size:12px;letter-spacing:.18em;color:#1F4FE0">FOUNDER AND CEO</div>
<div style="{FONT_B};font-weight:800;font-size:28px;line-height:1.1;color:#0B1A2E">Steve Lee</div></div>
</div>
<div style="font-family:'Cormorant',Georgia,serif;font-style:italic;font-weight:500;font-size:24px;line-height:1.2;color:#0B1A2E;margin-bottom:12px">Built by someone who has worked inside both search and brick-and-mortar small business.</div>
<div style="font-size:16px;line-height:1.6;color:#3D4A5C">20+ years in digital, starting in search at Google and Microsoft, then leading digital for consumer brands and companies that sell to local businesses. He also owns a brick-and-mortar business, so he has run the storefront side of this work too.</div>
<div class="sg">{stat("14", "age he sold his first company, for $3M")}{stat("20+", "years in digital")}<div style="grid-column:1/-1">{stat("1", "Nasdaq IPO, at Evolus")}</div></div>
</div>
<div class="cg">{"".join(ctile(l, r) for l, r in career)}</div>
</div>"""

# ---------------------------------------------------------------- splice sections
i_vid = find(lambda s: s.startswith("<!-- VIDEO -->"))
i_built = find(lambda s: s.startswith("<!-- BUILT BY -->"))
i_stats = find(lambda s: s.startswith("<!-- STATS -->"))
i_trust = find(lambda s: s.startswith("<!-- TRUST -->"))
i_story = find(lambda s: s.startswith("<!-- STORY -->"))
L = L[:i_vid] + ["<!-- BUILT BY -->", built] + L[i_stats:i_trust + 1] + [trust] + L[i_story:]

# swap the Venn card for the founder card
i_venn = find(lambda x: x.startswith('<div style="grid-column: 1 / -1; background: #0B1A2E; color: #F4F1EA; border-radius: 16px; padding: 18px;'))
j = i_venn
while L[j].strip() != "</div>":
    j += 1
L = L[:i_venn] + [FOUNDER] + L[j + 1:]

# drop video script
out = "\n".join(L)
out = re.sub(r"<script>\n\(function\(\)\{\nvar wrap=document.getElementById\('vwrap'\).*?</script>\n", "", out, flags=re.S)

# hero avatar row: dispensary initials, no photos
HERO = [c for c in CUSTOMERS if c[4] == "square"][:5]
hero_faces = "".join(
    f'<span style="margin-left: {0 if k == 0 else -12}px; border: 2px solid #F2EFE9; border-radius: 50%; display: flex; '
    f'width: 34px; height: 34px; overflow: hidden; background: {c[3]}"><img src="{c[2]}" alt="{html.escape(c[0])}" '
    'style="width: 100%; height: 100%; object-fit: cover"></span>'
    for k, c in enumerate(HERO))
out = re.sub(r'<div style="display: flex"><span style="margin-left: 0px.*?</div>(?=\s*<p[^>]*>Trusted)',
             f'<div style="display: flex">{hero_faces}</div>', out, count=1, flags=re.S)

# ---------------------------------------------------------------- race chart -> near-me searches
race = ('<svg id="race" viewBox="0 0 340 260" role="img" aria-label="Bar chart: US monthly searches. weed dispensary near me 41,000, '
        'dispensaries near me 226,000, dispensary near me 1.59 million" style="width:100%;height:auto;overflow:visible">'
        '<path d="M20 210 H320" stroke="currentColor" stroke-opacity=".25" stroke-width="1.5"/>'
        '<rect class="ib" data-h="8" x="40" y="202" width="68" height="8" rx="4" fill="currentColor" fill-opacity=".28"/>'
        '<rect class="ib" data-h="24" x="136" y="186" width="68" height="24" rx="8" fill="currentColor" fill-opacity=".5"/>'
        '<rect class="ib" data-h="158" x="232" y="52" width="68" height="158" rx="8" fill="#4F7BFF"/>'
        '<g font-family="Bricolage Grotesque, sans-serif" font-weight="700" text-anchor="middle">'
        '<text class="il" x="74" y="190" font-size="22" fill="currentColor" style="transition:opacity .6s">41K</text>'
        '<text class="il" x="170" y="174" font-size="22" fill="currentColor" style="transition:opacity .6s">226K</text>'
        '<text class="il" x="266" y="38" font-size="28" fill="#6E92FF" style="transition:opacity .6s">1.59M</text>'
        '<g font-size="12" fill="currentColor" fill-opacity=".75"><text x="74" y="230">weed dispensary</text><text x="74" y="246">near me</text>'
        '<text x="170" y="230">dispensaries</text><text x="170" y="246">near me</text></g>'
        '<g font-size="12" fill="#6E92FF"><text x="266" y="230">dispensary</text><text x="266" y="246">near me</text></g></g></svg>')
out = re.sub(r'<svg id="race".*?</svg>', race, out, count=1, flags=re.S)

# ---------------------------------------------------------------- text swaps
R = [
    # head
    ("How plastic surgeons get recommended by ChatGPT", "How dispensaries get recommended by ChatGPT"),
    ("Patients ask ChatGPT and Gemini which plastic surgeon to see. We confirm your credentials, procedures and reviews everywhere AI looks, so it names you.",
     "Shoppers ask ChatGPT and Gemini for a dispensary near me. We confirm your store, hours, menu and reviews everywhere AI looks, so it names you."),
    ("lair-medspa/plastic-surgeons/og.png", "lair-medspa/dispensaries/og.png"),
    # hero
    (">For plastic surgeons<", ">For dispensaries<"),
    ("Ask ChatGPT who does the best facelift in your city. Does it name you?",
     "Ask ChatGPT for a dispensary near&nbsp;you. Does it name&nbsp;yours?"),
    ("Patients now vet surgeons with AI before they book a consult. We make sure AI can confirm your credentials, your procedures and your results.",
     "Shoppers now ask AI where to buy. With cannabis ads restricted on Google and Meta, being recommended is how new customers find you. We make sure AI can confirm your store, your hours and your&nbsp;menu."),
    ("See what AI says about your practice", "See what AI says about your&nbsp;store"),
    ("Trusted by top surgeons", "Trusted by dispensaries across the US"),
    ("Who is the best facelift surgeon near me?", "What&rsquo;s the best dispensary near me?"),
    ("Three surgeons I can vouch for:", "Three I would check out:"),
    ("The one with more reviews", "The one with more Google reviews"),
    ("The one with a RealSelf profile", "The one with its menu on Leafly"),
    ('<span style="font-weight: 700; color: #FFFFFF; font-size: 16px">Your practice</span>',
     '<span style="font-weight: 700; color: #FFFFFF; font-size: 16px">Your dispensary</span>'),
    # stats
    ("Patients changed how they pick a surgeon. In one year.", "Shoppers changed how they find a dispensary. In one year."),
    ("Before the consult, there is now an AI conversation. Most surgeons never see it.",
     "Before the first visit, there is now an AI conversation. Most dispensaries never see&nbsp;it."),
    ("A five-figure procedure gets more research, not less.", "And &ldquo;dispensary near me&rdquo; is one of the biggest local searches there is."),
    ("Ask for a rhinoplasty surgeon and AI names two or three. That is the whole list.",
     "Ask AI for the best dispensary nearby and it names two or three. That is the whole list."),
    ('color: #1F4FE0">66%</span>', 'color: #1F4FE0">1.59M</span>'),
    ('color: #3D4A5C">vs 41%</span>', 'color: #3D4A5C">searches a month</span>'),
    ("of upper-income adults use AI chatbots, compared with 41% of lower-income adults. In households earning $150K or more, AI has already passed Google as the first place people look for a local business. Those are your elective surgery patients.",
     "US searches every month for &ldquo;dispensary near me,&rdquo; plus 226,000 for &ldquo;dispensaries near me.&rdquo; Each one is a chance for AI to name your store, or the one down the street."),
    ("Pew Research Center, Americans and AI 2026. Yext, Consumer Search Behaviors Report 2026", "Ahrefs Keywords Explorer, US monthly search volume, November 2026"),
    # story
    ("Patients meet your practice before your website", "Shoppers meet your store before your website"),
    ("Before: patients found you, then read about you", "Before: shoppers found you, then browsed your menu"),
    ('A patient searched "rhinoplasty near me," clicked your site and scrolled your gallery. Your website did the convincing.',
     'A shopper searched "dispensary near me," clicked your site and scrolled your menu. Your website did the convincing.'),
    ("Now: AI vets you before the patient does", "Now: AI picks the store before the shopper does"),
    ("AI checks your board certification, reviews, RealSelf answers and every directory listing, then decides if you are safe to recommend. If those sources disagree or go quiet, it names another surgeon.",
     "AI checks your Google profile, Leafly and Weedmaps listings, reviews and every directory, then decides which store to recommend. If those sources disagree or go quiet, it names another dispensary."),
    ("reads Google, Yelp, RealSelf, reviews, Instagram, Healthgrades, directories", "reads Google, Weedmaps, Leafly, reviews, Instagram, Apple Maps, directories"),
    (">Yelp<", ">Weedmaps<"), (">RealSelf<", ">Leafly<"), (">Healthgrades<", ">Apple Maps<"),
    ("\"I couldn't confirm their board certification. I'd look at another surgeon nearby.\"",
     "\"I couldn't confirm they're open today. I'd try another dispensary nearby.\""),
    ("With us: your credentials, confirmed everywhere", "With us: your store, confirmed everywhere"),
    ("You confirm your credentials, procedures, locations and hours once.", "You confirm your locations, hours, menu and license once."),
    ("\"For a facelift, I'd start with <strong style=\"color: #D63A1C\">your practice</strong>. Board-certified, 4.9 stars, consults open this week.\"",
     "\"For a dispensary near you, I'd start with <strong style=\"color: #D63A1C\">your store</strong>. 4.8 stars, open until 10 tonight, pickup ready in 15 minutes.\""),
    # questions
    ("What patients ask AI before they book a consult", "What shoppers ask AI before they visit"),
    ("Surgery is a big decision, so patients ask AI question after question. Every answer is built from what AI can verify about you.",
     "Shoppers ask AI where to go, what is in stock and who has the best deals. Every answer is built from what AI can verify about you."),
    ("&ldquo;Who is the best rhinoplasty surgeon near me?&rdquo;", "&ldquo;What&rsquo;s the best dispensary near me?&rdquo;"),
    ("Your procedures named clearly on your site and profiles, with reviews that mention them.",
     "The same name, address and hours on every source, with recent reviews that mention you."),
    ("&ldquo;Is this surgeon board certified?&rdquo;", "&ldquo;Which dispensary is open right now?&rdquo;"),
    ("Your board certification stated the same way on every source AI checks.",
     "Correct hours on Google, Leafly, Weedmaps and Apple Maps, holidays included."),
    ("&ldquo;How much does a tummy tuck cost here?&rdquo;", "&ldquo;Who has the best deals on flower today?&rdquo;"),
    ("Price ranges or financing details AI can quote instead of guessing.", "Current deals and specials posted where AI can read them."),
    ("&ldquo;Which surgeon has the best facelift results?&rdquo;", "&ldquo;Which dispensary carries live rosin?&rdquo;"),
    ("Before-and-after photos labeled so AI knows which procedure each one shows.", "A live menu AI can read, kept in sync with your POS."),
    ("&ldquo;Who specializes in revision rhinoplasty?&rdquo;", "&ldquo;Is there a dispensary with curbside pickup?&rdquo;"),
    ("Pages and articles that show depth in a procedure, not just a list of services.", "Pickup, delivery and parking details stated the same way everywhere."),
    ("&ldquo;What is recovery like after breast augmentation?&rdquo;", "&ldquo;Is this dispensary licensed?&rdquo;"),
    ("Plain-English answers on your own site, with your name on them.", "Your license number and an address that match state records."),
    # checklist
    ("What AI checks before it names a surgeon. Every month.", "What AI checks before it names a dispensary. Every month."),
    ("Leave gaps and AI sends the consult somewhere else.", "Leave gaps and AI sends the shopper somewhere else."),
    ("Google profile posts for each procedure you offer", "Google profile posts for deals and new drops"),
    ("RealSelf, Healthgrades, Vitals, Yelp, Apple Maps, Bing", "Leafly, Weedmaps, Yelp, Apple Maps, Bing"),
    ("HIPAA-safe replies to every review", "Compliant replies to every review"),
    ("A steady flow of new patient reviews", "A steady flow of new customer reviews"),
    ("Before-and-after galleries AI can actually read", "A menu AI can actually read"),
    ("Board certification marked up in your site code", "License and hours marked up in your site&nbsp;code"),
    ("Procedure pages that load fast on a phone", "Store pages that load fast on a phone"),
    ("Articles on recovery, cost and safety", "Guides on products, deals and local rules"),
    ("Checking what ChatGPT tells patients about you", "Checking what ChatGPT tells shoppers about&nbsp;you"),
    ("Thank you for trusting our team. We are so glad you...", "Thanks for stopping in! We are so glad you..."),
    # steps
    ("Claim your free practice page", "Claim your free dispensary page"),
    ("Add your credentials, procedures, surgeons and locations in five short steps.", "Add your locations, hours, menu and license in five short steps."),
    ("Directories, Google, RealSelf, reviews, press and site code", "Directories, Google, Leafly, Weedmaps, reviews, press and site code"),
    ("AI recommends your practice by name", "AI recommends your store by name"),
    # calculator
    ("What is one surgical patient from AI worth?", "What are new regulars from AI worth?"),
    ("Plug in your own case value and volume.", "Plug in your own numbers."),
    ("New surgical patients from AI, per month", "New customers from AI, per month"),
    ('id="ptsOut" style="color: #1F4FE0">2<', 'id="ptsOut" style="color: #1F4FE0">30<'),
    ('<input id="pts" type="range" min="1" max="20" step="1" value="2"', '<input id="pts" type="range" min="5" max="300" step="5" value="30"'),
    ("<span>Average case value</span>", "<span>Average yearly spend per customer</span>"),
    ('id="valOut" style="color: #1F4FE0">$8,000<', 'id="valOut" style="color: #1F4FE0">$600<'),
    ('<input id="val" type="range" min="2000" max="30000" step="500" value="8000"', '<input id="val" type="range" min="100" max="3000" step="50" value="600"'),
    ("A year of AI-referred cases is worth", "A year of AI-referred customers is worth"),
    ('<span id="totOut">$192,000</span>', '<span id="totOut">$216,000</span>'),
    # guarantee
    ("and medical aesthetics (Revance, Evolus) overlap", "and the cannabis industry (MITA, Herb) overlap"),
    ('letter-spacing=".14em">AESTHETICS</text><text x="240" y="82" font-size="14.5" font-weight="700">Revance</text><text x="240" y="103" font-size="14.5" font-weight="700">Evolus</text>',
     'letter-spacing=".14em">CANNABIS</text><text x="240" y="82" font-size="14.5" font-weight="700">MITA</text><text x="240" y="103" font-size="14.5" font-weight="700">Herb</text>'),
    ("Former executive at Google, Microsoft, Revance and Evolus. He has spent his career in search and in aesthetics, and owns a local med spa.",
     "Former executive at Google and Microsoft. He has spent his career in search and now helps local brick-and-mortar businesses, dispensaries included, get found."),
    ("If AI is not naming your practice in 90 days", "If AI is not naming your store in 90 days"),
    ("A 90 day calendar, then AI names your practice", "A 90 day calendar, then AI names your store"),
    (">your practice</text>", ">your store</text>"),
    ("var txt=h.textContent.replace(/\\s+/g,' ').trim();", "var txt=h.textContent.replace(/[ \\t\\r\\n]+/g,' ').trim();"),
    ("var LIGHT={'0':'#F2EFE9','1':'#F2EFE9','2':'#F4F1EA','3':'#FFFFFF','4':'#F4F1EA','5':'#FFFFFF','6':'#F4F1EA','7':'#FFFFFF','8':'#F4F1EA','9':'#F4F1EA','10':'#FFFFFF','11':'#F4F1EA'};",
     "var LIGHT={'0':'#F2EFE9','1':'#F4F1EA','2':'#FFFFFF','3':'#F4F1EA','4':'#FFFFFF','5':'#F4F1EA','6':'#FFFFFF','7':'#F4F1EA','8':'#F4F1EA','9':'#FFFFFF','10':'#F4F1EA'};"),
    ("var THEME=[0,0,0,1,0,1,0,0,1,0,0,0,1];", "var THEME=[0,0,1,0,1,0,0,1,0,0,0,1];"),
    ("['Patients changed how',", "['Shoppers changed how',"),
    # FAQ
    ("Questions surgeons ask us", "Questions dispensaries ask us"),
    ("How does ChatGPT decide which plastic surgeons to recommend?", "How does ChatGPT decide which dispensaries to recommend?"),
    ("It recommends surgeons it can verify. That means the same facts on Google, directories and review sites, a board certification it can confirm, procedures it can match to the question, and recent reviews.",
     "It recommends stores it can verify. That means the same name, address, hours and phone on Google, Leafly, Weedmaps and directories, a menu it can read, and recent reviews."),
    ("names only a few surgeons", "names only a few dispensaries"),
    ("How do you keep review replies HIPAA-safe?", "Can this help when cannabis ads are restricted?"),
    ("Our replies never confirm that someone is a patient and never mention a procedure or any health details. Every reply waits for your approval before it posts.",
     "Yes. We do not run ads. We work on the organic side: your Google profile, listings, reviews and every source AI reads. None of it depends on ad approval, so it keeps working when Google and Meta say no."),
    ("what each one says about your practice", "what each one says about your store"),
    ("How long until AI starts naming my practice?", "How long until AI starts naming my store?"),
    ("some practices see changes sooner", "some stores see changes sooner"),
    # CTA
    ("Be the surgeon AI recommends.", "Be the dispensary AI recommends."),
    ("Find out what ChatGPT tells patients about your practice right now. Free.", "Find out what ChatGPT tells shoppers about your store right now. Free."),
    ("Yext, Consumer Search Behaviors Report 2026. Pew Research Center, Americans and AI 2026.", "Ahrefs Keywords Explorer, November 2026."),
]
missing = []
for a, b in R:
    if a not in out:
        missing.append(a[:70])
    out = out.replace(a, b)

out = out.replace("—", ", ")

# glue the last two words of every text run so no word is stranded alone on a line
def glue(m):
    t = m.group(1)
    core = t.rstrip()
    words = core.replace("&nbsp;", " ").split()
    if len(words) < 2 or (len(words) == 2 and len(core) > 12):
        return m.group(0)
    head, tail = core.rsplit(" ", 1)
    prev = head.rsplit(" ", 1)[-1]
    if len(prev) + len(tail) > 20:
        return m.group(0)
    # also keep each sentence's last word with the word before it, but only short pairs
    head = re.sub(r"(?<= )(\S{1,7}) (\S{1,8}[.?!])(?= )", "\\1&nbsp;\\2", head) if len(words) >= 6 else head
    return ">" + head + "&nbsp;" + tail + t[len(core):] + "<"

out = out.replace("<style>\nbody{margin:0}", "<style>\nbody{margin:0;text-wrap:pretty}h1,h2,h3,summary{text-wrap:balance}", 1)
body_start = out.index("<body")
parts = re.split(r"(<script.*?</script>|<style.*?</style>|<svg.*?</svg>)", out[body_start:], flags=re.S)
for k in range(0, len(parts), 2):
    parts[k] = re.sub(r">([^<>]+)<", glue, parts[k])
out = out[:body_start] + "".join(parts)

(ROOT / "dispensaries" / "index.html").write_text(out)
print("missing:", *missing, sep="\n  ")
left = re.findall(r"(?i)[^<>]{0,40}(surgeon|patient|practice|consult|RealSelf|HIPAA|facelift|rhinoplasty|aesthetic)[^<>]{0,40}", re.sub(r"<script.*?</script>", "", out, flags=re.S))
print("leftover words:", len(left))
for x in left[:40]:
    print("  ", x)
