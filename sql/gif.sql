/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80013
Source Host           : localhost:3306
Source Database       : gif

Target Server Type    : MYSQL
Target Server Version : 80013
File Encoding         : 65001

Date: 2020-03-13 11:36:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin_user
-- ----------------------------
DROP TABLE IF EXISTS `admin_user`;
CREATE TABLE `admin_user` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '用户名',
  `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '密码',
  `status` varchar(4) DEFAULT NULL COMMENT '用户状态',
  `nick_name` varchar(32) DEFAULT NULL COMMENT '昵称',
  `create_time` datetime DEFAULT NULL,
  `create_user` varchar(32) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin_user
-- ----------------------------

-- ----------------------------
-- Table structure for gif_info
-- ----------------------------
DROP TABLE IF EXISTS `gif_info`;
CREATE TABLE `gif_info` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '名称',
  `template_dir` varchar(255) DEFAULT NULL COMMENT '模板文件夹位置',
  `home_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '主页地址',
  `video_url` varchar(255) DEFAULT NULL COMMENT '视频位置',
  `template_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '模板位置',
  `gif_template_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'gif动图模板url',
  `is_delete` int(4) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `create_user` varchar(32) DEFAULT NULL,
  `update_user` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`tid`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gif_info
-- ----------------------------
INSERT INTO `gif_info` VALUES ('1', 'dagong', null, 'static/template/dagong/example.png', 'static/template/dagong/template.mp4', 'static/template/dagong/template.tpl', null, '1', '2020-03-09 16:17:37', '2020-03-09 16:17:39', 'admin', 'admin');
INSERT INTO `gif_info` VALUES ('2', 'diandongche', null, 'static/template/diandongche/example.png', 'static/template/diandongche/template.mp4', 'static/template/diandongche/template.tpl', null, '2', '2020-03-09 16:17:57', '2020-03-09 16:17:59', 'admin', 'admin');
INSERT INTO `gif_info` VALUES ('3', 'jinkela', null, 'static/template/jinkela/example.png', 'static/template/jinkela/template.mp4', 'static/template/jinkela/template.tpl', null, '1', '2020-03-09 16:17:37', '2020-03-09 16:17:39', 'admin', 'admin');
INSERT INTO `gif_info` VALUES ('4', 'kongming', null, 'static/template/kongming/example.png', 'static/template/kongming/template.mp4', 'static/template/kongming/template.tpl', null, '1', '2020-03-09 16:17:57', '2020-03-09 16:17:59', 'admin', 'admin');
INSERT INTO `gif_info` VALUES ('5', 'marmot', null, 'static/template/marmot/example.png', 'static/template/marmot/template.mp4', 'static/template/marmot/template.tpl', null, '1', '2020-03-09 16:17:37', '2020-03-09 16:17:39', 'admin', 'admin');
INSERT INTO `gif_info` VALUES ('6', 'sorry', null, 'static/template/sorry/example.png', 'static/template/sorry/template.mp4', 'static/template/sorry/template.tpl', null, '1', '2020-03-09 16:17:57', '2020-03-09 16:17:59', 'admin', 'admin');
INSERT INTO `gif_info` VALUES ('7', 'wangjingze', null, 'static/template/wangjingze/example.png', 'static/template/wangjingze/template.mp4', 'static/template/wangjingze/template.tpl', null, '1', '2020-03-09 16:17:37', '2020-03-09 16:17:39', 'admin', 'admin');

