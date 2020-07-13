#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

from django_cron import CronJobBase, Schedule

from thread_.models import Post


class ResetUpVotes(CronJobBase):

    RUN_EVERY_MINS = 86_400     # 24 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'thread_.reset_up_votes'

    def do(self):
         Post.objects.all().update(up_votes=0)