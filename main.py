import bs4
import requests


def getArrInnertext(arr):
    resArr = []
    for each in arr:
        resArr.append(each.get_text())
    return resArr


class eachQuestionClass:
    def __init__(self, classifiction, question, options, answer):
        self.classifiction = classifiction
        self.question = question
        self.options = options
        self.answer = answer

    def myPrint(self):
        print(f"本题类型为：{self.classifiction}\n题目内容为：{self.question}")
        for each in self.options:
            print(each)
        print("正确答案为：" + str(self.answer))


def getRightAnwer(optionsArr, rightAnswer):  # 从答案选项中获取正确答案
    resArr = []
    for eachOption in optionsArr[0]:
        if len(rightAnswer) == 1:  # 说明是判断题或者是单选题
            if rightAnswer in eachOption:
                resArr.append({
                    "text": eachOption.replace("A. ", "").replace("B. ", "").replace("C. ", "").replace("D. ", ""),
                    "isRichText": False,
                    "isCorrect": True
                })
            else:
                resArr.append({
                    "text": eachOption.replace("A. ", "").replace("B. ", "").replace("C. ", "").replace("D. ", ""),
                    "isRichText": False,
                    "isCorrect": False
                })
        else:  # 说明是多选题
            for eachrightAnswer in rightAnswer:
                if eachrightAnswer + "." in eachOption:
                    resArr.append({
                        "text": eachOption.replace("A. ", "").replace("B. ", "").replace("C. ", "").replace("D. ", ""),
                        "isRichText": False,
                        "isCorrect": True
                    })
                    break
            else:
                resArr.append({
                    "text": eachOption.replace("A. ", "").replace("B. ", "").replace("C. ", "").replace("D. ", ""),
                    "isRichText": False,
                    "isCorrect": False
                })
    return resArr


