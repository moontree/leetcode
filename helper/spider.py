# --*-- coding: utf-8 --*--
"""
运行程序之前，安装pyquery这个包
pip3 install pyquery
在python文件下新建一个目录，用于存放抓取的作文，并将prefix=后面的"contents"替换为对应的目录名
"""
from __future__ import print_function
from pyquery import PyQuery as pq
import urllib


class Spider:

    def __init__(self, url, target="a", prefix="contents"):
        self.idx = 0
        self.url = url
        self.target = target
        self.prefix = prefix
        self.titles = {}
        self.count = 0
        self.parsed = {}

    def parse_content(self, url):
        try:
            print("正在获取作文内容", url)
            filename = url.split("/")[-1][:-6]
            req = urllib.request.Request(url)
            res = urllib.request.urlopen(req)
            html = res.read().decode("gbk")
            d = pq(html)
            contents = d(".con_content p").items()
            title = d(".h_title").text()
            if "题目" in title:
                print("作文题目，返回")
                return
            if title in self.titles:
                print("内容重复")
                return
            self.titles[title] = True
            with open(self.prefix + "/" + filename + ".txt", "w") as f:
                f.write(title + "\n")
                for content in contents:
                    f.write(content.text() + "\n")
            print("完成")
        except Exception as e:
            print(e)

    def parse_article_list(self):
        list_url, ele = self.url, self.target
        print("正在处理作文列表页面", list_url)
        res = urllib.request.urlopen(list_url)
        html = res.read().decode("gbk")
        d = pq(html)
        for item in d(ele).items():
            url = item.attr("href")
            # if self.count == 10:
            #     return
            if url[-5:] == "shtml" and ("index" not in url) and (url not in self.parsed):
                    self.parse_content(url)
                    self.count += 1
                    self.parsed[url] = True

    # def parse_list_pages(self, url):
    #     print("正在获取作文列表链接", url)
    #     res = urllib.request.urlopen(url)
    #     html = res.read()
    #     pattern = re.compile(r"<a href=\"(.*?)\"")
    #     results = pattern.findall(str(html))
    #     next_pages = [url]
    #     for url in results:
    #         if url[-5:] == "shtml" and "index" in url:
    #             next_pages.append(url)
    #     print(next_pages)
    #     if "index" not in url:
    #         for page in next_pages:
    #             self.parse_article_list(page)

    def start(self):
        self.parse_article_list()
        print("一共有", self.count, "篇文章")


def generate_urls():
    nianji = ["gaoyi", "gaoer", "gaosan"]
    ticai = ["xieren", "xushi", "xiejing",
             "xiangxiang", "zhuangwu", "huatizuowen",
             "yilunwen", "yanjianggao", "duhougan",
             "riji", "shuomingwen", "xiaoshuo", "shuxin",
             "shuqingsanwen", "qizhongkaoshizuowen", "qimokaoshizuowen"]
    res = []
    for nj in nianji:
        for tc in ticai:
            res.append("http://www.zuowen.com/gaozhong/" + nj + "/" + tc + "/")
    print(res)


single_pages = [
    {
        "url": "http://www.zuowen.com/zhongkaozw/lnzkmf/",
        "feature": ".columnCon_r a"
    }, {
        "url": "http://www.zuowen.com/gaokaozw/lngkmf/",
        "feature": ".box1_1 a"
    }
]

