import { getCollection } from 'astro:content';

export async function getAllSessions() {
  const sessions = await getCollection('sessions');
  return sessions.sort((a, b) => a.data.order - b.data.order);
}

export async function getSessionsByWeek() {
  const sessions = await getAllSessions();
  const grouped = new Map<number, typeof sessions>();
  for (const session of sessions) {
    const week = session.data.week;
    if (!grouped.has(week)) grouped.set(week, []);
    grouped.get(week)!.push(session);
  }
  return grouped;
}

export async function getAdjacentSessions(currentSlug: string) {
  const all = await getAllSessions();
  const idx = all.findIndex(s => s.slug === currentSlug);
  return {
    prev: idx > 0 ? all[idx - 1] : null,
    next: idx < all.length - 1 ? all[idx + 1] : null,
  };
}
