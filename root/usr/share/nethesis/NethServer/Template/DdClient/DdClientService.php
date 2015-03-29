<?php

echo $view->header()->setAttribute('template', $T('DdClientService_Title'));

//echo $view->panel()
echo $view->fieldsetSwitch('status', 'enabled', $view::FIELDSETSWITCH_CHECKBOX)->setAttribute('uncheckedValue', 'disabled')
//    ->insert($view->checkbox('status', 'enabled')->setAttribute('uncheckedValue', 'disabled'))
    ->insert($view->checkbox('SSL', 'yes')->setAttribute('uncheckedValue', 'no'))

->insert($view->slider('DeamonUpdate', $view::SLIDER_ENUMERATIVE | $view::LABEL_ABOVE)
->setAttribute('label', $T('Deamon Update (${0})')))
->insert($view->selector('urlcheckip', $view::SELECTOR_DROPDOWN))
;

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_HELP);
?>

