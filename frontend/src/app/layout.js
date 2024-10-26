import localFont from "next/font/local";
import "./globals.css";
import { Navbar } from "../features/navbar/Narbar";
import { Toaster } from "@/components/ui/toaster"

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata = {
  title: "Jen",
  description: "Jen, your personal AI assistant",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased  overflow-x-hidden overflow-y-hidden w-[100vw] h-[100vh]`}
      >
        <Toaster />
        <div className="flex flex-row w-[100vw] h-[100vh]">
          <Navbar />
          {children}
        </div>
      </body>
    </html>
  );
}
