def groupAnagrams(strs)
  check = {}

  strs.each do |word|
    key = word.chars.sort.join
    if !check.key?(key)
      check[key] = []
    end
    check[key].append(word)
  end
  check.values
end

p groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])


def topKFrequent(nums, k)
  count = {}
  result = []

  #counter
  nums.each do |num|
    if count.key?(num) then
      count[num] += 1
    else
      count[num] = 1
    end
  end

  sorted = count.sort_by { |nums, freq| -freq}

  sorted.each do |num, freq|
    result.append(num)
  end
  result.first(k)

  
end

p topKFrequent([5,3,1,1,1,3,73,1],2)