def main():
    BigDict = {"单选题": [], "多选题": [], "填空题": [], "判断题": []}
    urlArr = [
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=18752466&answerId=50920327&enc=14553052672d554174f49e2def89f526",
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=18752466&answerId=50920327&enc=14553052672d554174f49e2def89f526",
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=19136639&answerId=51108389&enc=08095db79cab27d2997eb284d388a4e6",
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=19136619&answerId=51108391&enc=a7e8e336f98bc661ca03aeccd43a892a",
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=19136598&answerId=51108399&enc=a6c798ae75c75cf78ade263863ab975b",
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=19136586&answerId=51108402&enc=f357086203f862e95b2bb5090c509902",
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=19136568&answerId=51108404&enc=14653e3ba445bffe0ec597d2ed38cbff",
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=19136546&answerId=51107487&enc=cba4ebc72bd8d841d0e59ec5dcfa84fe",
        "https://mooc1.chaoxing.com/mooc2/work/view?courseId=95340662&classId=53881441&cpi=149873770&workId=18752583&answerId=51108406&enc=fed622b637ab18343411c24d7abb630e"]
    for burp0_url in urlArr:
        burp0_cookies = {"uname": "20081130", "lv": "1", "pid": "33406", "_uid": "149132515",
                         "uf": "b2d2c93beefa90dcde9d0d2db09fc568087b71d346bb59ddf88794e0450c26383bfc133ed7f50baef5bd38dbf4e1bf88913b662843f1f4ad6d92e371d7fdf64477aa791b0b255b77fd68be96b6183b1a1a4a210555d879cdae99523634df203cf0d43407f1df07c0",
                         "_d": "1652074324921", "UID": "149132515", "vc": "F9361E8CAD40812A61DABEEE9648196D",
                         "vc2": "9251B44061E76ACF9175B1A3C80D2CFF",
                         "vc3": "MbFUknwWibxiTOfRWk%2BL4pvevkYKtE4IrEFx9NKaumfrXC2LFKsgzBE15p3pttOgahBUzjSH4Ks03BNV%2FoheysHzXN1V%2Fx9NMVLtrwHFT0zKN9qh%2Fjx6MBaFhvQqwLSZWn%2FtlnrrhmirLBZ9IFc6JVkuTZV06f1zc4%2BN7I36QHU%3D2eea417bf6344fa8a69a01347ddd0da3",
                         "xxtenc": "64648e1a7fb85b762f6a92d7b7b2aea4",
                         "DSSTASH_LOG": "C_38-UN_592-US_149132515-T_1652074324924", "tl": "1", "_industry": "5",
                         "thirdRegist": "0", "k8s": "c21113753d8521fe2ad83c9bb1ffe44e0f6bd257",
                         "jrose": "42575126391F609B8C2AD331ADFC764C.mooc-1523198214-nj4sf",
                         "route": "ac9a7739314fa6817cbac7e56032374b"}
        burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0",
                         "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
                         "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"",
                         "Upgrade-Insecure-Requests": "1",
                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
                         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                         "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1",
                         "Sec-Fetch-Dest": "document", "Referer": "http://mooc2-ans.chaoxing.com/",
                         "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
        AllHTML = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies).text
        soup = bs4.BeautifulSoup(AllHTML, "lxml")
        BigBigDiv = soup.find_all("div", class_="mark_item")

        for BigDiv in BigBigDiv:
            eachSoup = BigDiv
            # print(eachSoup.find("h2"))
            # print(eachSoup.find_all("h2"))
            if "单选题" in str(eachSoup.find("h2")):
                for eachQuestion in eachSoup.find_all("div", "questionLi"):  # 每道题的循环
                    eachQuestionSoup = eachQuestion
                    text = eachQuestionSoup.find("h3", class_='mark_name').get_text().split('题)')[1]
                    optionsArr = getArrInnertext(eachQuestionSoup.find("ul", class_="mark_letter").find_all("li")),
                    rightAnswer = str(
                        eachQuestionSoup.find("div", class_="mark_answer").find("div", "mark_key").find_all("span")[
                            1]).split("</i>")[1].replace("</span>", "").replace(" ", '')
                    BigDict["单选题"].append(
                        eachQuestionClass("单选题", text, optionsArr[0], rightAnswer))
                    # createQuestion(text, getRightAnwer(optionsArr, rightAnswer), False)
                    BigDict["单选题"][-1].myPrint()
            elif "多选题" in str(eachSoup.find("h2")):
                for eachQuestion in eachSoup.find_all("div", "questionLi"):  # 每道题的循环
                    eachQuestionSoup = eachQuestion
                    text = eachQuestionSoup.find("h3", class_='mark_name').get_text().split('题)')[1]
                    optionsArr = getArrInnertext(eachQuestionSoup.find("ul", class_="mark_letter").find_all("li")),
                    rightAnswer = str(
                        eachQuestionSoup.find("div", class_="mark_answer").find("div", "mark_key").find_all("span")[
                            1]).split("</i>")[1].replace("</span>", "").replace(" ", '')
                    BigDict["多选题"].append(
                        eachQuestionClass("多选题", text, optionsArr[0], rightAnswer))
                    # createQuestion(text, getRightAnwer(optionsArr, rightAnswer), True)

                    BigDict["多选题"][-1].myPrint()
            elif "判断题" in str(eachSoup.find("h2")):
                for eachQuestion in eachSoup.find_all("div", "questionLi"):  # 每道题的循环
                    eachQuestionSoup = eachQuestion
                    text = eachQuestionSoup.find("h3", class_='mark_name').get_text().split('题)')[1]
                    optionsArr = getArrInnertext(eachQuestionSoup.find("ul", class_="mark_letter").find_all("li")),
                    rightAnswer = str(
                        eachQuestionSoup.find("div", class_="mark_answer").find("div", "mark_key").find_all("span")[
                            1]).split("</i>")[1].replace("</span>", "").replace(" ", '')
                    BigDict["判断题"].append(
                        eachQuestionClass("判断题", text, optionsArr[0], rightAnswer))
                    # 发送请求
                    # print(getRightAnwer(optionsArr, rightAnswer.replace("\r", "").replace("\t", "").replace("\n","")))
                    # createQuestion(text, getRightAnwer(optionsArr,
                    #                                    rightAnswer.replace("\r", "").replace("\t", "").replace("\n",
                    #                                                                                            "")),
                    #                False)
                    BigDict["判断题"][-1].myPrint()
    print("单选题数量：", len(BigDict["单选题"]))
    print("多选题数量：", len(BigDict["多选题"]))
    print("判断题数量：", len(BigDict["判断题"]))


# print(BigDiv)


def createQuestion(text, anserTextArr, isMultipleFlag):
    header = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJbmZvIjp7IlVJRCI6IiIsIkluZm9Db21wbGV0ZSI6ZmFsc2V9LCJleHAiOjE2NTI1OTUxMTl9.uAm0R2_29lL7a_M_FpCZCKINJJdE9da4klmmf7LaGTA"
    }
    sendData = {
        "setID": "2e47f134-7cf9-4292-bd9e-54f3d5e07b5a",
        "text": text,
        "isRichText": False,
        "isMultipleChoice": isMultipleFlag,
        "answers": anserTextArr
    }
    print(
        requests.post("http://localhost:8080/questionSet/question/add", headers=header, json=sendData).text)


if __name__ == '__main__':
    # createQuestion()
    main()