pages = [
    "http://www.zuowen.com/gaokaozw/gkttzw/",
    'http://www.zuowen.com/gaozhong/gaoyi/xieren/',
    'http://www.zuowen.com/gaozhong/gaoyi/xushi/',
    'http://www.zuowen.com/gaozhong/gaoyi/xiejing/',
    'http://www.zuowen.com/gaozhong/gaoyi/xiangxiang/',
    'http://www.zuowen.com/gaozhong/gaoyi/zhuangwu/',
    'http://www.zuowen.com/gaozhong/gaoyi/huatizuowen/',
    'http://www.zuowen.com/gaozhong/gaoyi/yilunwen/',
    'http://www.zuowen.com/gaozhong/gaoyi/yanjianggao/',
    'http://www.zuowen.com/gaozhong/gaoyi/duhougan/',
    'http://www.zuowen.com/gaozhong/gaoyi/riji/',
    'http://www.zuowen.com/gaozhong/gaoyi/shuomingwen/',
    'http://www.zuowen.com/gaozhong/gaoyi/xiaoshuo/',
    'http://www.zuowen.com/gaozhong/gaoyi/shuxin/',
    'http://www.zuowen.com/gaozhong/gaoyi/shuqingsanwen/',
    'http://www.zuowen.com/gaozhong/gaoyi/qizhongkaoshizuowen/',
    'http://www.zuowen.com/gaozhong/gaoyi/qimokaoshizuowen/',
    'http://www.zuowen.com/gaozhong/gaoer/xieren/',
    'http://www.zuowen.com/gaozhong/gaoer/xushi/',
    'http://www.zuowen.com/gaozhong/gaoer/xiejing/',
    'http://www.zuowen.com/gaozhong/gaoer/xiangxiang/',
    'http://www.zuowen.com/gaozhong/gaoer/zhuangwu/',
    'http://www.zuowen.com/gaozhong/gaoer/huatizuowen/',
    'http://www.zuowen.com/gaozhong/gaoer/yilunwen/',
    'http://www.zuowen.com/gaozhong/gaoer/yanjianggao/',
    'http://www.zuowen.com/gaozhong/gaoer/duhougan/',
    'http://www.zuowen.com/gaozhong/gaoer/riji/',
    'http://www.zuowen.com/gaozhong/gaoer/shuomingwen/',
    'http://www.zuowen.com/gaozhong/gaoer/xiaoshuo/',
    'http://www.zuowen.com/gaozhong/gaoer/shuxin/',
    'http://www.zuowen.com/gaozhong/gaoer/shuqingsanwen/',
    'http://www.zuowen.com/gaozhong/gaoer/qizhongkaoshizuowen/',
    'http://www.zuowen.com/gaozhong/gaoer/qimokaoshizuowen/',
    'http://www.zuowen.com/gaozhong/gaosan/xieren/',
    'http://www.zuowen.com/gaozhong/gaosan/xushi/',
    'http://www.zuowen.com/gaozhong/gaosan/xiejing/',
    'http://www.zuowen.com/gaozhong/gaosan/xiangxiang/',
    'http://www.zuowen.com/gaozhong/gaosan/zhuangwu/',
    'http://www.zuowen.com/gaozhong/gaosan/huatizuowen/',
    'http://www.zuowen.com/gaozhong/gaosan/yilunwen/',
    'http://www.zuowen.com/gaozhong/gaosan/yanjianggao/',
    'http://www.zuowen.com/gaozhong/gaosan/duhougan/',
    'http://www.zuowen.com/gaozhong/gaosan/riji/',
    'http://www.zuowen.com/gaozhong/gaosan/shuomingwen/',
    'http://www.zuowen.com/gaozhong/gaosan/xiaoshuo/',
    'http://www.zuowen.com/gaozhong/gaosan/shuxin/',
    'http://www.zuowen.com/gaozhong/gaosan/shuqingsanwen/',
    'http://www.zuowen.com/gaozhong/gaosan/qizhongkaoshizuowen/',
    'http://www.zuowen.com/gaozhong/gaosan/qimokaoshizuowen/'
]


def parse_content(fp, base_url, start, end):
    try:
        print(fp)
        ff = open(fp, 'w')
        for i in range(start, end):
            url = base_url + str(i)
            print("正在获取检索内容", url)
            res = urllib.urlopen(url)
            html = res.read()
            d = pq(html)
            # contents = d(".hide-mobile").items()
            indexes = d(".hide-mobile th").text().split(' ')
            contents = list(d(".hide-mobile .col-md-5").items())
            c = len(indexes)
            print(fp, indexes)
            for i in range(c):
                setence = contents[i * 2].text() + contents[i * 2 + 1].text()
                ff.write("%s###%s\n" % (indexes[i], setence.encode("utf8")))
        ff.close()
    except Exception as e:
        print(e)


