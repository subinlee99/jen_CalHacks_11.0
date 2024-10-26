"use client";

import { LogIn, LogOut, MessageSquare, Users } from "lucide-react";
import Link from "next/link";

import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import NavbarItem from "./NavbarItem";

// import { environmentConfig } from "@/environments/config";


const settings = [
  // Remove settings for now
  // { name: "Settings", href: "settings", icon: Settings },
];


export const navigation = [
  { name: "Memories", href: "memories", icon: Users, childNav: null },
  { name: "Chat", href: "chats", icon: MessageSquare, childNav: null },
];


const NavbarContent = ({ setSidebarOpen, currentPageStates }) => {
  const loggedIn = true;

  return (
    <div className="flex grow flex-col gap-y-3 overflow-y-auto border-r border-gray-200 bg-white px-5 min-h-screen">
      <div className="flex w-full items-center justify-start my-3">
        <Link href="/">
        </Link>
        <div>
          <h1 className="font-bold text-lg">Jen</h1>
          <p className="text-gray-400 font-extralight text-xs">
            Your personal assistant
          </p>
        </div>
      </div>
      <Separator />
      <nav className="flex flex-1 flex-col gap-y-4">
        <ul className="flex flex-col gap-y-2">
          <li>
            <p className="text-gray-400 font-medium text-xs -my-1">MAIN</p>
          </li>
          <li>
            <ul className="-mx-2 space-y-1">
              {navigation.map((item) => (
                <li key={item.name}>
                  <NavbarItem
                    setSidebarOpen={setSidebarOpen}
                    dropdownItem={item}
                    currentPageStates={currentPageStates}
                  />
                </li>
              ))}
            </ul>
          </li>
        </ul>
        <Separator />
        <ul className="flex flex-col gap-y-2">
          <li>
            <ul className="-mx-2 space-y-1">
              {settings.map((item) => (
                <li key={item.name}>
                  <Link
                    href={`/${item.href}`}
                    className={`${
                      currentPageStates[item.href]
                        ? "bg-primary-foreground text-black"
                        : "text-gray-400 hover:bg-primary-foreground"
                    }
                          group flex gap-x-3 rounded-md p-2 text-sm leading-6 justify-start
                        `}
                  >
                    <item.icon
                      className={`
                            ${
                              currentPageStates[item.href]
                                ? "text-black"
                                : "text-gray-400"
                            }
                            h-6 w-6 shrink-0
                          `}
                      aria-hidden="true"
                    />
                    {item.name}
                  </Link>
                </li>
              ))}
              <li className="text-primary">
                {loggedIn ? (
                  <Button
                    variant="raw"
                    className="group flex gap-x-3 rounded-md p-2 text-sm leading-6 justify-start w-full"
                  >
                    <LogOut
                      className={`h-6 w-6 shrink-0 text-[#6495ED]`}
                      aria-hidden="true"
                    />
                    Logout
                  </Button>
                ) : (
                  <Button
                    variant="raw"
                    className="group flex gap-x-3 rounded-md p-2 text-sm leading-6 justify-start w-full"
                  >
                    <LogIn className={`h-6 w-6 shrink-0 `} aria-hidden="true" />
                    Login
                  </Button>
                )}
              </li>
            </ul>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default NavbarContent;
