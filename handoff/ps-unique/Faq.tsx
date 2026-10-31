import { FAQ } from './content';

/**
 * Questions surgeons ask before signing up. Answers sit in the server-rendered
 * HTML inside <details>, so crawlers and AI read them even when collapsed.
 * The page adds the matching FAQPage JSON-LD.
 */
export function Faq() {
  return (
    <section className="bg-brand-paper px-5 py-[96px] text-brand-ink">
      <div className="mx-auto max-w-[720px]">
        <h2 className="mb-8 mt-0 font-cormorant text-[36px] font-medium leading-[1.05] tracking-[-0.005em]">
          {FAQ.heading}
        </h2>
        <div className="flex flex-col gap-3">
          {FAQ.items.map((item) => (
            <details key={item.q} className="group rounded-2xl bg-white p-5">
              <summary className="flex cursor-pointer list-none items-start justify-between gap-4 font-bricolage text-[18px] font-bold leading-snug [&::-webkit-details-marker]:hidden">
                <span>{item.q}</span>
                <span
                  aria-hidden="true"
                  className="flex-none text-[22px] leading-none text-brand-blue transition-transform group-open:rotate-45 motion-reduce:transition-none"
                >
                  +
                </span>
              </summary>
              <p className="mb-0 mt-3 text-brand-ink/80">{item.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}
