Integer toInt(String s) {
    return s == "X" ? 10 : s.toInteger()
}

Integer sumISBN(String isbn) {
    sum = 0
    isbn.eachWithIndex { s, i ->
        sum += toInt(s) * (isbn.length() - i)
    }
    return sum
}

Integer sumEAN(String isbn) {
    sum = 0
    isbn.eachWithIndex { s, i ->
        sum += (i % 2 == 0 ? 1 : 3) * toInt(s)
    }
    return sum    
}

boolean validISBN(isbn) {
    s = isbn.replaceAll("-", "")
    switch (s.length()) {
        case 10:
            return sumISBN(s) % 11 == 0
        case 13:
            return sumEAN(s) % 10 == 0
        default:
            return false
    }
}

if (args.length > 0) {
    args.each {
        println(it + " -> " + (validISBN(it) ? "valid" : "invalid"))
    }
} else {
    println("usage: groovy isbn.groovy ISBN1 ISBN2...")
}
