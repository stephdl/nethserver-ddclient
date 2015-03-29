<?php
namespace NethServer\Module\DdClient;

use Nethgui\System\PlatformInterface as Validate;

/**
 * Implement gui module for dynamic dns
 */

class DdClient extends \Nethgui\Controller\TableController
{

    public function initialize()
    {
        $columns = array(
            'Key',
            'Description',
            'DynDns',
            'Actions',
        );

        $parameterSchema = array(
            array('hostname', Validate::HOSTNAME_FQDN, \Nethgui\Controller\Table\Modify::KEY),
            array('Description', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD),
            array('DynDns', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD),
            array('login', Validate::NOTEMPTY, \Nethgui\Controller\Table\Modify::FIELD),
            array('password', Validate::NOTEMPTY, \Nethgui\Controller\Table\Modify::FIELD),
            array('mx', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD),
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('hosts', 'dyndns'))
            ->setColumns($columns)            
            ->addRowAction(new \Nethgui\Controller\Table\Modify('delete', $parameterSchema, 'Nethgui\Template\Table\Delete'))
            ->addRowAction(new \Nethgui\Controller\Table\Modify('update', $parameterSchema, 'NethServer\Template\DdClient\DdClient'))
            ->addTableAction(new \Nethgui\Controller\Table\Modify('create', $parameterSchema, 'NethServer\Template\DdClient\DdClient'))
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))
        ;

        parent::initialize();
    }



    public function onParametersSaved($changes)
    {
        $this->getPlatform()->signalEvent('nethserver-ddclient-update@post-process');
    }


}
