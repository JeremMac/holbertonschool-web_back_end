export default function hasValuesFromArray(MySet, MyArray) {
  return MyArray.every((element) => MySet.has(element));
}
