import React from "react";

const ChatStartupPage = () => {
  return (
    <div className="flex items-center justify-center text-center">
      <div className="w-5/6 pt-8 px-8">
        <h1 className="text-8xl font-bold mt-8 mb-4">
          <span className="text-lunaPink">Hello Jenny!</span>
        </h1>

        <h1 className="text-4xl mb-8 ">How can i help you today</h1>

        {/* <p className="text-xl mb-8"> */}
          {/* Ask me a */}
        {/* </p> */}

        {/* commenting out this code because we are voiding the Jouvire4U service for MVP */}
        {/* <div className="flex items-center my-8">
          <div className="grow border-t" style={{ borderColor: '#757575' }} />
          <span className="mx-4 text-gray-500">OR</span>
          <div className="grow border-t" style={{ borderColor: '#757575' }} />
        </div>

        <h1 className="text-xl font-bold text-lunaPink mb-4">
          Already have an idea in mind?
        </h1>

        <p className="text-lg mb-8">
          Start your personalised planning with
          <span>
            {' '}
            <button type="button" className="text-lunaPink font-bold underline">
              Jouvire4u
            </button>{' '}
          </span>
          and bring your idea and requirements to life!
        </p> */}
      </div>
    </div>
  );
};

export default ChatStartupPage;
