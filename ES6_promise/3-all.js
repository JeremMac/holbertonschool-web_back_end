#!/usr/bin/node

import {uploadPhoto, createUser} from './utils.js';

export default function handleProfileSignup() {
    const MyPromise = Promise.all([uploadPhoto(), createUser()]);
    MyPromise
    .then(value => {
        console.log(`${value[0].body} ${value[1].firstName} ${value[1].lastName}`);
    })
    .catch(() => {
        console.error('Signup system offline');
    });
}
