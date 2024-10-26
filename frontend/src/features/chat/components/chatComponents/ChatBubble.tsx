import Image from "next/image";
import Markdown from "react-markdown";
import rehypeRaw from "rehype-raw";
import rehypeSanitize from "rehype-sanitize";
import remarkGfm from "remark-gfm";
import { v4 as uuidv4 } from "uuid";

import type { ChatBubbleProps } from "../types/chat.schema";

// Move the component definition for `img` outside of the `ChatBubble` component and pass the necessary data as props
const ImgComponent = ({ ...props }) => (
  <img style={{ maxWidth: "100%" }} {...props} alt="" />
);

export const ChatBubble = ({ isMe, content, carousell }: ChatBubbleProps) => {
  console.log(content);
  return (
    <div className="flex w-full items-start">
      <div
        className={`flex flex-col max-w-[70%] leading-1.5 p-4 my-2 border-gray-300 bg-white border-[1px] dark:bg-gray-700 ${
          isMe
            ? "rounded-s-xl rounded-se-xl ml-auto"
            : "rounded-e-xl rounded-ss-xl"
        }`}
      >
        <Markdown
          className="prose"
          remarkPlugins={[remarkGfm]}
          rehypePlugins={[rehypeRaw, rehypeSanitize]}
          components={{
            img: ImgComponent, // Use the component definition here
          }}
        >
          {content}
        </Markdown>
      </div>
    </div>
  );
};
