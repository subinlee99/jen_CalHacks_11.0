import React from "react";
import MemoryBoard from "./MemoryComponents/MemoryBoard";

const Memories = ({ userMemories, setRefresh }) => {
  console.log(userMemories);

  // if length of memories is 0, return no memories
  if (userMemories.memories.length === 0) {
    return <div>No memories</div>;
  }

  return (
    <div className="p-4 mt-5">
      <h2 className="text-2xl font-bold text-gray-800">Memories</h2>
      <p className="text-base text-gray-600 mt-2">Here are your memories that Jen has remembered about you.</p>
      <div>
        <MemoryBoard memories={userMemories.memories} setRefresh={setRefresh} />
      </div>
    </div>
  );
};

export default Memories;
