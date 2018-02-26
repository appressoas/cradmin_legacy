angular.module('djangoCradmin.directives', [])

.directive 'djangoCradminBack', ->
  return {
    restrict: 'A'
    link: (scope, element, attrs) ->
      element.on 'click', ->
        history.back()
        scope.$apply()
      return
  }

.directive 'djangoCradminFormAction', ->
  return {
    restrict: 'A'
    scope: {
      'value': '=djangoCradminFormAction'
    }

    controller: ($scope) ->
      $scope.$watch 'value', (newValue) ->
        $scope.element.attr('action', newValue)
      return

    link: (scope, element, attrs) ->
      scope.element = element
      return
  }

.directive 'djangoCradminSelectTextForCopyOnFocus', ->
  ###
  Select text of an input field or textarea when the field
  receives focus.

  Example:
  ```
  <p>Copy the url below and share it on social media!</p>
  <input type="text" value="example.com" django-cradmin-select-text-for-copy-on-focus="http://example.com">
  ```
  ###
  return {
    restrict: 'A'
    scope: {
      valueToCopy: '@djangoCradminSelectTextForCopyOnFocus'
    }

    link: (scope, element, attrs) ->
      scope.value = attrs['value']
      element.on 'click', ->
        element.val(scope.valueToCopy)
        this.select()

      scope.resetValue = ->
        element.val(scope.value)
      element.on 'change', ->
        scope.resetValue()
      element.on 'blur', ->
        scope.resetValue()
      return
  }

.directive 'focusonme', ['$timeout', ($timeout) ->
  {
    restrict: 'A',
    link: ($scope, $element) ->
      $timeout () ->
        $element[0].focus()
        return
      return
  }
]