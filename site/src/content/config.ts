import { defineCollection, z } from 'astro:content';

const sessions = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    session: z.number().min(1).max(17).optional(), // omitted for retrospective
    week: z.number().min(1).max(5),
    weekTheme: z.string(),
    duration: z.string(),           // "30 min" | "60 min"
    objectives: z.array(z.string()),
    coreTeachingMoment: z.string(),
    takeaway: z.string(),
    status: z.enum([
      'complete',
      'in-progress',
      'planned'
    ]).default('complete'),
    order: z.number(),              // Explicit sort order (matches session number)
    isRetro: z.boolean().default(false),
  }),
});

export const collections = { sessions };
