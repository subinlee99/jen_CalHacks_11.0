import React, { useLayoutEffect, useRef, useState } from "react";

import { PaperPlaneIcon } from "@radix-ui/react-icons";

export interface ChatInputProps {
  sendButtonPressed: (text: string) => void;
  isDisabled: boolean;
}

export const Input = ({ sendButtonPressed, isDisabled }: ChatInputProps) => {
  const textbox = useRef<HTMLTextAreaElement>(null);
  const [text, setText] = useState("");

  // Text Area heights
  const ONE_LINE_HEIGHT: string = "24px";
  const ORIGINAL_HEIGHT: string = "40px";

  // Adds an extra line for the text area when the user types
  function adjustHeight() {
    // if (textbox.current) {
    //   textbox.current.style.height = ONE_LINE_HEIGHT;
    //   textbox.current.style.height = `${textbox.current.scrollHeight}px`;
    // }
  }

  useLayoutEffect(adjustHeight, []);

  function handleKeyDown(event: React.ChangeEvent<HTMLTextAreaElement>) {
    setText(event.target.value);
    adjustHeight();
  }

  const handleSubmit = (
    e:
      | React.FormEvent<HTMLFormElement>
      | React.KeyboardEvent<HTMLTextAreaElement>,
  ) => {
    sendButtonPressed(text);
    setText("");
    if (textbox.current) {
      textbox.current.style.height = ORIGINAL_HEIGHT;
    }
    e.preventDefault();
  };

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
          className="resize-none pt-2 px-4 h-[40px] grow border-none rounded-xl focus:outline-none border-transparent focus:ring-0 overflow-x-hidden"
          disabled={isDisabled} // Disable textarea when isDisabled is true
        />
        <button type="submit" disabled={isDisabled}>
          {" "}
          {/* Disable button when isDisabled is true */}
          <PaperPlaneIcon
            type="submit"
            className="h-5 w-5 mx-2 hover:cursor-pointer"
          />
        </button>
      </fieldset>
    </form>
  );
};
