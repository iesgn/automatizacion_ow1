<?php
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, and ABSPATH. You can find more information by visiting
 * {@link https://codex.wordpress.org/Editing_wp-config.php Editing wp-config.php}
 * Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'user_wp');

/** MySQL database password */
define('DB_PASSWORD', 'asdasd');

/** MySQL hostname */
define('DB_HOST', {{servidor_mysql}});

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'c;u$9x8elk<^jbS}a+*_AQ1y;J!2W@|;{grIBd}jowYuF-tG6H$YjgDUw8_}moPf');
define('SECURE_AUTH_KEY',  '{BCHq8/}%S)X|./7`*R!#Cz/W^&=!KQ&3oB9bFrIZr|_FTEv5AD|,sd9~M~IE9dw');
define('LOGGED_IN_KEY',    'hl]q,CX&q~C-^>B,XL-3fgFG3Pnw$OVhf Syo/,[2vsI(%3/++6{IF!,oQP+0|Vz');
define('NONCE_KEY',        'hni|+1A_IT@HfU(+9=xZd6GQRwmqJ~>-d|P,ofQ3.]K<68!gP#n9}F}U9n4/IA&z');
define('AUTH_SALT',        'wt#T<t1jKIvj;i8TgFRs80+9#0)HRiHpzKW-zCF#V>|g-kNX1)#X`w*6s>F.rx](');
define('SECURE_AUTH_SALT', 'fNy+!%v8[p|fbN[%umD^B~tc-Ory@F&u/z6xV)Sn<} ,p|xIL<XWq}nDw3H{w!xP');
define('LOGGED_IN_SALT',   'voDk#o,ME@D0P<nd2k/jHVN#wt[OVB~wQR_-$.-JSIN?r>IrA!RY{0bjrLUZ#g>0');
define('NONCE_SALT',       '?H58Jtd?w??*w@/YRK!;2<Qm|saMGwk$-[!2=4 $qNDpl1S_s!TIws/}wTV~-QCw');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each a unique
 * prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');

