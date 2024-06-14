import re

"""
Trường hợp âm chính của âm tiết được ghi bằng một chữ cái, dấu thanh được đặt trên hoặc dưới chữ cái ghi âm chính của mỗi âm tiết, ví dụ: mái nhà, hoà nhạc, quý hoá, thuỷ thủ, mạnh khoẻ, trí tuệ,...

2. Trường hợp âm chính của âm tiết được ghi bằng hai chữ cái

a) Đối với các kí hiệu ia, ua, ưa, dấu thanh đặt trên hoặc dưới chữ cái thứ nhất, ví dụ: bìa, lụa, lửa,...

b) Đối với các kí hiệu iê, yê, uô, uơ, dấu thanh đặt trên hoặc dưới chữ cái thứ hai, ví dụ: biển, thuyền, nhuộm, được,...

Điều 9. Cách viết âm i sau phụ âm đầu trong các âm tiết không có âm đệm và âm cuối

1. Trường hợp âm i đứng ngay sau phụ âm đầu thì được viết bằng chữ i, ví dụ: hi vọng, kỉ niệm, lí luận, mĩ thuật, bác sĩ, tỉ lệ,...

2. Trường hợp âm tiết chứa âm i là tên riêng thì viết theo đúng tên riêng đó, ví dụ: bản Vy, Vi Văn Định, Nguyễn Vỹ, Thy Ngọc,..."""
import re

def place_tonal_mark(word):
    vowels = "aeiouyâăêôơư"
    tonal_vowels = "áàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
    vowel_combinations = ["oa", "oe", "uy"]

    def find_vowel_indices(word):
        return [i for i, char in enumerate(word) if char in vowels]

    def has_tonal_vowel(word):
        return any(char in tonal_vowels for char in word)

    def place_tone_on_vowel(word, vowel_index):
        # Remove existing tone marks
        word = re.sub(f"[{tonal_vowels}]", lambda m: vowels[tonal_vowels.index(m.group(0)) % len(vowels)], word)
        # Add the tonal mark
        vowel = word[vowel_index]
        if vowel in vowels:
            word = word[:vowel_index] + tonal_vowels[vowels.index(vowel)] + word[vowel_index + 1:]
        return word

    if has_tonal_vowel(word):
        return word

    vowel_indices = find_vowel_indices(word)

    if len(vowel_indices) == 0:
        return word  # No vowels to place the tonal mark on

    # Rule 1: One vowel in the syllable
    if len(vowel_indices) == 1:
        return place_tone_on_vowel(word, vowel_indices[0])

    # Rule 2: One tonal vowel (ă, â, ê, ơ, ư, etc.)
    for idx in vowel_indices:
        if word[idx] in "ăâêôơư":
            return place_tone_on_vowel(word, idx)

    # Rule 3: Two vowels and ending in consonant or consonant cluster
    if len(vowel_indices) == 2 and not word[-1] in vowels:
        return place_tone_on_vowel(word, vowel_indices[-1])

    # Rule 4: Ending with oa, oe, uy
    if any(word.endswith(comb) for comb in vowel_combinations):
        return place_tone_on_vowel(word, vowel_indices[-1])

    # Rule 5: Ending with two or three vowels, not oa, oe, uy
    if len(vowel_indices) >= 2 and not any(word.endswith(comb) for comb in vowel_combinations):
        return place_tone_on_vowel(word, vowel_indices[-2])

    return word

# Test cases
test_words = ["ủ", "ủ rũ", "ế ẩm", "tiến triển", "xoèn xoẹt", "kế hoạch", "bức họa", "lóe sáng", "bài vở", "đào hoa"]
result = [place_tonal_mark(word) for word in test_words]
print(result)
