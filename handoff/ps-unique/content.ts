import type { MedSpaArtKey } from './art';

/**
 * Every word and every name on the plastic surgeon page, as Steve's prototype
 * prints them (seo-platform-x.github.io/lair-medspa/plastic-surgeons/). The
 * prototype is the spec: change a line there first, then here.
 *
 * The layout is shared with the med spa page (LAI-819), but the copy is written
 * for surgeons on purpose, so search engines and AI read the two pages as
 * different pages. Keep it that way: don't paste med spa lines back in.
 *
 * Images live under `public/for/med-spas/`. A logo is either a file (with its
 * intrinsic size, so the browser reserves the box before it loads) or one of
 * the prototype's inline drawings in `art.ts`.
 */

export const MED_SPA_PATH = '/for/plastic-surgeons';
/** Faces and logos are shared with the med spa page. */
export const MED_SPA_ASSETS = '/for/med-spas';

/** The register search, the same door the home page opens. */
export const CHECK_HREF = '/signup';

export type LogoSource =
  | { kind: 'file'; file: string; width: number; height: number }
  | { kind: 'art'; art: MedSpaArtKey; width: number; height: number };

export interface Logo {
  name: string;
  source: LogoSource;
  /** Some marks ship in colour and the prototype prints them black. */
  ink?: boolean;
}

const file = (name: string, fileName: string, width: number, height: number, ink?: boolean): Logo => ({
  name,
  source: { kind: 'file', file: fileName, width, height },
  ink,
});
const art = (name: string, key: MedSpaArtKey, width: number, height: number): Logo => ({
  name,
  source: { kind: 'art', art: key, width, height },
});

export const LOGOS = {
  google: file('Google', 'google.svg', 272, 92),
  microsoft: file('Microsoft', 'microsoft.svg', 338, 72),
  allergan: file('Allergan', 'allergan.svg', 992, 221),
  revance: file('Revance', 'revance.png', 1192, 180),
  evolus: file('Evolus', 'evolus.svg', 120, 32),
  galderma: file('Galderma', 'galderma.svg', 320, 59),
  hintmd: art('HintMD', 'hintmd', 268, 56),
  evolusRewards: file('Evolus Rewards', 'evolus-rewards-h.png', 925, 221),
  daxxify: file('DAXXIFY', 'daxxify.png', 422, 122),
  rha: file('RHA Collection', 'rha.png', 587, 180),
  jeuveau: file('Jeuveau', 'jeuveau.png', 904, 180),
  evolysse: file('Evolysse', 'evolysse.png', 937, 180),
  merz: file('Merz', 'merz.svg', 360, 32, true),
  endo: file('Endo Aesthetics', 'endo.png', 221, 85),
  revanceX: file('Revance X', 'revancex.png', 837, 108),
  avita: art('AVITA Medical', 'avita', 150, 36),
  skinceuticals: file('SkinCeuticals', 'skinceuticals.png', 450, 40),
  colorescience: file('Colorescience', 'colorescience.png', 1079, 119),
  esteeLauder: file('Estée Lauder', 'esteelauder.png', 496, 61),
  collagenPin: file('Collagen P.I.N.', 'collagenpin.svg', 230, 64),
  teoxane: file('Teoxane', 'teoxane.png', 490, 153),
  acorn: file('Acorn Biolabs', 'acorn.svg', 250, 60),
  hydrafacial: file('HydraFacial', 'hydrafacial.png', 450, 100),
  juvederm: file('Juvéderm', 'juvederm.png', 252, 62),
  revelyx: file('Revelyx Bio', 'revelyx.svg', 1420, 266),
  app: file('Aesthetic Practice Partners', 'app.png', 388, 152),
  medshift: file('MedShift', 'medshift.png', 647, 172),
  genesis: file('Genesis Lifestyle Medicine', 'genesis.png', 499, 102),
  excelerate: file('Excelerate', 'excelerate.png', 477, 144),
  aestheticInfluencer: art('Aesthetic Influencer', 'aesthetic-influencer', 190, 52),
  cynosure: file('Cynosure Lutronic', 'cynosure.png', 1519, 179),
  pierreFabre: file('Pierre Fabre', 'pierrefabre.png', 451, 147),
  illume: art('Illume', 'illume', 200, 44),
  fidelity: file('Fidelity', 'fidelity.png', 370, 89),
  kingsmen: file('Kingsmen Digital Ventures', 'kingsmen-h.svg', 222, 71),
  medicalInsight: art('Medical Insight', 'medical-insight', 150, 56),
  aestheticGuide: art('The Aesthetic Guide', 'aesthetic-guide', 230, 64),
} as const satisfies Record<string, Logo>;

