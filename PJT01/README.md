<<<<<<< HEAD
# PJT01

## problem 1

1. 학습한 내용

- 클라이언트가 API를 통해서 서버에 필요한 데이터를 요청하고 출력한다. 그 과정에서 json형식으로 request()를 사용하여 api에 요청한다.
- 일부 클라이언트가 데이터에 대해 악의적인 의도를 가지고 접근할 수 있으므로, 이를 방지하기 위해 인증하는 것인 'api key'를 발급받는다. 
- 출력된 총 데이터 중 필요한 정보인 key만 출력했다.

## problem 2

1. 학습한 내용
- 출력된 총 데이터 중 필요한 정보를 출력했다. 좀 더 세밀하게 타겟팅하여 출력했다. 

## problem 3

1. 학습한 내용
- 출력된 총 데이터 중 필요한 정보들을 출력했고, 이 정보들로 새로운 딕셔너리를 만들었다.  

2. 어려웠던 부분
- 아직 딕셔너리에 익숙치 않아 딕셔너리를 새로 만들어내는 데 어려움을 겪었다. 


## problem 4

1. 학습한 내용
- 출력된 총 데이터 중 필요한 정보들을 출력했고, 이 정보들로 새로운 딕셔너리를 만들었다 

2. 어려웠던 부분
- 로직 : 문제대로 로직을 세우는 과정이 어려웠다. 옆사람의 도움을 받았다. 
- 코딩능력 : 새로 만든 딕셔너리 안에서 for문, if문 구워 삶는 게 아직 익숙치 않아서 어려웠다.

3. 새로 배운 것들 및 느낀 점 
- 지금까지 배운 바로는 문제푸는 과정에 대한 로직과 이를 구현할 수 있는 코딩능력, 두 가지 능력이 중요한 것 같다.
- 코딩능력은 꾸준히 문법을 배우고 익히다보면 늘어날 것이라고 생각한다.
- 하지만 로직은 재능적인 측면도 많은 것 같다.

- 나는 아직까지 둘 다 부족한 것 같다.
- 걱정이 앞서지만 코딩을 눈으로 보는 것 만이 아닌 직접 타자를 치면서 익히려고 노력할 것이다.
- 로직은 다양한 사람들의 로직을 들어보고 이해하고 분석해보려고 노력할 것이다. 이렇게 데이터를 쌓아서 하다보면 늘지않을까.. 


=======
# 01_pjt1



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://lab.ssafy.com/tmdwoghd/01_pjt1.git
git branch -M master
git push -uf origin master
```

## Integrate with your tools

- [ ] [Set up project integrations](https://lab.ssafy.com/tmdwoghd/01_pjt1/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
>>>>>>> f8c2e67f1c228e63f5ec7adbc3a49e07dd8fc582
