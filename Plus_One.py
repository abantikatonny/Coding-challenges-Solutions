class Solution:
    def plusOne(self, digits):

        digits[len(digits)-1] = digits[len(digits)-1] + 1

        for i in range(len(digits)-1, 0, -1):

            # # print(i, digits[i])
            # if i == len(digits) - 1:
            #     # print(digits[i]+1, "last")
            #     digits[i] = digits[i]+1
            #     # print(digits)

            if int(digits[i] / 10) != 0:
                digits[i-1] = digits[i-1] + int(digits[i] /10)
                digits[i] = digits[i] % 10
                print(digits)

        if int(digits[0] /10) != 0:
            digits.insert(0, int(digits[0] / 10))
            digits[1] = digits[1] % 10



        return digits


if __name__ == "__main__":

    test_cases = [
        [0],
        [1, 2, 3 ],
        [3, 4, 6],
        [0, 0, 0],
        [9, 9, 9],
        [4, 3, 2, 1]
    ]

    correct_answers = [
        [1],
        [1, 2, 4],
        [3, 4, 7],
        [0, 0, 1],
        [1, 0, 0, 0],
        [4,3,2,2]
    ]

    cls = Solution()  # Slution cls = new Slution();

    for case, correct_answer in zip(test_cases, correct_answers):
        print(case, correct_answer)

        answer = cls.plusOne(case)

        if answer == correct_answer:
            print('ok')
        else:
            print('Failed for', case, answer)