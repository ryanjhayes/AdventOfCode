//elves
//calories

const input = puzzleInput.value;
const elfCalories = input
    .split('\n\n')
    .map(elf => {
        return elf
            .split('\n')
            .reduce((total, current) => total + Number(current.trim()), 0);
    })
    .sort((a, b) => b-a);

puzzleSolution.setValue(elfCalories[0]);