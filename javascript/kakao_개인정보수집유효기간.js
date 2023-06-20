function dateToNumber(date){
    const arr = date.split('.')
    const year = Number(arr[0])
    const month = Number(arr[1])
    const day = Number(arr[2])
    const result = day + month*30 + (year-2000)*12*30
    return result
}

function solution(today, terms, privacies) {
    // 날짜는 2000년도를 빼준값을 사용
    // n개의 개인정보가 있음 => privacies
    // privacies 에서 today를 뺀 값이 음수면 파기해야된다. terms에 정보가 있음
    // terms 객체를 만들어줌
    let info = {}
    for (term of terms){
        let data = term.split(' ')
        let type = data[0]
        let period = data[1]
        info[type] = period
    }
    let answer = []
    let i = 1
    for (privacy of privacies){
        let data = privacy.split(' ')
        let date = data[0]
        let type = data[1]
        
        // date + type 이 today 보다 작으면 파기
        let originalDate = dateToNumber(today)
        let privacyDate = dateToNumber(date)
        let expireDate = privacyDate + Number(info[type])*30
        if (expireDate <= originalDate){
            answer.push(i)
        }
        i++
    }
    
    return answer
}

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
const result = solution(today, terms, privacies)
console.log(result)

