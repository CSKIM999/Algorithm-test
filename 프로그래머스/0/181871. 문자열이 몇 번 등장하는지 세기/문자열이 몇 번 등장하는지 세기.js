function solution(myString, pat) {
    var answer = 0;
    const patLength = pat.length
    for (let i = 0; i + patLength <= myString.length; i++) {
        if (myString.slice(i,i+patLength) === pat) answer++
    }
    
    return answer;
}