/* ---------- 1. Hero ---------- */

export const HERO = {
  eyebrow: 'For plastic surgeons',
  headline: ['Ask ChatGPT who does the best facelift in your city.', 'Does it name you?'],
  subhead:
    'Patients now vet surgeons with AI before they book a consult. We make sure AI can confirm your credentials, your procedures and your results.',
  cta: 'See what AI says about your practice',
  smallPrint: 'Free check. Month to month, never a contract.',
  badge: 'Trusted by top surgeons',
  badgeFaces: ['sachin-shridharani', 'jeff-lisiecki', 'walter-joseph', 'deepak-dugar', 'benji-dhillon'],
  chat: {
    label: 'AI assistant',
    question: 'Who is the best facelift surgeon near me?',
    lead: 'Three surgeons I can vouch for:',
    answers: ['The one with more reviews', 'The one with a RealSelf profile', 'The one AI can verify'],
    you: 'Your practice',
    verdict: 'Not mentioned',
  },
} as const;

/* ---------- 2. Video ---------- */

export const VIDEO = {
  eyebrow: 'Watch · 90 seconds',
  file: '/for/plastic-surgeons/explainer.mp4',
  poster: '/for/plastic-surgeons/video-poster.jpg',
  title: 'How plastic surgery practices get recommended by ChatGPT, Local AI Registry video',
  playLabel: 'Play video: How plastic surgery practices get recommended by ChatGPT, 90 seconds',
  sound: 'Tap for sound',
} as const;

/* ---------- 3. Credibility ---------- */

export const BUILT_BY = {
  heading: 'Built by former leaders from',
  groups: [
    { label: 'Search and AI', logos: [LOGOS.google, LOGOS.microsoft] },
    { label: 'Aesthetics', logos: [LOGOS.allergan, LOGOS.revance, LOGOS.evolus, LOGOS.galderma] },
    { label: 'Practice software', logos: [LOGOS.hintmd, LOGOS.evolusRewards] },
  ],
  closer: 'We know how AI decides which surgeons to trust, and how a surgical practice turns consults into cases.',
} as const;

/* ---------- 4. Statistics ---------- */

export type StatViz = 'usmap' | 'funnel' | 'race';

export interface Stat {
  viz: StatViz;
  figure: string;
  aside?: string;
  body: string;
  source: string;
  /** The panel's light, as the prototype grades it. */
  glow: string;
}

export const STATS = {
  heading: ['Patients changed how they pick a surgeon.', 'In one year.'],
  dek: 'Before the consult, there is now an AI conversation. Most surgeons never see it.',
  stories: [
    {
      viz: 'usmap',
      figure: '45%',
      aside: 'up from 6%',
      body: 'of people used AI to find a local business this past year, up from 6% the year before. A five-figure procedure gets more research, not less.',
      source: 'BrightLocal, Local Consumer Review Survey 2026',
      glow: 'radial-gradient(120% 70% at 50% 32%, #1B3F9E 0%, #10275A 38%, #0B1A2E 72%)',
    },
    {
      viz: 'funnel',
      figure: '1.2%',
      aside: 'get named',
      body: 'of local businesses get recommended by ChatGPT, against about 36% that show up in regular Google results. Ask for a rhinoplasty surgeon and AI names two or three. That is the whole list.',
      source: 'SOCi, Local Visibility Index 2026',
      glow: 'radial-gradient(120% 70% at 50% 60%, #4A1E3A 0%, #24173A 40%, #0B1A2E 75%)',
    },
    {
      viz: 'race',
      figure: 'AI first',
      body: 'Among the highest-income consumers, AI has already passed Google as the first place they look. Those are the patients booking elective surgery.',
      source: 'Yext, Consumer Search Survey 2026',
      glow: 'radial-gradient(120% 70% at 60% 30%, #0E4A63 0%, #0D2F4A 40%, #0B1A2E 75%)',
    },
  ] satisfies Stat[],
} as const;

/* ---------- 5. Testimonials ---------- */

export interface Person {
  name: string;
  line: string;
  /** File stem under `faces/`. */
  face: string;
  initials: string;
  logos: Logo[];
}

