import { RuntimeConfig } from "@nuxt/schema";

const generateRequestBody = (
  email: string,
  password: string,
  firstName?: string,
  lastName?: string
) => {
  let requestBody: object = {
    email: email,
    password: password,
  };

  if (firstName && lastName) {
    requestBody["first_name"] = firstName;
    requestBody["last_name"] = lastName;
  }

  return requestBody;
};

const generateRequestInfo = (
  endpoint: string,
  method: string,
  requestBody: object
) => {
  let requestInfo: object = {
    method: method,
    headers: { "Content-Type": "application/json" },
  };

  if (endpoint !== "/users/register") {
    requestInfo["credentials"] = "include";
  }

  if (requestBody) {
    requestInfo["body"] = JSON.stringify(requestBody);
  }

  return requestInfo;
};

export { generateRequestInfo, generateRequestBody };
