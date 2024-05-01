from src import constants


class LockPick:

    def hack(self, text):
        options = []
        for shift in range(94):
            result_text = ''
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
                curr_deviation += abs(count[i] - constants.SPREADING[i])
            deviation.append(curr_deviation)
        return options[deviation.index(min(deviation))]
