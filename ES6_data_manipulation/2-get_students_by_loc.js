export default function getStudentsByLocation(studentList, city) {
    const MyArray = studentList.filter((key) => key.location === city);
    return MyArray;
}
