export default function getListStudentIds(Myarray) {
  if (Array.isArray(Myarray)) {
    return Myarray.map((student) => student.id);
  }
  const emptyArray = [];
  return emptyArray;
}
