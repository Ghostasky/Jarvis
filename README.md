# Jarvis

`Jarvis`一个命令行的ChatGPT。

还有很多不足，更新中......

## 界面

![image-20230303145003940](./README/image-20230303145003940.png)

## 安装

使用pip直接安装whl即可

> 可能会出现权限相关的问题，管理员安装即可，待修正

## 使用

第一次运行时要求输入`API key`，会保存到`config.txt`文件中，该文件位于`User\[username]\Jarivs_log\`中


正常使用：输入，按两次回车发送。

## 程序参数

- 显示所有命令 : `/list`, `/?`, `/help`
- 显示所有角色 : `/listR`, `/cr`
- 改变角色: `/change_role`, `/cr`



## 待解决

- 各参数待更新
- 权限问题
- release

## Updating

- 日志问题。日志位于`User\[username]\Jarivs_log\`目录中，命名方式为：`2023-xx-xx.txt`
- `2023.4.22 - v0.4.0`: 添加部分参数：显示所有命令，显示所有角色，改变角色