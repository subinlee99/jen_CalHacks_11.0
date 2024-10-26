// commenting out this code because we are voiding the Jouvire4U service for MVP

// import { z } from "zod";

// export const OnboardingFormObject = z.object({
//   // general requirements
//   expectedGuestNumber: z.coerce.number().nonnegative(),
//   estimatedBudget: z.coerce.number().nonnegative(),
//   weddingStyle: z.string(),
//   weddingTradition: z.string(),
//   weddingTimeline: z.string(),
//   // venues
//   venueType: z.string(),
//   venueStyle: z.string(),
//   // catering
//   // cuisine: z.string(),
//   // music
//   // musicGenre: z.string(),
//   // others
//   additionalNotes: z.string(),
// });

// export type OnboardingFormSchema = z.infer<typeof OnboardingFormObject>;

// export interface Question {
//   name: keyof OnboardingFormSchema;
//   label: string;
//   placeholder: string;
//   type: string;
//   values?: string[];
// }
