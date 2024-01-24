#!/usr/bin/node

export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      resolve({ statut: 200, body: 'success' });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
