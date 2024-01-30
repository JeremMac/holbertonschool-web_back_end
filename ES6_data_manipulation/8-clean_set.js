export default function cleanSet(inputSet, startString) {
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  const arr = [];
  inputSet.forEach((element) => {
    if (element.startsWith(startString)) {
      const result = element.substring(startString.length);
      arr.push(result);
    }
  });
  return arr.join('-');
}
