// Brute force solution to https://programmingpraxis.com/2016/06/28/curious-numbers/
// TODO: find a faster algorithm

open System

let scale x =
    let powersOfTen = Seq.unfold (fun p -> Some(p, p * 10I)) 1I
    powersOfTen |> Seq.skipWhile (fun p -> p < x) |> Seq.head

let isCurious x =
    let p = x * x
    let r = p % scale x
    r = x

let solve x =
    [1I .. x] |> Seq.filter isCurious |> Seq.sum;

printfn "%A" (solve 10I**3)
