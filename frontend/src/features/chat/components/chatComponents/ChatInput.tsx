import React, { useLayoutEffect, useRef, useState } from "react";

import { PaperPlaneIcon } from "@radix-ui/react-icons";

export interface ChatInputProps {
  sendButtonPressed: (text: string) => void;
}

export const ChatInput = ({ sendButtonPressed }: ChatInputProps) => {
  const textbox = useRef<HTMLTextAreaElement>(null);
  const [text, setText] = useState("");

  // Text Area heights
  const ONE_LINE_HEIGHT = "24px";
  const ORIGINAL_HEIGHT = "40px";

  // Adds an extra line for the text area when the user types
  function adjustHeight() {
    if (textbox.current) {
      textbox.current.style.height = ONE_LINE_HEIGHT;
      textbox.current.style.height = `${textbox.current.scrollHeight}px`;
    }
  }

  useLayoutEffect(adjustHeight, []);

  function handleKeyDown(event: React.ChangeEvent<HTMLTextAreaElement>) {
    setText(event.target.value);
    adjustHeight();
  }

  function handleSubmit(
    e:
      | React.FormEvent<HTMLFormElement>
      | React.KeyboardEvent<HTMLTextAreaElement>,
  ) {
    sendButtonPressed(text);
    setText("");
    if (textbox.current) {
      textbox.current.style.height = ORIGINAL_HEIGHT;
    }
    e.preventDefault();
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="w-[100%] h-fit border-gray-300 border-[1px] rounded-xl bg-white"
    >
      <fieldset className="flex justify-between">
        <textarea
          ref={textbox}
          value={text}
          onChange={handleKeyDown}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              handleSubmit(e);
            }
          }}
          placeholder="Send message"
          className="resize-none px-4 max-h-[40vh] grow border-none rounded-xl focus:outline-none border-transparent focus:ring-0 overflow-x-hidden"
        />
        <button type="submit">
          <PaperPlaneIcon className="h-5 w-5 mx-2 hover:cursor-pointer" />
        </button>
      </fieldset>
    </form>
  );
};
