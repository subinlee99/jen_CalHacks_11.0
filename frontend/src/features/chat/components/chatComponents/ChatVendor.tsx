import React from "react";
import { v4 as uuidv4 } from "uuid";

import type { Vendor } from "../types/chat.schema";

export const ChatVendor = ({ vendor }: { vendor: Vendor }) => {
  return (
    <div className="mb-4">
      {vendor.Title && (
        <h2 className="text-2xl font-semibold mb-4">{vendor.Title}</h2>
      )}

      {vendor.Description && (
        <p className="mb-2">
          <span className="font-bold">Description: </span> {vendor.Description}
        </p>
      )}

      {vendor.GoogleReviews && (
        <p className="mb-2">
          <span className="font-bold">Google Reviews: </span>{" "}
          {vendor.GoogleReviews}
        </p>
      )}

      {vendor.Address && (
        <p className="mb-2">
          <span className="font-bold">Address: </span> {vendor.Address}
        </p>
      )}

      {vendor.ContactNumber && (
        <p className="mb-2">
          <span className="font-bold">Contact: </span> {vendor.ContactNumber}
        </p>
      )}

      {vendor.Email && (
        <p className="mb-2">
          <span className="font-bold">Email: </span>
          <a
            href={`mailto:${vendor.Email}`}
            className="text-blue-500 underline"
          >
            {vendor.Email}
          </a>
        </p>
      )}

      {vendor.Pricing && (
        <p className="mb-2">
          <span className="font-bold">Pricing: </span> {vendor.Pricing}
        </p>
      )}

      {vendor.Link && (
        <p className="mb-2">
          <a
            href={vendor.Link}
            target="_blank"
            rel="noopener noreferrer"
            className="text-lunaPink hover:underline"
          >
            Click Here to View The Vendor!
          </a>
        </p>
      )}

      {vendor.Image && (
        <div key={vendor.Image} className="relative m-4 h-64">
          <img
            src={vendor.Image}
            alt="Currently Unavailable"
            className="rounded-lg shadow-md h-full w-full object-contain"
          />
        </div>
      )}

      {/* commenting out these code because we are voiding the Jouvire4U service for MVP */}
      {/* <div className="flex flex-col h-fit items-center bg-gray-200 rounded-xl mx-2 px-2 md:flex-row">
        <p className="text-left min-w-[180px] text-lg font-semibold text-gray-900 px-2">
          Add {vendor.Title} to your vendor list here!
        </p>
        {added ? (
          <Button
            variant="primaryGrey"
            onClick={() => {
              ToastBuilder.success("Success")
                .withDesc("Successfully removed!")
                .send();
              setAdded(false);
            }}
            className="md:ml-auto mr-2 my-2  "
          >
            Remove
          </Button>
        ) : (
          <Button
            variant="primaryPink"
            onClick={() => {
              ToastBuilder.success("Success")
                .withDesc("Successfully added!")
                .send();
              setAdded(true);
            }}
            className="md:ml-auto mr-2 my-2  "
          >
            Add
          </Button>
        )}
      </div> */}
    </div>
  );
};

export const ChatVendors = ({ vendors }: { vendors: Vendor[] }) => {
  return (
    <div className="flex flex-col w-full my-2">
      <div className="flex flex-col space-y-6">
        {vendors.map((vendor) => (
          <ChatVendor key={uuidv4()} vendor={vendor} />
        ))}
      </div>
    </div>
  );
};
