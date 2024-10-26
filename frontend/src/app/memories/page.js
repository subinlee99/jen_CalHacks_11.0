"use client";

import React, { useState, useEffect } from "react";
import Memories from "@/features/memories/Memories";
import axios from "axios";
import { BeatLoader } from "react-spinners";

const page = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [refresh, setRefresh] = useState(false); // New state for refresh

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://0.0.0.0:8080/memory/all_memories?user_id=jenny"
        );
        setData(response.data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchData();
  }, [refresh]);

  return (
    <>
      {data && <Memories userMemories={data} setRefresh={setRefresh} />}
      {error && <div>{error}</div>}
      {!data && !error && <BeatLoader />}
    </>
  );
};

export default page;
