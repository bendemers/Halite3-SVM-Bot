#!/usr/bin/env python3

import model

m = model.HaliteModel()
m.train_on_files('training', 'aggressive')
m.save(file_name='greedy.svc')
