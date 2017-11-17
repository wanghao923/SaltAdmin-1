-- MySQL dump 10.13  Distrib 5.5.36-34.1, for Linux (x86_64)
--
-- Host: localhost    Database: saltadmin
-- ------------------------------------------------------
-- Server version	5.5.36-34.1-log

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(3) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` varchar(20) NOT NULL,
  `password` varchar(60) NOT NULL,
  `email` varchar(50) DEFAULT NULL COMMENT '用户E-mail地址',
  `phone` varchar(15) DEFAULT NULL COMMENT '手机号',
  `nickname` varchar(20) DEFAULT NULL COMMENT '昵称，用于友好显示在页面上',
  `gender` varchar(50) DEFAULT NULL COMMENT '用户gender',
  `dept` varchar(50) DEFAULT NULL COMMENT '用户dept',
  `role` varchar(20) DEFAULT NULL COMMENT '用户角色',
  `lang` varchar(20) DEFAULT NULL COMMENT '用户语言',
  `login_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '用户登陆时间',
  `login_ua` varchar(20) DEFAULT NULL COMMENT '用户登陆ua',
  `login_ip` varchar(20) DEFAULT NULL COMMENT '用户登陆ip',
  `login_location` varchar(20) DEFAULT NULL COMMENT '用户登陆location',
  `create_time` timestamp NOT NULL COMMENT '用户创建时间',
  `update_time` timestamp NOT NULL COMMENT '用户更新时间',
  `status` varchar(3) NOT NULL DEFAULT 'yes' COMMENT '用户状态：yes表示启用，no表示禁用',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `hosts`
--

DROP TABLE IF EXISTS `hosts`;
CREATE TABLE `hosts` (
  `id` int(5) NOT NULL AUTO_INCREMENT COMMENT '主机ID',
  `hostname` varchar(64) NOT NULL COMMENT '主机名',
  `master_id` int(10) NOT NULL COMMENT 'Host salt master ID',
  `minion_id` varchar(64) NOT NULL COMMENT 'Host salt minion ID',
  `ip` varchar(64) DEFAULT NULL COMMENT 'Host IP',
  `os` varchar(64) DEFAULT NULL COMMENT '操作系统',
  `vendor` varchar(64) DEFAULT NULL COMMENT '制造商',
  `model` varchar(64) DEFAULT NULL COMMENT '型号',
  `cpu` varchar(64) DEFAULT NULL COMMENT 'CPU',
  `hdd` varchar(64) DEFAULT NULL COMMENT '磁盘',
  `mem` varchar(64) DEFAULT NULL COMMENT '内存',
  `snum` varchar(64) DEFAULT NULL COMMENT '序列号',
  `tag` varchar(64) DEFAULT NULL COMMENT '标签',
  `host_desc` varchar(64) DEFAULT NULL COMMENT '主机描述',
  `host_group` varchar(64) DEFAULT NULL COMMENT '主机分组',
  `create_time` date NOT NULL COMMENT '上架日期',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `status` varchar(16) DEFAULT "online" COMMENT '主机状态',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  UNIQUE KEY `minion_id` (`minion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `hosts_group`
--

DROP TABLE IF EXISTS `hosts_group`;
CREATE TABLE `hosts_group` (
  `id` int(5) NOT NULL AUTO_INCREMENT COMMENT '主机ID',
  `group_name` varchar(64) NOT NULL COMMENT '主机组名',
  `host_count` int(5) NOT NULL DEFAULT 0 COMMENT '主机组包含的主机数量',
  `create_time` date NOT NULL COMMENT '主机组创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '主机组修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `group_name` (`group_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `salt_master`
--

DROP TABLE IF EXISTS `salt_master`;
CREATE TABLE `salt_master` (
  `id` int(5) NOT NULL AUTO_INCREMENT COMMENT 'salt master id',
  `hostname` varchar(64) NOT NULL COMMENT '主机名',
  `type` varchar(12) NOT NULL DEFAULT 'remote' COMMENT 'salt master工作方式',
  `api` varchar(64) NOT NULL COMMENT 'salt api',
  `username` varchar(64) NOT NULL COMMENT 'salt api用户名',
  `password` varchar(64) NOT NULL COMMENT 'salt api用户密码',
  `eauth` varchar(12) NOT NULL COMMENT 'salt api加密方式',
  `minion_count` int(10) NOT NULL DEFAULT 0 COMMENT 'salt minion数量',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'minion接入时间',
  `status` varchar(3) NOT NULL DEFAULT 'yes' COMMENT 'salt minion状态：1表示启用，0表示禁用',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `hostname` (`hostname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES (1,'admin','21232f297a57a5a743894a0e4a801fc3','超级管理员','88888888','admin@test.com','男','用户中心','role','lang','login_ua','10.206.0.229','ShangHai','2014-03-30 06:18:50','2014-03-30 06:18:50','2014-03-30 06:18:50','yes');
UNLOCK TABLES;
