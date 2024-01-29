export default function getStudentIdsSum(studentList) {
    const count = 0;
    return studentList.reduce((total, addId) => total + addId.id, count);
}