-- ----------------------------
-- Table structure for gif_info_template
-- ----------------------------
DROP TABLE IF EXISTS `gif_info_template`;
CREATE TABLE `gif_info_template` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `gif_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'gif名称',
  `index` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '顺序',
  `template_text` varchar(255) DEFAULT NULL COMMENT '模板文字',
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gif_info_template
-- ----------------------------
INSERT INTO `gif_info_template` VALUES ('1', 'dagong', '1', '没有钱啊 肯定要做的啊');
INSERT INTO `gif_info_template` VALUES ('2', 'dagong', '2', '不做的话没有钱用');
INSERT INTO `gif_info_template` VALUES ('3', 'dagong', '3', '那你不会去打工啊');
INSERT INTO `gif_info_template` VALUES ('4', 'dagong', '4', '有手有脚的');
INSERT INTO `gif_info_template` VALUES ('5', 'dagong', '5', '打工是不可能打工的');
INSERT INTO `gif_info_template` VALUES ('6', 'dagong', '6', '这辈子不可能打工的');
INSERT INTO `gif_info_template` VALUES ('7', 'diandongche', '1', '戴帽子的首先进里边去');
INSERT INTO `gif_info_template` VALUES ('8', 'diandongche', '2', '开始拿剪刀出来 拿那个手机');
INSERT INTO `gif_info_template` VALUES ('9', 'diandongche', '3', '手机上有电筒 用手机照射');
INSERT INTO `gif_info_template` VALUES ('10', 'diandongche', '4', '寻找那个比较新的电动车');
INSERT INTO `gif_info_template` VALUES ('11', 'diandongche', '5', '六月六号 两名男子再次出现');
INSERT INTO `gif_info_template` VALUES ('12', 'diandongche', '6', '民警立即将两人抓获');
INSERT INTO `gif_info_template` VALUES ('13', 'jinkela', '1', '金坷垃好处都有啥');
INSERT INTO `gif_info_template` VALUES ('14', 'jinkela', '2', '谁说对了就给他');
INSERT INTO `gif_info_template` VALUES ('15', 'jinkela', '3', '肥料掺了金坷垃');
INSERT INTO `gif_info_template` VALUES ('16', 'jinkela', '4', '不流失 不蒸发 零浪费');
INSERT INTO `gif_info_template` VALUES ('17', 'jinkela', '5', '肥料掺了金坷垃');
INSERT INTO `gif_info_template` VALUES ('18', 'jinkela', '6', '能吸收两米下的氮磷钾');
INSERT INTO `gif_info_template` VALUES ('19', 'kongming', '1', '没想到');
INSERT INTO `gif_info_template` VALUES ('20', 'kongming', '2', '你竟说出如此粗鄙之语');
INSERT INTO `gif_info_template` VALUES ('21', 'marmot', '1', '金坷垃好处都有啥');
INSERT INTO `gif_info_template` VALUES ('22', 'marmot', '2', '谁说对了就给他');
INSERT INTO `gif_info_template` VALUES ('23', 'sorry', '1', '好啊');
INSERT INTO `gif_info_template` VALUES ('24', 'sorry', '2', '就算你是一流工程师');
INSERT INTO `gif_info_template` VALUES ('25', 'sorry', '3', '就算你出报告再完美');
INSERT INTO `gif_info_template` VALUES ('26', 'sorry', '4', '我叫你改报告你就要改');
INSERT INTO `gif_info_template` VALUES ('27', 'sorry', '5', '毕竟我是客户');
INSERT INTO `gif_info_template` VALUES ('28', 'sorry', '6', '客户了不起啊');
INSERT INTO `gif_info_template` VALUES ('29', 'sorry', '7', 'sorry 客户真的了不起');
INSERT INTO `gif_info_template` VALUES ('30', 'sorry', '8', '以后叫他天天改报告');
INSERT INTO `gif_info_template` VALUES ('31', 'sorry', '9', '天天改 天天改');
INSERT INTO `gif_info_template` VALUES ('32', 'wangjingze', '1', '我就是饿死');
INSERT INTO `gif_info_template` VALUES ('33', 'wangjingze', '2', '死外边 从这跳下去');
INSERT INTO `gif_info_template` VALUES ('34', 'wangjingze', '3', '也不会吃你们 一点东西');
INSERT INTO `gif_info_template` VALUES ('35', 'wangjingze', '4', '真香');

-- ----------------------------
-- Table structure for test
-- ----------------------------
DROP TABLE IF EXISTS `test`;
CREATE TABLE `test` (
  `tid` int(11) NOT NULL,
  `name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test
-- ----------------------------
INSERT INTO `test` VALUES ('1', 'test');
INSERT INTO `test` VALUES ('2', 'test2');
INSERT INTO `test` VALUES ('3', 'test3');
INSERT INTO `test` VALUES ('4', 'test4');
