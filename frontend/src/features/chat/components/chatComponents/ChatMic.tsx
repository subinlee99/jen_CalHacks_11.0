"use client";

import React, { useState } from "react";
import { FaMicrophone } from "react-icons/fa6";

const ChatMic = ({
  onClick,
  connected,
  loadedVapi,
}: {
  onClick: () => void;
  connected: boolean;
  loadedVapi: boolean;
}) => {

    let text = loadedVapi ? "Press to talk" : "Loading Vapi...";

  return (
    <div className="flex flex-col items-center justify-center">
      <button onClick={onClick}>
        <div className="w-[94px] h-[94px] mb-2 border-2 border-gray-500 rounded-full flex items-center justify-center">
          <FaMicrophone className="size-[30px]" />
        </div>
      </button>
      {!connected ? <h2 className="text-gray-500 text-lg">{text}</h2> : <h2 className="text-gray-500 text-lg">Listening...</h2>}  
    </div>
  );
};

export default ChatMic;