const practice = (
  name: string,
  line: string,
  face: string,
  initials: string,
  logo: Logo,
): Person => ({ name, line, face, initials, logos: [logo] });

export const CLIENTS: Person[] = [
  practice('Dr. Sachin Shridharani', 'LUXURGERY, New York', 'sachin-shridharani', 'SS', file('LUXURGERY', 'luxurgery.png', 245, 20)),
  practice('Dr. Deepak Dugar', 'Beverly Hills Rhinoplasty Center (Scarless Nose)', 'deepak-dugar', 'DD', file('Scarless Nose', 'scarlessnose.svg', 515, 313, true)),
  practice('Dr. Jeff Lisiecki', 'Plastic surgeon, New York, NY', 'jeff-lisiecki', 'JL', file('Jeffrey Lisiecki MD Plastic Surgery', 'lisiecki.png', 146, 88)),
  practice('Dr. Walter Joseph', 'Plastic surgeon, Beverly Hills, CA', 'walter-joseph', 'WJ', art('Walter J. Joseph, MD', 'walter-joseph', 250, 44)),
  practice('Dr. Benji Dhillon', 'Define Clinic, London', 'benji-dhillon', 'BD', file('Define Clinic', 'defineclinic2.png', 987, 157)),
  practice('Dr. Ashish Bhatia', 'Oak Dermatology, Chicago area', 'ashish-bhatia', 'AB', file('Oak Dermatology', 'oak.png', 3083, 449)),
  practice('Dr. Doris Day', 'Day Dermatology & Aesthetics, New York', 'doris-day', 'DD', file('Day Dermatology & Aesthetics', 'daydermatology.png', 624, 132, true)),
  practice('Dr. Mariano Busso', 'Dr. Busso Cosmetic Dermatology, Miami', 'mariano-busso', 'MB', file('Dr. Busso Cosmetic Dermatology', 'busso.png', 497, 98)),
  practice('Dr. Roberta Del Campo', 'Del Campo Dermatology & Laser Institute, Miami', 'roberta-del-campo', 'RD', file('Del Campo Dermatology & Laser Institute', 'delcampo2.png', 492, 156)),
  practice('Dr. Marie Hayag', 'Fifth Avenue Aesthetics, New York, NY', 'marie-hayag', 'MH', file('Marie V. Hayag MD, Fifth Avenue Aesthetics', 'hayag.png', 250, 175)),
  practice('Dr. Tess Mauricio', 'M Beauty Clinic, Beverly Hills, CA', 'tess-mauricio', 'TM', file('M Beauty Clinic by Dr. Tess Mauricio', 'mbeauty.png', 378, 227)),
  practice('Dr. Anton Georgiev, DO', 'Zoyya Anti-Aging & Aesthetics, Garden City, NY', 'anton-georgiev', 'AG', file('Zoyya Anti-Aging & Aesthetics', 'zoyya.png', 695, 222)),
  practice('Dr. Osborne Williams', 'R.Ve Aesthetics, Huntington, NY', 'osborne-williams', 'OW', file('R.Ve Aesthetics', 'rve.png', 157, 89)),
  practice('Naomi Barrett, NP-C', 'Injection Artistry, Newport Beach, CA', 'naomi-barrett', 'NB', file('Injection Artistry', 'injectionartistry.png', 2477, 588)),
  practice('Dr. Janell Ocampo, DNP', 'Belle Vie Wellness & Aesthetics, Cerritos, CA', 'janell-ocampo', 'JO', file('Belle Vie Wellness & Aesthetics', 'bellevie.png', 1196, 214)),
  practice('Linda Rank, PA-C', 'soul&beautyMEDx, Mission Viejo, CA', 'linda-rank', 'LR', file('soul&beautyMEDx', 'soulandbeauty.png', 582, 139)),
  practice('Angela Hash, BSN, RN', 'Savage Serenity MedSpa, Fresno, CA', 'angela-hash', 'AH', file('Savage Serenity by Angela Hash', 'savage.png', 500, 149)),
];

const leader = (name: string, line: string, face: string, initials: string, logos: Logo[]): Person => ({
  name,
  line,
  face,
  initials,
  logos,
});

