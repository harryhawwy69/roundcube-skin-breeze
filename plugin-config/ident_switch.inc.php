<?php
// Overrides plugins/ident_switch/config.inc.php (Roundcube loads config/<plugin>.inc.php after it).
// Servers pre-filled for extra accounts (Settings > Identities > "Separate account").
$config['ident_switch.preconfig'] = [
    '*' => [
        'imap_host' => 'ssl://imap.timeweb.ru:993',
        'smtp_host' => 'ssl://smtp.timeweb.ru:465',
        'user' => 'email',
    ],
];
$config['ident_switch.hide_notifier_warning'] = true;
