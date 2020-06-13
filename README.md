# dirsearch-single
# 介绍
在平时会碰到一个目标的多个资产都是使用的同一个CMS，当发现了一个站点的漏洞时，可能其他站点也存在此漏洞，此时就可以对这些URL进行单个目录的批量检测了。

# 安装
```
pip3 install requests
```
# 使用
1、在`url.txt`文件中，加上自己想要检测的url
2、使用`python3`运行以下命令，最后的`dir_path`改成你想检测的目录
```
python3 disearch_single.py dir_path
```
# 注意事项
* `url.txt`中的格式为`https://www.teamssix.com`或`http://www.teamssix.com`
* 此程序使用`Python3`开发

![](https://teamssix.oss-cn-hangzhou.aliyuncs.com/TeamsSix_Subscription_Logo2.png)
