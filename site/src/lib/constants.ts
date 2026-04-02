export const WEEKS = [
  { number: 1, theme: 'How LLMs Actually Work',                              label: 'Foundations' },
  { number: 2, theme: 'Tell the Model What It Can and Cannot Do',            label: 'Evaluation & Guidance' },
  { number: 3, theme: 'Making Behavior Persistent',                          label: 'Thinking in Agents' },
  { number: 4, theme: 'Constraining the Agent Makes It Perform Better',      label: 'Harness Engineering' },
  { number: 5, theme: 'The Capstone Skill',                                  label: 'Spec-Driven Development' },
] as const;

export type Week = (typeof WEEKS)[number];
