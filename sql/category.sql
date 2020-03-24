-- 分类功能需要的sql
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8mb4 DEFAULT '' COMMENT '类别名字',
  `is_valid` tinyint(1) DEFAULT '1' COMMENT '是否有效 1是 0否',
  `home_image_url` varchar(100) DEFAULT '' COMMENT '主页图片地址',
  `description` varchar(200) CHARACTER SET utf8mb4 DEFAULT '' COMMENT '描述',
  `create_datetime` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_datetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
)

-- 新增category_id 字段
ALTER TABLE `gif`.`gif_info`
ADD COLUMN `category_id` int(11) NULL DEFAULT 0 COMMENT '分类id' AFTER `name`;
