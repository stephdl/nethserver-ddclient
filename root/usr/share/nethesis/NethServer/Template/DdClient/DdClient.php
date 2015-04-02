<?php
/* @var $view \Nethgui\Renderer\Xhtml */

if ($view->getModule()->getIdentifier() == 'update') {
    $keyFlags = $view::STATE_DISABLED;
    $template = 'Update_DynDns_Header';
} else {
    $keyFlags = 0;
    $template = 'Create_DynDns_Header';
}

echo $view->header('hostname')->setAttribute('template', $T($template));

$login = $view->panel()
    ->setAttribute('title', $T('DynDns_Credentials_Title'))
        ->insert($view->textInput('hostname', $keyFlags))
        ->insert($view->textInput('Description'))
        ->insert($view->textInput('login'))
        ->insert($view->textInput('password'))
        ->insert($view->textInput('mx'))
;

$destination = $view->panel()
    ->setAttribute('title', $T('DynDns_Provider_Title'))
    ->insert($view->fieldsetSwitch('CustomService', 'enabled', $view::FIELDSETSWITCH_EXPANDABLE)
        ->setAttribute('label', $T('CustomService_label'))
        ->insert($view->textInput('DynServer'))
        ->insert($view->textInput('DynDns')))
    ->insert($view->fieldsetSwitch('CustomService', 'disabled', $view::FIELDSETSWITCH_EXPANDABLE)
        ->setAttribute('label', $T('KnownService_label'))
        ->insert($view->radioButton('DynDns', 'CHANGEIP'))
        ->insert($view->radioButton('DynDns', 'DNSDYNAMIC'))
        ->insert($view->radioButton('DynDns', 'DNSPARK'))
        ->insert($view->radioButton('DynDns', 'DSLREPORTS'))
        ->insert($view->radioButton('DynDns', 'DTDNS'))
        ->insert($view->radioButton('DynDns', 'DYNDNS1'))
        ->insert($view->radioButton('DynDns', 'DYNDNS2'))
        ->insert($view->radioButton('DynDns', 'DYNDNS3'))
        ->insert($view->radioButton('DynDns', 'DYNHOST'))
        ->insert($view->radioButton('DynDns', 'EASYDNS'))
        ->insert($view->radioButton('DynDns', 'EURODYNDNS'))
        ->insert($view->radioButton('DynDns', 'FREEDNS'))
        ->insert($view->radioButton('DynDns', 'HAMMER'))
        ->insert($view->radioButton('DynDns', 'LOOPIA'))
        ->insert($view->radioButton('DynDns', 'NAMECHEAP'))
        ->insert($view->radioButton('DynDns', 'NOIP'))
        ->insert($view->radioButton('DynDns', 'ZONEDIT'))
);

$tabs = $view->tabs()
->insert($login)
->insert($destination);
echo $tabs;
        
echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL | $view::BUTTON_HELP);
?>
