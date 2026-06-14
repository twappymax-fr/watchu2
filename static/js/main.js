// hamburger toggle
function toggleMenu(btn) {
  btn.classList.toggle('open');
  document.getElementById('mobile-menu').classList.toggle('open');
}

// ── CAROUSEL ENGINE ──
const carousels = {
  stories: { index: 0, trackId: 'stories-track', timer: null },
  news:    { index: 0, trackId: 'news-track',    timer: null }
};

const AUTO_INTERVAL = 3500;

function getCardWidth(trackEl) {
  if (!trackEl.children.length) return 0;
  return trackEl.children[0].offsetWidth + 16; // 16 = gap
}

function applySlide(name, instant) {
  const c = carousels[name];
  const track = document.getElementById(c.trackId);
  const cardW = getCardWidth(track);
  const visible = Math.max(1, Math.floor(track.parentElement.offsetWidth / cardW));
  const max = Math.max(0, track.children.length - visible);
  c.index = Math.min(Math.max(c.index, 0), max);
  if (instant) {
    track.style.transition = 'none';
    track.style.transform = `translateX(-${c.index * cardW}px)`;
    requestAnimationFrame(() => requestAnimationFrame(() => {
      track.style.transition = '';
    }));
  } else {
    track.style.transform = `translateX(-${c.index * cardW}px)`;
  }
}

function slide(name, dir) {
  const c = carousels[name];
  const track = document.getElementById(c.trackId);
  const cardW = getCardWidth(track);
  const visible = Math.max(1, Math.floor(track.parentElement.offsetWidth / cardW));
  const max = Math.max(0, track.children.length - visible);
  c.index = c.index + dir;
  if (c.index > max) c.index = 0;
  if (c.index < 0)   c.index = max;
  applySlide(name);
  resetTimer(name);
}

function startTimer(name) {
  const c = carousels[name];
  c.timer = setInterval(() => slide(name, 1), AUTO_INTERVAL);
}

function resetTimer(name) {
  const c = carousels[name];
  clearInterval(c.timer);
  startTimer(name);
}

// ── DRAG / TOUCH ──
function initDrag(name) {
  const c = carousels[name];
  const wrap = document.getElementById(c.trackId).parentElement;
  let startX = 0, startIndex = 0, isDragging = false;

  function onDown(e) {
    isDragging = true;
    startX = e.type === 'touchstart' ? e.touches[0].clientX : e.clientX;
    startIndex = c.index;
    clearInterval(c.timer);
    wrap.style.cursor = 'grabbing';
  }

  function onMove(e) {
    if (!isDragging) return;
    const x = e.type === 'touchmove' ? e.touches[0].clientX : e.clientX;
    const dx = startX - x;
    const track = document.getElementById(c.trackId);
    const cardW = getCardWidth(track);
    track.style.transition = 'none';
    track.style.transform = `translateX(-${startIndex * cardW + dx}px)`;
  }

  function onUp(e) {
    if (!isDragging) return;
    isDragging = false;
    wrap.style.cursor = '';
    const x = e.type === 'touchend'
      ? e.changedTouches[0].clientX
      : e.clientX;
    const dx = startX - x;
    const track = document.getElementById(c.trackId);
    track.style.transition = '';
    const cardW = getCardWidth(track);
    if (Math.abs(dx) > cardW * 0.25) {
      slide(name, dx > 0 ? 1 : -1);
    } else {
      applySlide(name);
      resetTimer(name);
    }
  }

  wrap.addEventListener('mousedown',  onDown);
  window.addEventListener('mousemove', onMove);
  window.addEventListener('mouseup',   onUp);

  wrap.addEventListener('touchstart', onDown, { passive: true });
  wrap.addEventListener('touchmove',  onMove, { passive: true });
  wrap.addEventListener('touchend',   onUp);

  wrap.addEventListener('mouseenter', () => clearInterval(c.timer));
  wrap.addEventListener('mouseleave', () => { if (!isDragging) startTimer(name); });
}

// ── INIT ──
document.addEventListener('DOMContentLoaded', () => {
  Object.keys(carousels).forEach(name => {
    initDrag(name);
    startTimer(name);
  });
});
