import axios from "axios";
import { z } from "zod";

const uploadSuccessSchema = z.object({
  message: z.string(),
});

export async function uploadFile(formData: FormData) {
  const result = await axios("/api/upload", {
    method: "POST",
    data: formData,
  });
  return uploadSuccessSchema.parse(result.data);
}
