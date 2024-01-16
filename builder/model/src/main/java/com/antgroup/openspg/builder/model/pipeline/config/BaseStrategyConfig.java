/*
 * Copyright 2023 OpenSPG Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied.
 */

package com.antgroup.openspg.builder.model.pipeline.config;

import com.antgroup.openspg.builder.model.pipeline.enums.StrategyTypeEnum;
import com.antgroup.openspg.server.common.model.base.BaseValObj;
import lombok.Getter;

@Getter
public abstract class BaseStrategyConfig extends BaseValObj {

  private final StrategyTypeEnum strategyType;

  public BaseStrategyConfig(StrategyTypeEnum strategyType) {
    this.strategyType = strategyType;
  }
}
