const getUserData = async (config = useRuntimeConfig()): Promise<Response> => {
  let userData: Response;

  await fetch(config.baseURL.concat("/users/profile/"), {
    headers: { "Content-Type": "application/json" },
    credentials: "include",
  }).then(async (response) =>
    response.ok
      ? (userData = await response.json())
      : new Error("Something went wrong")
  );

  return userData;
};

const delay = (time: number) =>
  new Promise((resolve) => setTimeout(resolve, time));

export { delay, getUserData };
