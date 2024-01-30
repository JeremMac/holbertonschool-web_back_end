export default function updateUniqueItems(MyMap) {
  for (const [key, value] of MyMap) {
    if (value === 1) {
      MyMap.set(key, 100);
    }
  }
  return MyMap;
}
