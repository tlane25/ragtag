import { useState } from "react";

export function ChatContainer() {
  const [messages, setMessages] = useState([]);
  return (
    <div className="chat-container">
      <form action="">
        <input type="text" />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
