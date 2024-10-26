"use client";

import { usePathname } from "next/navigation";
import { Fragment, useEffect, useState } from "react";

import { Dialog, Transition } from "@headlessui/react";
import { Bars3Icon, XMarkIcon } from "@heroicons/react/24/outline";

// import NavbarContent, { navigation } from "./navbarComponents/NavbarContent";
import NavbarContent from "./navbarComponents/NavbarContent";
function Navbar() {
  const pathName = usePathname();
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [currentPageStates, setCurrentPageStates] = useState({});

  // Check which pages to display the side navbar
  useEffect(() => {
    const isCurrentPage = {};
    for (let i = 0; i < navigation.length; i += 1) {
      isCurrentPage[navigation[i].href] = false;
    }
    isCurrentPage[pathName.slice(1)] = true;
    setCurrentPageStates(isCurrentPage);
  }, [pathName]);


  return (
    <div>
      {/* ==========MOBILE NAV BAR============== */}
      <Transition.Root show={sidebarOpen} as={Fragment}>
        <Dialog
          as="div"
          className="relative z-50 lg:hidden"
          onClose={setSidebarOpen}
        >
          <Transition.Child
            as={Fragment}
            enter="transition-opacity ease-linear duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="transition-opacity ease-linear duration-300"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-gray-900/80" />
          </Transition.Child>

          <div className="fixed inset-0 flex">
            <Transition.Child
              as={Fragment}
              enter="transition ease-in-out duration-300 transform"
              enterFrom="-translate-x-full"
              enterTo="translate-x-0"
              leave="transition ease-in-out duration-300 transform"
              leaveFrom="translate-x-0"
              leaveTo="-translate-x-full"
            >
              <Dialog.Panel className="relative mr-16 flex w-full max-w-xs flex-1">
                <Transition.Child
                  as={Fragment}
                  enter="ease-in-out duration-300"
                  enterFrom="opacity-0"
                  enterTo="opacity-100"
                  leave="ease-in-out duration-300"
                  leaveFrom="opacity-100"
                  leaveTo="opacity-0"
                >
                  <div className="absolute left-full top-0 flex w-16 justify-center pt-5">
                    <button
                      type="button"
                      className="-m-2.5 p-2.5"
                      onClick={() => setSidebarOpen(false)}
                    >
                      <span className="sr-only">Close sidebar</span>
                      <XMarkIcon
                        className="h-6 w-6 text-white"
                        aria-hidden="true"
                      />
                    </button>
                  </div>
                </Transition.Child>
                {/* Sidebar component, swap this element with another sidebar if you like */}
                <NavbarContent
                  setSidebarOpen={setSidebarOpen}
                  currentPageStates={currentPageStates}
                />
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </Dialog>
      </Transition.Root>

      {/* ==========DESKTOP NAV BAR============== */}
      <div className="hidden h-full lg:z-50 lg:flex lg:w-56 lg:flex-col py-4">
        {/* Sidebar component, swap this element with another sidebar if you like */}
        <NavbarContent
          setSidebarOpen={setSidebarOpen}
          currentPageStates={currentPageStates}
        />
      </div>

      <div className="lg:hidden sticky top-0 z-40 flex items-center gap-x-6 bg-white p-4 shadow-sm sm:px-6">
        <button
          type="button"
          className="-m-2.5 p-2.5 text-gray-700 lg:hidden"
          onClick={() => setSidebarOpen(true)}
        >
          <span className="sr-only">Open sidebar</span>
          <Bars3Icon className="h-6 w-6" aria-hidden="true" />
        </button>
      </div>
      
    </div>
  );
}

export { Navbar };
