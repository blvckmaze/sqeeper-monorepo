const validate = {
  email: (email: string): boolean =>
    /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g.test(email),
  string: (arg: any, length: number): boolean =>
    String(arg).replace(/\s/g, "").length >= length,
};

const validateInput = (
  email: string,
  password: string,
  user?: Array<Text>
): boolean => {
  let validationChecks: Array<boolean> = [];

  if (user) {
    user.forEach((value, index) => {
      value
        ? validationChecks.push(validate.string(value, 2))
        : validationChecks.push(false);
    });
  }

  email
    ? validationChecks.push(validate.email(email))
    : validationChecks.push(false);

  password
    ? validationChecks.push(validate.string(password, 6))
    : validationChecks.push(false);

  return validationChecks.every((check) => check) ? true : false;
};

export { validate, validateInput };
