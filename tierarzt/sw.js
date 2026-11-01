// Offline-Unterstützung: Spiel und alle Sprachdateien werden beim ersten Öffnen gespeichert,
// danach läuft das Spiel auch ohne Internet. Neue Version: Zahl bei CACHE erhöhen.
const CACHE = 'tierarzt-v2';
const FILES = ['./', './index.html', './manifest.webmanifest', './icon-180.png', './icon-192.png', './icon-512.png', './ton/liste.json'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(async c => {
    await c.addAll(FILES);
    try {
      const l = await (await fetch('./ton/liste.json')).json();
      await c.addAll(l.map(n => './ton/' + n + '.mp3'));
    } catch (err) {}
  }));
  self.skipWaiting();
});
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('tierarzt') && k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.pathname.endsWith('.mp3')) {  // Sprachdateien: zuerst aus dem Speicher
    e.respondWith(caches.match(e.request, { ignoreSearch: true }).then(hit => hit || fetch(e.request).then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); return r; })));
    return;
  }
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request, { ignoreSearch: true })));
});
