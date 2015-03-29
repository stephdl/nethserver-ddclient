<?php
namespace NethServer\Module;

/**
 * Implementation of dynamic dns with ddclient
 */
class DdClient extends \Nethgui\Controller\TabsController
{
    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Configuration', 50);
    }

    public function initialize()
    {
        parent::initialize();
        $this->loadChildrenDirectory();
    }

}
