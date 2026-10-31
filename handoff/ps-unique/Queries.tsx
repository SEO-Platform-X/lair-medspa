import { QUERIES } from './content';

/** The questions patients put to AI before a consult, and what AI needs to answer each with your name. */
export function Queries() {
  return (
    <section className="bg-brand-paper px-5 py-[96px] text-brand-ink">
      <div className="mx-auto max-w-[720px]">
        <h2 className="m-0 font-cormorant text-[36px] font-medium leading-[1.05] tracking-[-0.005em]">
          {QUERIES.heading}
        </h2>
        <p className="mb-10 mt-3 max-w-[560px] text-brand-ink/75">{QUERIES.dek}</p>
        <ul className="m-0 grid list-none grid-cols-1 gap-3 p-0 sm:grid-cols-2">
          {QUERIES.items.map((item) => (
            <li key={item.ask} className="flex flex-col gap-2 rounded-2xl bg-white p-5">
              <p className="m-0 font-bricolage text-[17px] font-bold leading-snug">
                {'“'}
                {item.ask}
                {'”'}
              </p>
              <p className="m-0 text-[15px] leading-normal text-brand-ink/75">
                <span className="font-bold text-brand-blue">{QUERIES.needsLabel}: </span>
                {item.needs}
              </p>
            </li>
          ))}
        </ul>
        <p className="mb-0 mt-8 font-bricolage text-[19px] font-bold">{QUERIES.closer}</p>
      </div>
    </section>
  );
}
