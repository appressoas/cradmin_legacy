angular.module('cradminLegacy', [
  'cradminLegacy.templates'
  'cradminLegacy.directives'
  'cradminLegacy.providers'
  'cradminLegacy.calendar.providers'
  'cradminLegacy.messages'
  'cradminLegacy.detectizr'
  'cradminLegacy.menu'
  'cradminLegacy.objecttable'
  'cradminLegacy.acemarkdown'
  'cradminLegacy.bulkfileupload'  # TODO: We have to fix this! Commented out because it crashes everything!
  'cradminLegacy.iosaddtohomescreen'
#  'cradminLegacy.wysihtml'
  'cradminLegacy.imagepreview'
  'cradminLegacy.collapse'
  'cradminLegacy.modal'
  'cradminLegacy.scrollfixed'
  'cradminLegacy.pagepreview'
  'cradminLegacy.forms.modelchoicefield'
  'cradminLegacy.forms.usethisbutton'
  'cradminLegacy.forms.datetimewidget'
  'cradminLegacy.forms.filewidget'
  'cradminLegacy.forms.setfieldvalue'
  'cradminLegacy.forms.select'
  'cradminLegacy.forms.clearabletextinput'
  'cradminLegacy.backgroundreplace_element.providers'
  'cradminLegacy.backgroundreplace_element.directives'
  'cradminLegacy.listfilter.directives'
  'cradminLegacy.multiselect2.services'
  'cradminLegacy.multiselect2.directives'
  'cradminLegacy.loadmorepager.services'
  'cradminLegacy.loadmorepager.directives'
])
