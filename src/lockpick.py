class LockPick:
    spreading = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1,
                 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07, 0]

    def hack(self, text):
        options = []
        for shift in range(94):
            result_text = ""
            for char in text:
                if char.isspace():
                    result_text += char
                else:
                    result_text += chr(33 + (ord(char) - 33 - shift) % 94)
            options.append(result_text)
        deviation = []
        for text in options:
            count = [0] * 27
            for char in text:
                if char.isupper():
                    count[ord(char) - ord('A')] += 1
                elif char.islower():
                    count[ord(char) - ord('a')] += 1
                else:
                    count[26] += 1
            total = sum(count)
            curr_deviation = 0
            for i in range(27):
                count[i] = (count[i] / total) * 100
                curr_deviation += abs(count[i] - self.spreading[i])
            deviation.append(curr_deviation)
        return options[deviation.index(min(deviation))]
