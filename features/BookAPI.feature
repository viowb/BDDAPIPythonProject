# Created by viowb at 20/02/2026
#Feature: # Verify books are added and deleted using library API
  # Enter feature description here

  #Scenario: Verify AddBook API functionality
    #Given the Book details which needs to be added to library
    #When we execute the AddBook PostAPI method
   # Then Book is successfully added

  Scenario: Run behave without errors
    Given I have a clean environment
    When I run behave
    Then it should not crash