#!/usr/bin/node

export default function getResponseFromAPI() {
    const MyPromise = new Promise( (resolve, reject) => {
        resolve();
        reject();
    })
    return MyPromise;
}
