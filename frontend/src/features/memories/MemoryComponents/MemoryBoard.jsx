import React from "react";
import MemoryBox from "./MemoryBox";
const MemoryBoard = ({ memories, setRefresh }) => {
  // so basically if have a lot of memories and each memory has a category, and then we want sort each memory by the cateogires, we need to first determeine what all the cateories are by itereating through
  const categories = [
    ...new Set(memories.flatMap((memory) => memory.categories)),
  ];

  // Sort memories by categories
  const uniqueMemories = new Set();
  const sortedMemories = categories
    .map((category) => {
      const categoryMemories = memories.filter((memory) => {
        if (
          memory.categories.includes(category) &&
          !uniqueMemories.has(memory)
        ) {
          uniqueMemories.add(memory);
          return true;
        }
        return false;
      });
      return { category, memories: categoryMemories };
    })
    .filter((category) => category.memories.length > 0);

  const colors = ["#FFDDC1", "#FFABAB", "#FFC3A0", "#D5AAFF", "#85E3FF"]; // Add more colors as needed

  const formatCategory = (category) => {
    return category
      .split("_")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ");
  };

  return (
    <div className="flex flex-row gap-4">
      {sortedMemories.map((category, index) => (
        <div className="flex flex-col gap-2 p-4" key={index}>
          <h2
            className="text-xl font-bold text-gray-800 p-2 rounded-md"
            style={{ backgroundColor: colors[index % colors.length] }}
          >
            {formatCategory(category.category)}
          </h2>
          <div className="flex flex-col gap-2">
            {category.memories.map((memory, index) => (
              <MemoryBox memory={memory} key={index} setRefresh={setRefresh} />
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default MemoryBoard;
