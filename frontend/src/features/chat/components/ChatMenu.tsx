import React from "react";

import "./styles/ChatMenuStyles.css";

interface ChatMenuProps {
  chatMode: "General" | "Jouvire4u";
  setChatMode: (mode: "General" | "Jouvire4u") => void;
  Jouvire4uClicked: () => void;
}

const ChatMenu = ({
  chatMode,
  setChatMode,
  Jouvire4uClicked,
}: ChatMenuProps) => {
  return (
    <div className="mb-4">
      <button
        type="button"
        className="p-4 text-2xl border-transparent"
        onClick={() =>
          setChatMode(chatMode === "General" ? "Jouvire4u" : "General")
        }
      >
        <span
          className={
            chatMode === "General"
              ? "text-lunaPink underline-custom"
              : "text-black"
          }
        >
          General
        </span>
      </button>
      <button
        type="button"
        className="p-4 text-2xl border-transparent"
        onClick={() => {
          setChatMode(chatMode === "General" ? "Jouvire4u" : "General");
          Jouvire4uClicked();
        }}
      >
        <span
          className={
            chatMode === "Jouvire4u"
              ? "text-lunaPink underline-custom"
              : "text-black"
          }
        >
          Jouvire4u
        </span>
      </button>
    </div>
  );
};

export default ChatMenu;
