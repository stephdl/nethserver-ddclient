<?php
namespace NethServer\Module\DdClient;

use Nethgui\System\PlatformInterface as Validate;

/**
 * Implement gui module for ddclient service status
 */

class DdClientService extends \Nethgui\Controller\AbstractController
{


    public function setDefaultValues($parameterName, $value)
    {
        $this->defaultValues[$parameterName] = $value;
        return $this;
    }

    public function initialize()
    {
    $this->declareParameter('DeamonUpdate', Validate::POSITIVE_INTEGER, array('configuration', 'ddclient', 'DeamonUpdate'));
    $this->declareParameter('SSL', $this->createValidator()->memberOf('yes','no'), array('configuration', 'ddclient', 'SSL'));
    $this->declareParameter('status', Validate::SERVICESTATUS, array('configuration', 'ddclient', 'status'));
    $this->declareParameter('urlcheckip', Validate::HOSTNAME, array('configuration', 'ddclient', 'urlcheckip'));

    $this->setDefaultValues('DeamonUpdate', '300');
    $this->setDefaultValues('SSL', 'yes');
    $this->setDefaultValues('status', 'enabled');
    $this->setDefaultValues('urlcheckip', 'checkip.dyndns.org');



        parent::initialize();
    }

    public function prepareView(\Nethgui\View\ViewInterface $view)
    {
        parent::prepareView($view);
        $view['DeamonUpdateDatasource'] = \Nethgui\Renderer\AbstractRenderer::hashToDatasource(array(
                '300' => $view->translate('${0} seconds', array(300)),
                '600' => $view->translate('${0} seconds', array(600)),
                '900' => $view->translate('${0} seconds', array(900)),
                '1800' => $view->translate('${0} seconds', array(1800)),
                '3600' => $view->translate('${0} seconds', array(3600)),
        ));

        $view['urlcheckipDatasource'] = \Nethgui\Renderer\AbstractRenderer::hashToDatasource(array(
                 'checkip.dyndns.org' => $view->translate('checkip.dyndns.org'),
                 'ipdetect.dnspark.com' => $view->translate('ipdetect.dnspark.com'),
                 'checkip.dyndns.org:8245' => $view->translate('checkip.dyndns.org:8245'),
                 'ip.changeip.com' => $view->translate('ip.changeip.com'),
       ));

}
    public function onParametersSaved($changes)
    {
        $this->getPlatform()->signalEvent('nethserver-ddclient-update@post-process');
    }


}
