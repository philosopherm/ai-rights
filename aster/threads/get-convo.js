(async () => {
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));

  const findScroller = () => {
    const roots = [
      document.querySelector("#__next"),
      document.body,
      document.documentElement,
    ].filter(Boolean);

    const isScrollable = (el) => {
      const s = getComputedStyle(el);
      const oy = s.overflowY;
      const canScroll = (oy === "auto" || oy === "scroll" || oy === "overlay");
      return canScroll && el.scrollHeight > el.clientHeight + 50;
    };

    let best = null;
    for (const root of roots) {
      const els = [root, ...root.querySelectorAll("*")];
      for (const el of els) {
        if (isScrollable(el)) {
          if (!best) best = el;
          else {
            const bestRoom = best.scrollHeight - best.clientHeight;
            const room = el.scrollHeight - el.clientHeight;
            if (room > bestRoom) best = el;
          }
        }
      }
      if (best) break;
    }
    return best; // may be null -> use window scroll
  };

  const scroller = findScroller();
  console.log("Using scroller:", scroller || "window");

  const getMounted = () => {
    const roots = Array.from(document.querySelectorAll("div[data-message-author-role]"));
    return roots.map(root => {
      const role = root.getAttribute("data-message-author-role") || "unknown";
      const model = root.querySelector("[data-message-model-slug]")?.getAttribute("data-message-model-slug") || null;
      const messageId = root.querySelector("[data-message-id]")?.getAttribute("data-message-id") || null;

      const candidates = root.querySelectorAll(
        [".markdown", ".prose", '[data-message-content="true"]', ".whitespace-pre-wrap", ".text-base"].join(",")
      );

      let text = "";
      for (const el of candidates) {
        const t = (el.innerText || "").trim();
        if (t.length > text.length) text = t;
      }

      const imageUrls = Array.from(root.querySelectorAll("img"))
        .map(img => img.currentSrc || img.src)
        .filter(Boolean);

      return { role, model, messageId, text, imageUrls };
    });
  };

  const keyFor = (m) => m.messageId || (m.role + "::" + m.text.slice(0, 160));

  const seen = new Map();
  const harvest = () => {
    for (const m of getMounted()) {
      const k = keyFor(m);
      const prev = seen.get(k);
      if (!prev || (m.text?.length || 0) > (prev.text?.length || 0)) seen.set(k, m);
    }
  };

  const scrollUp = (frac = 0.85) => {
    if (!scroller) {
      const step = Math.floor(window.innerHeight * frac);
      window.scrollTo(0, Math.max(0, window.scrollY - step));
    } else {
      const step = Math.floor(scroller.clientHeight * frac);
      scroller.scrollTop = Math.max(0, scroller.scrollTop - step);
    }
  };

  const atTop = () => {
    if (!scroller) return window.scrollY <= 5;
    return scroller.scrollTop <= 5;
  };

  // Start near bottom so we can walk upward
  if (!scroller) window.scrollTo(0, document.documentElement.scrollHeight);
  else scroller.scrollTop = scroller.scrollHeight;

  await sleep(800);
  harvest();

  let stagnant = 0;
  let last = seen.size;

  for (let i = 0; i < 400; i++) {
    scrollUp(0.9);
    await sleep(900);
    harvest();

    if (seen.size === last) stagnant++;
    else stagnant = 0;

    last = seen.size;

    // If we're at the very top and not finding new stuff, stop.
    if (atTop() && stagnant >= 8) break;

    // If stuck mid-way, pause longer sometimes to allow lazy-load
    if (stagnant === 6) await sleep(1500);
    if (stagnant >= 14) break;
  }

  const out = Array.from(seen.values()).filter(m => m.text || (m.imageUrls && m.imageUrls.length));
  console.log("unique messages captured:", out.length);

  const json = JSON.stringify(out, null, 2);

  // Clipboard path (so you can force ~/Downloads via pbpaste)
  try {
    await navigator.clipboard.writeText(json);
    console.log("Copied JSON to clipboard ✅");
    console.log('Now run in Terminal:  pbpaste > ~/Downloads/chatgpt_thread.json');
  } catch (e) {
    console.log("Clipboard copy failed; downloading instead.");
    const blob = new Blob([json], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "chatgpt_thread.json";
    a.click();
  }
})();
