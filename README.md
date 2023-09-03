# import-alfred-snippets
Import snippets to Alfred 3 or 4 from `.csv` files in the current directory.

(Combine this with https://github.com/derickfay/te-to-alfredCSV to convert TextExpander 5 snippets to Alfred snippets)

Original script by [Derick Fay](https://github.com/derickfay/import-alfred-snippets/tree/master). This version has been modified to support processing multiple CSV files and organizing the outputs into folders.

Each CSV file should contain exactly three fields: the snippet name, the abbreviation, and the snippet text itself. For example:

```bash
"any","Pan","PropTypes.any"
"array","Parr","PropTypes.array"
...
"string","Pst","PropTypes.string"
```

## Usage

1. Save the file **importSnippets.py** to a location of your choice.
2. Place all your `.csv` files with the snippet details in the same directory where you saved the script.
3. To run the script, open a Terminal window in the same directory where you saved the script, then at the prompt, type:

    ```bash
    python ./importSnippets.py
    ```

4. If all goes well, for each CSV file, a new folder with the same name (minus the `.csv` extension) will be created. Inside each folder, there will be individual JSON files with names like *any [8760badff15c594b6308564f4460e7].json*, where the text in brackets is a random string generated as the uid (used by Alfred to track usage).

5. Move the newly generated folders (with the JSON files inside) to .../Alfred.alfredpreferences/snippets/ where each folder represents a group where you want the snippets. Creating a new folder will create a new group in Alfred. After a few seconds, the new snippets will appear in Alfred's preferences. (To view this folder in Finder, you'll need to find your Alfred.alfredpreferences file, right-click and click "Show Package Contents").

6. You can then delete or replace the `.csv` files and start again if needed.

Occasionally there may be errors where the csv library used by the script detects line breaks midway through a field. One solution is to open the problematic `.csv` file in Excel and then save it as a new `.csv`.

**DISCLAIMERS**: This script is largely untested and doesn't escape any special characters at the moment. From current observations, it seems to cause no problems for Alfred, but you should use it at your own risk.

Released under MIT License.
