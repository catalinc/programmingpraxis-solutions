// Solution https://programmingpraxis.com/2016/07/01/clock-angles/

let angle hour min =
    let m = 6. * float(min)
    let h = 30. * (float(hour) + (float(min) / 60.))
    abs (h - m)

printfn "%A" (angle 2 0)
printfn "%A" (angle 6 0)
printfn "%A" (angle 3 45)
