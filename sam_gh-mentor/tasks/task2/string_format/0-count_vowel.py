#!/usr/bin/python3
# A python program that counts vowels from a given strin

long_string = "The long-string instrument is a musical instrument in which the string is of such a length that the fundamental transverse wave is below what a person can hear as a tone (±20 Hz). If the tension and the length result in sounds with such a frequency, the tone becomes a beating frequency that ranges from a short reverb (approx 5–10 meters) to longer echo sounds (longer than 10 meters). Besides the beating frequency, the string also gives higher pitched natural overtones. Since the length is that long, this has an effect on the attack tone. The attack tone shoots through the string in a longitudinal wave and generates the typical science-fiction laser-gun sound as heard in Star Wars.[1] The sound is also similar to that occurring in upper electricity cables for trains."
vowel_lower_count = 0
vowel_upper_count = 0
sum_count = 0
for read in long_string:
    if read.lower() in "aeiou":
        vowel_lower_count += 1
    elif read.upper() in "AEIOU":
        vowel_upper_count += 1
    sum_count = vowel_lower_count + vowel_upper_count
print(sum_count)
