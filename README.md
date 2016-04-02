# test
这是一个将nginx日志插入到数据的脚本，仅用于测试，效率很低。

nginx log_format:
log_format  access '$remote_addr | $limit_rate | $content_length | $request_time | $remote_user | $time_iso8601 | $host | $request | $status | $body_bytes_sent | $http_referer | $http_user_agent | $http_x_forwarded_for';

sql:
CREATE TABLE `seo` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `remote_addr` varchar(100) NOT NULL DEFAULT '',
  `limit_rate` int(10) unsigned NOT NULL DEFAULT '0',
  `content_length` int(10) unsigned NOT NULL DEFAULT '0',
  `request_time` float(10,2) NOT NULL DEFAULT '0.00',
  `remote_user` varchar(100) NOT NULL DEFAULT '',
  `time_iso8601` varchar(100) NOT NULL DEFAULT '',
  `host` varchar(100) NOT NULL DEFAULT '',
  `request` varchar(2000) NOT NULL DEFAULT '',
  `status` int(10) unsigned NOT NULL DEFAULT '0',
  `body_bytes_sent` int(10) unsigned NOT NULL DEFAULT '0',
  `http_referer` varchar(2000) NOT NULL DEFAULT '',
  `http_user_agent` varchar(2000) NOT NULL DEFAULT '',
  `http_x_forwarded_for` varchar(2000) NOT NULL DEFAULT '',
  `method` varchar(100) NOT NULL,
  `protocol` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `request` (`request`(333)) USING BTREE,
  KEY `host` (`host`) USING BTREE,
  KEY `http_referer` (`http_referer`(333)) USING BTREE,
  KEY `http_user_agent` (`http_user_agent`(333)) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=11312659 DEFAULT CHARSET=utf8;

