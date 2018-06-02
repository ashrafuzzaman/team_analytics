from django.db import models


class GithubUser(models.Model):
    name = models.CharField(max_length=100)
    handler = models.CharField(max_length=50)


class Repository(models.Model):
    name = models.CharField(max_length=100)


class PullRequest(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    author = models.ForeignKey(GithubUser,
                               related_name="authored_prs",
                               related_query_name="authored_pr",
                               on_delete=models.CASCADE)
    merger = models.ForeignKey(GithubUser,
                               related_name="merged_prs",
                               related_query_name="merged_pr",
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    merged_at = models.DateTimeField()
    lines_added = models.IntegerField()
    lines_removed = models.IntegerField()