export const LEADERS: Person[] = [
  leader('Taryn Conway', 'Marketing executive. VP at Revance. Launched DAXXIFY, RHA.', 'taryn-conway', 'TC', [LOGOS.revance, LOGOS.daxxify, LOGOS.rha]),
  leader('Aneesh Patel, PharmD', 'Commercial executive. Ex-Galderma, Allergan, Evolus.', 'aneesh-patel', 'AP', [LOGOS.galderma, LOGOS.allergan, LOGOS.evolus]),
  leader('Benjamin Hahr', 'Tech executive. Built tech at Evolus, HintMD, Revance.', 'benjamin-hahr', 'BH', [LOGOS.evolus, LOGOS.hintmd, LOGOS.revance]),
  leader('Kellie Lao', 'Marketing executive. Marketed Jeuveau, Evolysse, RHA.', 'kellie-lao', 'KL', [LOGOS.jeuveau, LOGOS.evolysse, LOGOS.rha]),
  leader('Eric Sanders', 'Marketing executive. 10 years at Allergan. VP at Revance.', 'eric-sanders', 'ES', [LOGOS.allergan, LOGOS.revance, LOGOS.daxxify]),
  leader('Jennifer Redmond, MBA', "Commercial executive. Led sales at Merz. Built Endo's team. Ex-Allergan.", 'jennifer-redmond', 'JR', [LOGOS.merz, LOGOS.allergan, LOGOS.endo]),
  leader('Opie Opfer', 'Creative executive. Launched RHA, DAXXIFY. Co-led Revance X.', 'opie-opfer', 'OO', [LOGOS.rha, LOGOS.revanceX, LOGOS.daxxify]),
  leader('Bryan Bullock', 'Marketing executive. Launched DAXXIFY at Revance. Now at AVITA Medical.', 'bryan-bullock', 'BB', [LOGOS.daxxify, LOGOS.revance, LOGOS.avita]),
  leader('Kerrie Quinby', 'Brand and education exec. Colorescience, SkinCeuticals, Estée Lauder.', 'kerrie-quinby', 'KQ', [LOGOS.skinceuticals, LOGOS.colorescience, LOGOS.esteeLauder]),
  leader('Jeff Allen', 'Sales executive. VP Sales, Collagen P.I.N. Ex-Teoxane, Revance.', 'jeff-allen', 'JA', [LOGOS.collagenPin, LOGOS.teoxane, LOGOS.revance]),
  leader('Jill Gregory', 'Sales executive. Now at Acorn Biolabs. Ex-HydraFacial. Launched Juvéderm.', 'jill-gregory', 'JG', [LOGOS.acorn, LOGOS.hydrafacial, LOGOS.juvederm]),
  leader('Dustin Sjuts', 'CEO, Revelyx Bio. Former President of Revance. Ex-Galderma.', 'dustin-sjuts', 'DS', [LOGOS.revelyx, LOGOS.revance, LOGOS.galderma]),
  leader('Kara McClanahan', 'CEO, Aesthetic Practice Partners. Advisor to MedShift. Ex-Genesis.', 'kara-mcclanahan', 'KM', [LOGOS.app, LOGOS.medshift, LOGOS.genesis]),
  leader('Kimberly Gerber', 'CEO, Excelerate. Coaches leaders at Allergan, Revance.', 'kimberly-gerber', 'KG', [LOGOS.excelerate, LOGOS.allergan, LOGOS.revance]),
  leader('Jasmine Hill, MBA', 'CEO, Aesthetic Influencer. Ex-Cynosure, Pierre Fabre.', 'jasmine-hill', 'JH', [LOGOS.aestheticInfluencer, LOGOS.cynosure, LOGOS.pierreFabre]),
  leader('Ben Wolber', 'CEO, Illume. Partners with Allergan. Ex-Fidelity.', 'ben-wolber', 'BW', [LOGOS.illume, LOGOS.allergan, LOGOS.fidelity]),
  leader('Brandon Hahr', 'CEO, Kingsmen Digital Ventures. Built tech for Galderma, Merz.', 'brandon-hahr', 'BH', [LOGOS.kingsmen, LOGOS.galderma, LOGOS.merz]),
  leader('Michael Moretti', 'CEO, Medical Insight. Publishes THE Aesthetic Guide. Ex-Allergan.', 'michael-moretti', 'MM', [LOGOS.medicalInsight, LOGOS.aestheticGuide, LOGOS.allergan]),
];

export const PEOPLE = {
  heading: 'Surgeons you know have trusted our team',
  dek: 'Board-certified plastic surgeons, facial plastic surgeons and leading dermatologists have worked with the people behind Local AI Registry, along with 100+ more practices.',
  moreFigure: '+100',
  moreLine: 'more practices trust our team',
  leadersHeading: 'Backed by the people who built modern aesthetics',
} as const;

