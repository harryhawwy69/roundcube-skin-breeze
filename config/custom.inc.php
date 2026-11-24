<?php
$config['language'] = 'ru_RU';
$config['skin'] = 'breeze';
$config['skins_allowed'] = ['breeze'];  // single skin: hides the skin picker in settings
$config['htmleditor'] = 1;              // rich editor always, as in Timeweb
$config['product_name'] = 'Почта';
// Timeweb folder names (the server also marks them with SPECIAL-USE); never create folders on a real mailbox
$config['create_default_folders'] = false;
$config['default_folders'] = ['INBOX', 'Sent', 'Drafts', 'Archive', 'Spam', 'Trash'];
$config['archive_mbox'] = 'Archive';
$config['junk_mbox'] = 'Spam';
$config['mail_pagesize'] = 100;
$config['message_sort_col'] = 'date';
$config['message_sort_order'] = 'DESC';
$config['message_show_email'] = true;
// machine-readable list dates: skins/breeze/breeze.js turns them into "11:22" / "22 ноября 10:21" and date groups
$config['prettydate'] = false;
$config['date_long'] = 'Y-m-d H:i';
// users can't switch "Красивые даты" back on: the skin needs the raw format and formats dates itself
$config['dont_override'] = ['prettydate', 'skin']; // skin: old user prefs may still name the former 'timeweb' skin
