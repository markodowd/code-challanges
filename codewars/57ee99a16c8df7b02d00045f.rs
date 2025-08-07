fn flatten_and_sort(arr: &[Vec<i32>]) -> Vec<i32> {
    let mut answer: Vec<i32> = arr.iter().flatten().cloned().collect();

    answer.sort();

    answer
}