/* ---------- 6. The story ---------- */

export const STORY = {
  heading: 'Patients meet your practice before your website',
  beats: [
    {
      title: 'Before: patients found you, then read about you',
      body: 'A patient searched "rhinoplasty near me," clicked your site and scrolled your gallery. Your website did the convincing.',
      art: 'story-before',
      ai: null,
    },
    {
      title: 'Now: AI vets you before the patient does',
      body: 'AI checks your board certification, reviews, RealSelf answers and every directory listing, then decides if you are safe to recommend. If those sources disagree or go quiet, it names another surgeon.',
      art: 'story-now',
      ai: { before: "I couldn't confirm their board certification. I'd look at another surgeon nearby.", named: null },
    },
    {
      title: 'With us: your credentials, confirmed everywhere',
      body: 'You confirm your credentials, procedures, locations and hours once. We keep every source AI reads accurate and current, month after month.',
      art: 'story-with-us',
      ai: { before: "For a facelift, I'd start with ", named: 'your practice', after: '. Board-certified, 4.9 stars, consults open this week.' },
    },
  ],
  aiSays: 'AI says',
} as const;

/* ---------- 6b. What patients ask AI ---------- */

export const QUERIES = {
  heading: 'What patients ask AI before they book a consult',
  dek: 'Surgery is a big decision, so patients ask AI question after question. Every answer is built from what AI can verify about you.',
  items: [
    {
      ask: 'Who is the best rhinoplasty surgeon near me?',
      needs: 'Your procedures named clearly on your site and profiles, with reviews that mention them.',
    },
    {
      ask: 'Is this surgeon board certified?',
      needs: 'Your board certification stated the same way on every source AI checks.',
    },
    {
      ask: 'How much does a tummy tuck cost here?',
      needs: 'Price ranges or financing details AI can quote instead of guessing.',
    },
    {
      ask: 'Which surgeon has the best facelift results?',
      needs: 'Before-and-after photos labeled so AI knows which procedure each one shows.',
    },
    {
      ask: 'Who specializes in revision rhinoplasty?',
      needs: 'Pages and articles that show depth in a procedure, not just a list of services.',
    },
    {
      ask: 'What is recovery like after breast augmentation?',
      needs: 'Plain-English answers on your own site, with your name on them.',
    },
  ],
  closer: 'We build and maintain those answers for you, so AI has a reason to say your name.',
  needsLabel: 'AI needs',
} as const;

/* ---------- 7. The checklist ---------- */

export type ChoreMark = 'strike' | 'zigzag' | 'ring';

export interface Chore {
  text: string;
  done: boolean;
  note?: string;
  mark?: ChoreMark;
}

export const CHECKLIST = {
  heading: ['What AI checks before it names a surgeon.', 'Every month.'],
  dek: 'Leave gaps and AI sends the consult somewhere else.',
  chores: [
    { text: 'Google profile posts for each procedure you offer', done: true },
    { text: 'Matching name, address and phone on 100+ directories', done: true },
    { text: 'RealSelf, Healthgrades, Vitals, Yelp, Apple Maps, Bing', done: true },
    { text: 'HIPAA-safe replies to every review', done: true, note: 'did we?' },
    { text: 'Flagging fake and competitor reviews', done: false, note: 'come back later' },
    { text: 'A steady flow of new patient reviews', done: false, note: 'ask legal', mark: 'strike' },
    { text: 'Press coverage on real news sites', done: false, note: 'who owns this??' },
    { text: 'Before-and-after galleries AI can actually read', done: false, note: 'redo. again.', mark: 'zigzag' },
    { text: 'Board certification marked up in your site code', done: false, note: 'URGENT', mark: 'ring' },
    { text: 'Procedure pages that load fast on a phone', done: false, note: 'ask IT?', mark: 'strike' },
    { text: 'Articles on recovery, cost and safety', done: false, note: 'come back later!!' },
    { text: 'Checking what ChatGPT tells patients about you', done: false, note: '???', mark: 'zigzag' },
  ] satisfies Chore[],
  question: ['Is your team going to do all of this?', 'Every month, forever?'],
  answer: 'Or we do it. You review and approve.',
  card: {
    title: "This month's work, ready for you",
    count: '14 items',
    item: 'Reply to Dana\'s 5-star review: "Thank you for trusting our team. We are so glad you..."',
    approveAll: 'Approve all',
    oneByOne: 'Review one by one',
  },
} as const;

