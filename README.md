# Python测试自动化实践

面向测试工程师的 Python 自动化实践项目。

## 项目介绍

本项目记录使用 Python 解决测试工作中常见问题的实践代码。

主要应用场景：

- 测试日志解析
- 测试数据处理
- 文件自动化处理
- Excel测试报告生成
- 异常处理
- 测试工具封装


## 技术栈

- Python 3
- csv
- openpyxl
- pandas
- pytest

## 项目结构
.
├── Error_log.txt
├── Experience_log.txt
├── README.md
├── def_check_voltage.py
├── dict_practice01.py
├── dict_practice02.py
├── list_practice.py
├── string_practice01.py
└── string_practice02.py
（更新中……有时候会忘记……）

## 实践内容

### 1. 测试日志解析

通过 Python 自动解析设备测试日志：

实现：

- 提取设备编号
- 获取测试结果
- 统计失败原因


示例：

输入：

SN002 TEST=POWER RESULT=FAIL ERROR=Voltage_High

输出：

测试结果：FAIL
失败原因：Voltage_High

## 项目目标

结合本人测试工作经验，
探索 Python 在软件测试和硬件测试场景中的应用，
提升测试效率，减少重复性工作。

# Python Test Automation Practice

Python automation practice for QA engineers.

## Introduction

This repository contains Python scripts developed for testing scenarios.

The goal is to improve testing efficiency through automation, including:

- Log parsing
- Test data processing
- File operations
- Test report generation
- Exception handling


## Skills

- Python
- CSV / Excel data processing
- Log analysis
- Test automation


## Practice Examples

### Log Parser

Parse device test logs and extract:

- Device ID
- Test result
- Error information

Example:

Input:
SN002 TEST=POWER RESULT=FAIL ERROR=Voltage_High

Output:
RESULT: FAIL
ERROR: Voltage_High

## Purpose

This project demonstrates how Python can be applied in software testing and hardware testing scenarios.