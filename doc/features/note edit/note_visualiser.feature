'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

Feature: Note visualiser

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

    Scenario: Initialise note visualiser
        Given the note edit/create screen is in the process of opening
        And this is an empty note
        When the note visualiser is initialised
        Then 1 column is added
        And a cursor is created
        And the cursor is placed on top of the column

        Given the note contains signbox(es)
        When the note visualiser is initialised
        Then columns are created 
        The columns are filled with the note signbox
        And a cursor is created
        And the cursor is placed on top of the first column (left)
    
    Scenario: Add an empty column
        Given the note edit/create screen is opened
        And there is space in the window for another column
        And there is no columns
        When a column is added
        Then a column is added on the left of the window, covering the full window height

        Given there is space in the window for another column
        And there column(s)
        When a column is added
        Then a column is added on the right of the existing column(s)

        Given there is not enough space in the window for another column
        When a column is added
        Then a column is added on the right of the existing column(s)
        And the window is moved to its rightmost

    Scenario: Remove an empty column
        Given the note edit/create screen is opened
        And the window cover all columns
        When the column is removed
        Then the column on the rightmost is removed

        Given the window don


    Scenario: Move window

    Scenario: Add a signbox
        Given the note edit/create screen is opened
        When a signbox is added to the note
        And there is space to add the signbox in current column
        Then the signbox is added at note cursor position
        And the curso
    
    Scenario: Remove a signbox
        Given 

    Scenario: Move note cursor with tap
        Given the note edit/create screen is opened
        When the user click on a signbox is the note visualiser
        Then the note cursor is moved below that signbox
    