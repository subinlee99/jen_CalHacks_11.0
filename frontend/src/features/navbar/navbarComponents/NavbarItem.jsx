/* eslint-disable @typescript-eslint/no-shadow */
// ^ Weird bug where eslint is not recognizing the prop types
import Link from "next/link";
import React from "react";

import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
// import TreeLine from "@/components/icons/TreeLine";



function determineClass(
  currentPageStates,
  currDropdownItem,
) {
  let currClass =
    " group flex gap-x-3 rounded-md p-2 text-sm leading-6 justify-start ";
  if (currentPageStates[currDropdownItem.href]) {
    currClass += "bg-primary-foreground text-black underline";
  } else if (
    currDropdownItem.childNav?.some((child) => currentPageStates[child.href])
  ) {
    currClass += " bg-primary-foreground text-black";
  } else {
    currClass += " text-gray-400 hover:bg-primary-foreground";
  }
  return currClass;
}

function determineAccordionClass(
  currentPageStates,
  currDropdownItem,
) {
  let currClass = "w-full ";
  if (currentPageStates[currDropdownItem.href]) {
    currClass += "bg-primary-foreground text-black";
  } else if (
    currDropdownItem.childNav?.some((child) => currentPageStates[child.href])
  ) {
    currClass += " bg-primary-foreground text-black";
  } else {
    currClass += "text-gray-400 hover:bg-primary-foreground";
  }
  return currClass;
}

const NavbarItem = ({
  dropdownItem,
  currentPageStates,
  setSidebarOpen,
}) => {
  return (
    <div>
      {dropdownItem.childNav !== null ? (
        // Navbar items that have child navbar items
        <Accordion
          type="single"
          collapsible
          className={determineAccordionClass(currentPageStates, dropdownItem)}
        >
          <AccordionItem style={{ border: "none" }} value="dropdownItem-1">
            <AccordionTrigger>
              <div className={determineClass(currentPageStates, dropdownItem)}>
                <dropdownItem.icon
                  className={`
                ${
                  currentPageStates[dropdownItem.href]
                    ? "text-black"
                    : "text-gray-400"
                }
                h-6 w-6 shrink-0 
              `}
                  aria-hidden="true"
                />
                {dropdownItem.name}
              </div>
            </AccordionTrigger>
          </AccordionItem>
        </Accordion>
      ) : (
        // Navbar items that doesnt have child navbar items
        <Link
          onClick={() => setSidebarOpen(false)}
          href={`/${dropdownItem.href}`}
          className={`${
            currentPageStates[dropdownItem.href]
              ? "bg-primary-foreground text-black"
              : "text-gray-400 hover:bg-primary-foreground"
          }
              group flex gap-x-3 rounded-md p-2 text-sm leading-6 justify-start
            `}
        >
          <dropdownItem.icon
            className={`
                ${
                  currentPageStates[dropdownItem.href]
                    ? "text-black"
                    : "text-gray-400"
                }
                h-6 w-6 shrink-0
              `}
            aria-hidden="true"
          />
          {dropdownItem.name}
        </Link>
      )}
    </div>
  );
};

export default NavbarItem;
