# Picture-Equivalence-Check

Super hacked script to check if 2 series of pictures are equivalent.

A friend needed to see if 2 long decks of powerpoint slides were the same, and if not, which slides differed.

Steps:
1. Export the slides as images, using the export function in Powerpoint
2. Save the images in 2 separate directories
3. Run script, indicating paths of the 2 directories when prompted
4. Prints index of mismatched pictures. (NB: Index starts from 0, not 1.)

Caveats: 
1. Matched pictures should have the same name, or at least have the same index within their respective directories
2. Matched pictures must be of the same size.
