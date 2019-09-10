# 苏州大学网络自动登陆
## 环境配置
脚本需要Selenium自动化测试工具的配合,直接在浏览器中运行.
- [ ] FireFox浏览器/版本76的Chrome浏览器
- [ ] 最新的Selenium库

Selenium库安装(默认环境下安装):
```bash
pip install selenium
```
## 账户设置
在Login文件的main函数中使用苏大的学号和密码, 并可以选择Firefox或者Chrome的浏览器.

## 前台运行
运行Python文件.
```python
python Login.py
```

## 后台运行
若需要静默运行,即ubuntu断网自动打开浏览器并连接上网络,可设置静默运行.
```python
nohup python Login.py
```
提示```nohup: 忽略输入并把输出追加到'nohup.out'```, 可忽略,直接关闭Terminal即可.