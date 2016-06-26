let rand2() =
    let r = System.Random()
    r.Next(0, 2)

let rec rand3() =
    let f = rand2()
    let s = rand2() 
    match f, s with
    | 0, 0 -> 0
    | 0, 1 -> 1
    | 1, 0 -> 2
    | _, _ -> rand3()

printfn "rand3(): %d" (rand3())

let contains letters word =
    let wordLetters = Set.ofSeq word
    Set.isSubset letters wordLetters

let shortestWord lettersSeq fileName =
    let lines = System.IO.File.ReadLines fileName
    let letters = Set.ofSeq lettersSeq
    let words = lines |> Seq.filter (contains letters) |> Seq.toList
    let minLen = words |> List.minBy String.length |> String.length
    let shortest = words |> List.filter (fun w -> String.length w = minLen)
    shortest

printfn "shortestWord(): %A" (shortestWord "abcde" "../python/test_data/words.lst")
