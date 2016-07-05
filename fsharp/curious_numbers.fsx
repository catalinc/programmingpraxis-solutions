// Solution to https://programmingpraxis.com/2016/06/28/curious-numbers/

open System

let scale x =
    let powersOfTen = Seq.unfold (fun n -> Some(n, n * 10I)) 1I
    powersOfTen |> Seq.skipWhile (fun n -> n < x) |> Seq.head

let isCurious n =
    let p = n * n
    let r = p % scale n
    r = n

let getNextCurious c =
    let s = scale c
    let ns = Seq.unfold (fun n -> Some(n, n + 1I)) 1I
    ns |> Seq.map (fun n -> n * s + c) |> Seq.filter (fun n -> isCurious n) |> Seq.head

let curious c = Seq.unfold(fun n -> Some(n, getNextCurious n)) c

let sumCurious x n =
    curious x |> Seq.takeWhile (fun c -> c < n) |> Seq.sum 

let solve n =
    let r = [5I..6I] |> List.map (fun x -> sumCurious x n) |> List.sum
    r + 1I

printfn "sum: %A" (solve (10I**20))