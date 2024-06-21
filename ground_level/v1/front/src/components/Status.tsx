import { useState } from "react";
import { Message } from "../types";
import { sendQuery } from "../services/service";

export default function Status() {
  
  
  return (
    <div className="status-container">
      <p>{status}</p>
    </div>
  );
}
