def sequenceAlignmentProblem(a, b, scoring_matrix):
    n = len(a)
    m = len(b)

    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    traceback_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diagonal = score_matrix[i - 1][j - 1] + scoring_matrix[a[i - 1]][b[j - 1]]
            left = score_matrix[i - 1][j] + scoring_matrix[a[i - 1]]['-']
            up = score_matrix[i][j - 1] + scoring_matrix['-'][b[j - 1]]

            # Choose the maximum score
            score_matrix[i][j] = max(diagonal, left, up)

            # Update the traceback matrix
            if score_matrix[i][j] == diagonal:
                traceback_matrix[i][j] = 1  # diagonal
            elif score_matrix[i][j] == left:
                traceback_matrix[i][j] = 2  # left
            else:
                traceback_matrix[i][j] = 3  # up

    # Traceback to reconstruct the alignment
    aligned_string1 = ""
    aligned_string2 = ""
    total_score = 0
    i, j = n, m
    while i > 0 or j > 0:
        if traceback_matrix[i][j] == 1:  # diagonal
            aligned_string1 = a[i - 1] + aligned_string1
            aligned_string2 = b[j - 1] + aligned_string2
            total_score += scoring_matrix[a[i - 1]][b[j - 1]]
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == 2:  # left
            aligned_string1 = a[i - 1] + aligned_string1
            aligned_string2 = '-' + aligned_string2
            total_score += scoring_matrix[a[i - 1]]['-']
            i -= 1
        else:  # up
            aligned_string1 = '-' + aligned_string1
            aligned_string2 = b[j - 1] + aligned_string2
            total_score += scoring_matrix['-'][b[j - 1]]
            j -= 1

    print("Total Score:", total_score)
    return aligned_string1, aligned_string2

# Example usage:
x = "TCCCAGTTATGTCAGGGACACGAGCATGCAGAGAC"
y = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"
scoring_matrix = {
    'A': {'A': 1, 'T': -0.2, 'G': -0.8, 'C': -2.3, '-': -0.6},
    'T': {'A': -0.2, 'T': 1, 'G': -1.1, 'C': -0.5, '-': -0.9},
    'G': {'A': -0.8, 'T': -1.1, 'G': 1, 'C': -0.7, '-': -1.5},
    'C': {'A': -2.3, 'T': -0.5, 'G': -0.7, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'T': -0.9, 'G': -1.5, 'C': -1, '-': 0},
}

aligned_string1, aligned_string2 = sequenceAlignmentProblem(x, y, scoring_matrix)
print("Aligned x:", aligned_string1)
print("Aligned y:", aligned_string2)
