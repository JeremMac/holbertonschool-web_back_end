export default function updateUniqueItems(MyMap) {
  if (typeof MyMap !== 'object') {
    throw new Error('Cannot process');
  }
  for (const [key, value] of MyMap) {
    if (value === 1) {
      MyMap.set(key, 100);
    }
  }
  return MyMap;
}
