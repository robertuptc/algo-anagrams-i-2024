exports.isCharacterMatch = function(string1, string2) {
    let sorted_arr_str1 = string1.toLowerCase().split('').sort()
    let sorted_arr_str2 = string2.toLowerCase().split('').sort()
    let answer  = true

    for (let i = 0; i < sorted_arr_str1.length; i++) {
        if (sorted_arr_str1[i] !== sorted_arr_str2[i]) {
            return answer = false
        }
    }
    return answer
};  

exports.anagramsFor = function(word, listOfWords) {
    let sorted_word_arr = word.toLowerCase().split('').sort()
    word = word.toLowerCase().split('').sort().join("")
    let answer = []
    
    for (let i = 0; i < listOfWords.length; i++) {
        let sorted_word = listOfWords[i].toLowerCase().split('').sort().join("")
        if (sorted_word == word) {
            answer.push(listOfWords[i])
        }
    }

    return answer
};

