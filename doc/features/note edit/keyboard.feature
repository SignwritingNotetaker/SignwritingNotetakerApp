'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

Feature: Keyboard writing

    Scenario: Open the note edit/create screen
        Given a user open the note edit/create screen
        When the screen open
        Then the keyboard is visible
        And the note visualiser is visible
        And the recommendation bar is visible
        And a current note object exist
        And a current signbox object is created empty
        And the current signbox object is visible at start of the recommendation bar
        And the note cursor is at the end of the current note
        But there is no signbox cursor

    Scenario: Create a new current signbox
        Given the note edit/create screen is opened
        When a new current signbox is created
        Then a current signbox object is created empty
        And the recommendation system is triggered


    Scenario: Move signbox cursor with arrow #later
    Scenario: Move signbox cursor with tap #later

    Scenario: Click on a sign key
        Given the note edit/create screen is opened
        When a user click on a sign key
        Then the sign is added to the current signbox
        And the recommendation system is triggered
        And the first recommendation after the current signbox is highlighted

    Scenario: Click on a punctuation key
        Given the note edit/create screen is opened
        And the current signbox is empty
        When the user click on a punctuation key
        Then the punctuation signbox is added to the note

        Given the current signbox contains sign(s)
        And a recommendation is highlighted
        When the user click on a punctuation key
        Then the highlighted recommendation is added to the note at note cursor position
        And the cursor move at the end of that signbox
        And the punctuation signbox is added to the note at note cursor position
        And a new signbox object is created

        Given the punctuation key being clicked on is the space key
        Then no punctuation signbox is added 

    Scenario: Click on the delete key
        Given the note edit/create screen is opened
        And the current signbox is empty
        When the user click on the deleted key
        Then the signbox before the note cursor is removed

        Given the current signbox contains sign(s)
        When the user click on the deleted key
        Then the last sign is removed
        And the recommendation system is triggered

    Scenario: Click on a recommendation (include current signbox)
        Given the note edit/create screen is opened
        And the current signbox is not empty
        When the user click on a recommendation signbox
        Then the recommendation signbox is added to the note at note cursor position
        And a new current signbox is created
