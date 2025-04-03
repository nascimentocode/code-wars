const divisors = (integer) => {
    const result = []
    for (i = 2; i < integer; i++) {
        if (integer % i == 0) {
            result.push(i)
        }
    }
    if (!result.length) {
        return `${integer} is prime`
    }

    return result
}