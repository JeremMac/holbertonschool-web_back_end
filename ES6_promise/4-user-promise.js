#!/usr/bin/node

export default function signUpUser(firstName, lastName) {
  const MyPromise = new Promise((resolve) => {
    resolve({ firstName, lastName });
  });
  return MyPromise;
}
