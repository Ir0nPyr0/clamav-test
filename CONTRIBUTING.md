# Contributing to the ES³ Sovereignty Maturity Level (SML) Framework

First, thank you for considering contributing to the ES³ Sovereignty Maturity Level (SML) Framework!  
It's people like you who make the open-source community such an amazing place to learn, inspire, and create.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](.github/CODE_OF_CONDUCT.md).   
By participating, you are expected to uphold this code.   
Please report unacceptable behavior to the project leaders via the contact details in our [README](README.md#contact).

## How Can I Contribute?

We use GitHub to manage reviews of pull requests.

* If you are a new contributor, see: [Steps to Contribute](#steps-to-contribute)

### Contributor vs. Maintainer
**Contributors:** Anyone submitting code, docs or ideas via Issues or Pull Requests.  
**Maintainers:** Core team members with permission to review, approve, and merge contributions. Maintainers help enforce standards and ensure quality.

### Steps to Contribute

Should you wish to work on an issue, please claim it first by commenting on the GitHub issue that you want to work on. This is to prevent duplicated efforts from other contributors on the same issue.  
If you have questions about one of the issues, please comment on them, and one of the maintainers will clarify.

### 1. Reporting Bugs

Before creating a bug report, please check the existing [Issues](https://github.com/es3-sml/es3-sml/issues) to see if the problem has already been reported.

When creating a bug report, please include as many details as possible:
* **Use a clear and descriptive title.**
* **Describe the exact steps which reproduce the problem.**
* **Provide your environment details** (OS, runtime/Go/Python/Node version, etc.).
* **Include logs or error outputs** where relevant.

### 2. Suggesting Enhancements

Enhancement suggestions are tracked as GitHub Issues.
* **Use a clear and descriptive title.**
* **Provide a step-by-step description of the suggested feature.**
* **Explain why this enhancement would be useful** to the broader community.

### 3. Submitting Pull Requests (PRs)

We welcome pull requests for bug fixes, new features, and documentation improvements.

1. **Fork the Repository:** Create your own fork of the project.
2. **Create a Branch:** Create a feature branch off of `main` (e.g., `feature/my-new-feature` or `fix/issue-123`).
3. **Make Your Changes:**
   * Adhere to the existing code style and conventions.
   * Add unit or integration tests for new functionality, if applicable.
   * Keep your commits logical, clean, and concise.
4. **Run Tests:** Ensure all existing and new tests pass locally before pushing.
5. **Open a Pull Request:**
   * Fill out the PR template/description clearly referencing any related issues (e.g., `Fixes #123`).
   * Be responsive to code reviews and feedback from maintainers.

## Developer Guidelines

### Developer Certificate of Origin (DCO) / Commit Signing

To ensure that all contributions can be legally distributed, `es3-sml` adheres to the [**Developer Certificate of Origin (DCO) 1.1**](https://developercertificate.org/) (used by the Linux Foundation and CNCF).

### How to Sign Off Your Commits

By adding a `Signed-off-by` line to your commit messages, you certify that you have the right to submit the code under the project's open-source license.

To automatically sign off your commit, use the `-s` or `--signoff` flag when running `git commit`:

```bash
git commit -s -m "feat: add feature for ES3 documentation"
```

This will automatically append a line like this to your commit message:

```bash
Signed-off-by: Jane Doe <jane.doe@example.com>
```

Note: The email address in the sign-off line must match your Git author email address (i.e., the email in your commit’s `Author:` field).

What if I forgot to sign off a commit?
You can rebase or amend your commits before opening a Pull Request:

For the last commit:

```bash
git commit --amend -s --no-edit
git push --force-with-lease
```

For multiple commits in your branch:

```bash
git rebase -i HEAD~N -x "git commit --amend -s --no-edit"
git push --force-with-lease
```
