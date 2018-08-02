# coding: utf-8
# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Company Wizard - Account Module (Test)',
    'version': '10.0.1.0.0',
    'category': 'Tools',
    'summary': "Glue module to create companies when Account module is"
    " installed",
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'company_wizard_account',
        'l10n_generic_coa',
    ],
    'installable': True,
}
