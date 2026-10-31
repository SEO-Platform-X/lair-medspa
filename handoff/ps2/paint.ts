/** The income chart: each bar grows in turn, and its share appears once it lands. */
function paintRace(story: HTMLElement, p: number): void {
  story.querySelectorAll<SVGRectElement>('.ib').forEach((bar, i) => {
    const full = Number(bar.dataset.h);
    const k = clamp((p - 0.08 - i * 0.18) / 0.3);
    bar.setAttribute('height', String(full * k));
    bar.setAttribute('y', String(210 - full * k));
  });
  story.querySelectorAll<SVGElement>('.il').forEach((label, i) => {
    label.style.opacity = p >= 0.38 + i * 0.18 ? '1' : '0';
  });
}
