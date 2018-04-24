//: Playground - noun: a place where people can play

import UIKit
func countZerosAtIndex(in str: String)-> [Int:Int]{
    var zerosDict = [Int:Int]()
    var indexOfOne = 0
    let arr = Array(str)
    var count = 0
    for charIndex in 0..<arr.count{
        if arr[charIndex] == "1"{
            indexOfOne = charIndex
            count = 0
            continue
        }else{
            count += 1
            zerosDict[indexOfOne] = count
        }
    }
    return zerosDict
}

typealias tuple = (Int, Int)

func getMaxValueAndIndex(in dict: [Int: Int])-> tuple{
    var maxValue = 0
    var indexOfOneWithMaxZeros = 0
    for (key, value) in dict{
        if value > maxValue{
            maxValue = value
            indexOfOneWithMaxZeros = key
        }
    }
    return (indexOfOneWithMaxZeros, maxValue)
}

func insertOne(in str: String){
    let dict = countZerosAtIndex(in: str)
    let tuple = getMaxValueAndIndex(in: dict)
    var str = Array(str)
    if tuple.1 % 2 == 0 {
        str.insert("1", at: (tuple.1/2 + tuple.0))
    }else {
        str.insert("1", at: 1 + (tuple.1/2 + tuple.0))
    }
    print(String(str))
}

insertOne(in: "01010111000")
print(getMaxValueAndIndex(in:countZerosAtIndex(in: "000010010001010000100000")))