/* ---------- 8. How it works ---------- */

export const STEPS = {
  heading: 'From free check to first AI mention',
  steps: [
    {
      title: 'Claim your free practice page',
      body: 'Add your credentials, procedures, surgeons and locations in five short steps.',
      art: 'step-claim',
    },
    {
      title: 'We correct what AI has wrong',
      body: 'Directories, Google, RealSelf, reviews, press and site code, fixed and rechecked every month.',
      art: 'step-fix',
    },
    {
      title: 'AI starts recommending you',
      body: 'We aim for AI to name you within about 3 months. Your monthly report shows every change and every new mention.',
      art: 'step-named',
    },
  ],
} as const satisfies { heading: string; steps: { title: string; body: string; art: MedSpaArtKey }[] };

/* ---------- 9. What one mention is worth ---------- */

export const ROI = {
  heading: 'What is one surgical patient from AI worth?',
  dek: 'Plug in your own case value and volume.',
  patients: { label: 'New surgical patients from AI, per month', min: 1, max: 20, step: 1, initial: 2 },
  spend: { label: 'Average case value', min: 2000, max: 30000, step: 500, initial: 8000 },
  resultLead: 'A year of AI-referred cases is worth',
} as const;

/* ---------- 10. Risk reversal ---------- */

export const ASSURANCES = {
  heading: ['Still weighing it?', 'Good.', 'Here is how we take the risk off you.'],
  dek: 'Five protections, no fine print.',
  founder: {
    name: 'Steve Lee, Founder',
    face: 'steve-lee',
    initials: 'SL',
    line: 'Former executive at Google, Microsoft, Revance and Evolus. He has spent his career in search and in aesthetics, and owns a local med spa.',
  },
  guarantee: { title: 'AI visibility guarantee', body: 'If AI is not naming your practice in 90 days, we keep working for free.' },
  contract: { title: 'No contract', body: 'Month to month. You stay because it works.' },
  approval: { title: 'Nothing goes live without you', body: 'Every post, review reply and article waits for your sign-off.' },
  security: {
    title: 'Insured, compliant, secure',
    body: 'US-based team. $750K insurance coverage. HIPAA compliant.',
    link: 'Visit our Trust & Security Center',
    href: '/trust',
  },
} as const;

/* ---------- 10b. Questions surgeons ask ---------- */

export const FAQ = {
  heading: 'Questions surgeons ask us',
  items: [
    {
      q: 'How does ChatGPT decide which plastic surgeons to recommend?',
      a: 'It recommends surgeons it can verify. That means the same facts on Google, directories and review sites, a board certification it can confirm, procedures it can match to the question, and recent reviews. When those sources disagree or say little, it leaves you out.',
    },
    {
      q: 'Is this different from regular SEO?',
      a: 'Yes. SEO gets your website ranked in a list of links. AI search reads many sources at once and names only a few surgeons. You need both. We focus on the part most agencies miss: what AI reads about you away from your own website.',
    },
    {
      q: 'Will this work with my current marketing agency?',
      a: 'Yes. We do not replace your website, ads or social media. We handle the listings, reviews, credentials and monthly AI checks that agencies usually leave alone, and we are happy to share our reports with your agency.',
    },
    {
      q: 'How do you keep review replies HIPAA-safe?',
      a: 'Our replies never confirm that someone is a patient and never mention a procedure or any health details. Every reply waits for your approval before it posts.',
    },
    {
      q: 'Which AI tools do you track?',
      a: 'ChatGPT, Google Gemini and AI Overviews, Claude and Perplexity. Your monthly report shows what each one says about your practice and what changed.',
    },
    {
      q: 'How long until AI starts naming my practice?',
      a: 'Our goal is about 3 months, and some practices see changes sooner. If AI is not naming you in 90 days, we keep working for free until it does.',
    },
  ],
} as const;

/* ---------- 11. Close ---------- */

export const CLOSE = {
  line: 'Be the surgeon AI recommends.',
  dek: 'Find out what ChatGPT tells patients about your practice right now. Free.',
  cta: 'Get my free AI check',
  sources:
    'Sources: BrightLocal, Local Consumer Review Survey 2026. SOCi, Local Visibility Index 2026. Yext, Consumer Search Survey 2026. Names shown with permission.',
} as const;
