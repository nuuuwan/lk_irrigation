# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_06:32:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,091 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 06:32:44 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:20:32 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:11:50 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-07 06:08:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:08:26 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.088 |  |
| 2026-09-07 06:07:36 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-07 06:06:43 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.115 |  |
| 2026-09-07 06:06:21 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-07 06:05:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:05:15 | Thanamalwila (Kirindi Oya) | 0.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-07 06:04:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.407 |  |
| 2026-09-07 06:04:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-07 06:04:24 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:04:01 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-07 06:03:56 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:03:35 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:03:24 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:03:12 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.091 |  |
| 2026-09-07 06:03:01 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:53 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 06:02:53 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:51 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-09-07 06:02:35 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:30 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 06:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 06:02:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:08 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:05 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 06:01:59 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:01:54 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-09-07 06:01:49 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-07 06:01:34 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-09-07 06:01:33 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:01:28 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-07 06:00:51 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 06:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-07 06:02:05 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 06:11:50 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-07 06:04:01 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-07 06:01:49 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-07 06:04:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-07 06:05:15 | Thanamalwila (Kirindi Oya) | 0.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-07 06:06:21 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-07 06:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 06:02:30 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 06:02:53 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 06:01:59 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:01:28 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:04:24 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:00:51 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:08:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:03:01 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:20:32 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:32:44 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:53 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:03:56 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:05:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:35 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:04:14 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:03:24 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:08 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:03:35 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:01:51 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:01:33 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:02:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:07:36 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-07 06:01:54 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-09-07 06:02:51 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-09-07 06:01:34 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-09-07 05:06:28 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.015 |  |
| 2026-09-07 06:08:26 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.088 |  |
| 2026-09-07 06:03:12 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.091 |  |
| 2026-09-07 06:06:43 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.115 |  |
| 2026-09-07 06:04:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.407 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)