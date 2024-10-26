"use client";

import React, { useState } from "react";
import { MdOutlineEdit } from "react-icons/md";
import { MdDelete } from "react-icons/md";
import { TiTick } from "react-icons/ti";
import { RxCross1 } from "react-icons/rx";


import { useToast } from "@/hooks/use-toast";
import axios from "axios";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";

import { Button } from "@/components/ui/button";

const MemoryBox = ({ memory, setRefresh }) => {
  const { toast } = useToast();
  const memory_id = memory.id;
  const [isEdit, setIsEdit] = useState(false);
  const [currentMemory, setCurrentMemory] = useState(memory.memory);

  const deleteMemory = async () => {

    try {
      await axios.delete(
        `http://0.0.0.0:8080/memory/${memory_id}`
      );
      return { success: true };
    } catch (err) {
      return { success: false, error: err.message };
    }
  };

  const updateMemory = async () => {
    console.log("test")
    console.log(memory_id);
    try {
      await axios.put(
        `http://0.0.0.0:8080/memory/${memory_id}`,
        { updated_content: currentMemory } // Pass currentMemory as data
      );
      return { success: true };
    } catch (err) {
      return { success: false, error: err.message };
    }
  };

  const handleDelete = async () => {
    console.log("delete");
    const response = await deleteMemory();
    console.log(response);

    if (!response.success) {
      toast({
        title: "Memory deletion failed",
        description: response.error,
      });
      return;
    }

    toast({
      title: "Memory deleted",
      description: "Your memory has been deleted",
    });
    setRefresh(true);
  };

  const handleUpdate = async () => {
    console.log("update");
    console.log(currentMemory);
    const response = await updateMemory();
    console.log(response);
    if (!response.success) {
      toast({
        title: "Memory update failed",
        description: response.error,
      });
      return;
    }
    toast({
      title: "Memory updated",
      description: "Your memory has been updated",
    });
    setRefresh(true);
  };

  return (
    <div className="p-2 rounded-md bg-gray-100">
      <div className="flex flex-row justify-between">
        {isEdit ? (
          <div className="flex flex-row gap-1 items-center">
            <input
              type="text"
              value={currentMemory}
              className="text-sm rounded-lg p-1 px-2"
              onChange={(e) => setCurrentMemory(e.target.value)}
            />
            <TiTick
              onClick={() => {
                setIsEdit(false);
                handleUpdate();
              }}
              className="hover:scale-110 cursor-pointer transition-transform duration-200"
            />
            <RxCross1
              onClick={() => setIsEdit(false)}
              className="hover:scale-110 cursor-pointer transition-transform duration-200"
            />
          </div>
        ) : (
          <>
            <p className="text-sm">{memory.memory}</p>
            <div className="flex flex-row gap-1">
              <MdOutlineEdit
                onClick={() => setIsEdit(true)}
                className="hover:scale-110 cursor-pointer transition-transform duration-200"
              />
              <AlertDialog>
                <AlertDialogTrigger asChild>
                  <Button variant="ghost" className="size-[10px]">
                    <MdDelete className="over:scale-110 cursor-pointer transition-transform duration-200" />
                  </Button>
                </AlertDialogTrigger>
                <AlertDialogContent>
                  <AlertDialogHeader>
                    <AlertDialogTitle>
                      Are you absolutely sure?
                    </AlertDialogTitle>
                    <AlertDialogDescription>
                      This action cannot be undone. This will permanently delete
                      your memory.
                    </AlertDialogDescription>
                  </AlertDialogHeader>
                  <AlertDialogFooter>
                    <AlertDialogCancel>Cancel</AlertDialogCancel>
                    <AlertDialogAction onClick={handleDelete}>
                      Continue
                    </AlertDialogAction>
                  </AlertDialogFooter>
                </AlertDialogContent>
              </AlertDialog>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default MemoryBox;
