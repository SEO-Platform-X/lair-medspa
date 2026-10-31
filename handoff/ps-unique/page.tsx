import type { Metadata } from 'next';
import { bricolage, cormorant, hanken } from '@/lib/brand-fonts';
import { getTier } from '@/config/pricing-tiers';
import { formatUsd } from '@/lib/pricing-display';
import { Assurances } from '@/components/marketing/plastic-surgeon/Assurances';
import { Checklist } from '@/components/marketing/plastic-surgeon/Checklist';
import { Close } from '@/components/marketing/plastic-surgeon/Close';
import { Credibility } from '@/components/marketing/plastic-surgeon/Credibility';
import { Faq } from '@/components/marketing/plastic-surgeon/Faq';
import { Hero } from '@/components/marketing/plastic-surgeon/Hero';
import { HowItWorks } from '@/components/marketing/plastic-surgeon/HowItWorks';
import { MedSpaRoi } from '@/components/marketing/plastic-surgeon/MedSpaRoi';
import { MedSpaVideo } from '@/components/marketing/plastic-surgeon/MedSpaVideo';
import { People } from '@/components/marketing/plastic-surgeon/People';
import { Queries } from '@/components/marketing/plastic-surgeon/Queries';
import { Stats } from '@/components/marketing/plastic-surgeon/Stats';
import { Story } from '@/components/marketing/plastic-surgeon/Story';
import { FAQ, HERO, MED_SPA_PATH } from '@/components/marketing/plastic-surgeon/content';
import { buildOrganizationJsonLd, buildWebPageJsonLd, jsonLdScript } from '@/lib/seo/json-ld';
import { buildPublicMetadata } from '@/lib/seo/metadata';

const TITLE = 'How plastic surgeons get recommended by ChatGPT and AI search · Local AI Registry';
const DESCRIPTION =
  'Patients now ask ChatGPT, Gemini and Perplexity which plastic surgeon to see. Local AI Registry confirms your credentials, procedures and reviews everywhere AI looks, so it recommends your practice.';

// Absolute: the title already carries the brand, so the root template's
// " · Local AI Registry" suffix would print it twice.
export const metadata: Metadata = {
  ...buildPublicMetadata({ title: TITLE, description: DESCRIPTION, path: MED_SPA_PATH }),
  title: { absolute: TITLE },
};

/**
 * `/for/plastic-surgeons`. Same layout as the med spa page (LAI-819), with copy
 * written for surgeons plus two sections of its own (what patients ask AI, and
 * an FAQ with FAQPage JSON-LD) so the two pages don't read as duplicates.
 * Steve's prototype at seo-platform-x.github.io/lair-medspa/plastic-surgeons/
 * is the spec. Fully static.
 */
export default function PlasticSurgeonsPage() {
  const plansFrom = formatUsd(getTier('get_found').monthToMonth);
  const structured = [
    buildOrganizationJsonLd(),
    buildWebPageJsonLd({
      name: `${HERO.headline[0]} ${HERO.headline[1]}`,
      description: DESCRIPTION,
      path: MED_SPA_PATH,
      breadcrumb: [
        { name: 'Home', path: '/' },
        { name: 'By industry', path: '/for' },
        { name: 'Plastic surgeons', path: MED_SPA_PATH },
      ],
    }),
    {
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: FAQ.items.map((item) => ({
        '@type': 'Question',
        name: item.q,
        acceptedAnswer: { '@type': 'Answer', text: item.a },
      })),
    },
  ];

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: jsonLdScript(structured) }} />
      <div
        className={`${cormorant.variable} ${bricolage.variable} ${hanken.variable} overflow-clip bg-white font-hanken text-[17px] leading-normal text-brand-ink antialiased selection:bg-brand-blue selection:text-brand-paper`}
      >
        <main>
          <Hero />
          <MedSpaVideo />
          <Credibility />
          <Stats />
          <People />
          <Story />
          <Queries />
          <Checklist />
          <HowItWorks />
          <MedSpaRoi plansFrom={plansFrom} />
          <Assurances />
          <Faq />
          <Close />
        </main>
      </div>
    </>
  );
}