def parse_content_old(ff, url):
    try:
        print("正在获取检索内容", url)
        res = urllib.urlopen(url)
        html = res.read()
        time.sleep(2)

        d = pq(html)
        # contents = d(".hide-mobile").items()
        indexes = d(".hide-mobile th").text().split(' ')
        contents = list(d(".hide-mobile .col-md-5").items())
        c = len(indexes)
        if c == 0:
            exit(0)
        print(indexes)
        for i in range(c):
            print(indexes[i])
            setence = contents[i * 2].text() + contents[i * 2 + 1].text()
            ff.write("%s###%s\n" % (indexes[i], setence.encode("utf8")))
    except Exception as e:
        print(e)

import os
import xlwt
import time
import multiprocessing
if __name__ == "__main__":
    # zk_spider = Spider(single_pages[0]["url"], single_pages[0]["feature"], prefix="zk")  # 中考作文的保存路径
    # gk_spider = Spider(single_pages[1]["url"], single_pages[1]["feature"], prefix="gk")  # 高考作文的保存路径
    # zk_spider.start()
    # gk_spider.start()
    # valid = True
    # with open("还是.txt", "w") as of:
    #     with open("gkn/total-gkn.txt", "r") as f:
    #         while True:
    #             ss = f.readline()
    #             if valid:
    #                 of.write(ss)
    #                 # print(ss)
    #             if ss == "\r\n":
    #                 valid = True
    #             elif ss:
    #                 valid = False
    #             elif not ss:
    #                 break
    mm_map = {
        # '还是': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E8%BF%98%E6%98%AF?page=',
        #     'num': 77600,
        # },
        # '或': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E6%88%96?page=',
        #     'num': 98434,
        # },
        # '要么': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E8%A6%81%E4%B9%88?page=',
        #     'num': 2949,
        # },
        # '与其': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E4%B8%8E%E5%85%B6?page=',
        #     'num': 3560,
        # },
        # '抑或': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E6%8A%91%E6%88%96?page=',
        #     'num': 543,
        # },
        '亦或': {
            'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E4%BA%A6%E6%88%96?page=',
            'num': 43,
        },
        # '或者': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E6%88%96%E8%80%85?page=',
        #     'num': 32535,
        # },
        # '宁愿': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E5%AE%81%E6%84%BF?page=',
        #     'num': 2418,
        # },
        # '宁肯': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E5%AE%81%E8%82%AF?page=',
        #     'num': 368,
        # },
        # '宁可': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E5%AE%81%E5%8F%AF?page=',
        #     'num': 1776,
        # },
        # '或许': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E6%88%96%E8%AE%B8?page=',
        #     'num': 9726,
        # },
        # '与其': {
        #     'url': 'http://bcc.blcu.edu.cn/zh/search/0/%E4%B8%8E%E5%85%B6%2A%E4%B8%8D%E5%A6%82?page=',
        #     'num': 109,
        # },

    }
    for key in mm_map:
        base = 'yl/%s' % key
        base_url = mm_map[key]['url']
        c = mm_map[key]['num']
        cc = c / 100 + 1
        start, end = 0, cc
        fp = '%s.txt' % base
        parse_content(fp, base_url, start, end)
        # mp = multiprocessing.Process(target=parse_content, args=(fp, base_url, start, end))
        # time.sleep(1.1)
        # mp.start()
    # ff = open("yl/还是.txt", 'a')
    # for i in xrange(769, 777):
    #     parse_content_old(ff, 'http://bcc.blcu.edu.cn/zh/search/0/%E8%BF%98%E6%98%AF?page=' + str(i))
    #     # parse_content(ff, 'http://bcc.blcu.edu.cn/zh/search/0/%E4%B8%8D%E6%98%AF%2A%E5%B0%B1%E6%98%AF?page=' + str(i))
    # ff.close()