export default function cleanSet(inputSet, startString) {
    if (typeof startString !== 'string' || startString === '') {
        return '';
    }
    let arr = []
        inputSet.forEach(element => {
            if (element.startsWith(startString)) {
                let result = element.substring(startString.length);
                arr.push(result); 
            }
        });
        return arr.join('-');
}
