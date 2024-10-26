export interface Vendor {
  Title: string;
  Description: string;
  GoogleReviews: string;
  Address: string;
  Image: string;
  ContactNumber: string;
  Email: string;
  Pricing: string;
  Link: string;
}

export interface ChatBubbleProps {
  isMe: boolean;
  content: string;
  carousell?: { title: string; description: string; image: string }[];
  id?: string;
}

// keep this interface aligned with the RequestBody in the backend
export interface RequestBody {
  userResponse: string;
}

interface CarousellPictures {
  title: string;
  description: string;
  image: string;
}

// keep this interface aligned with the RequestOutput in the backend
export interface RequestOutput {
  isMe: boolean;
  content: string;
  options?: string[];
  followUp?: boolean;
  carousell?: CarousellPictures[];
}
