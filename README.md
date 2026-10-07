# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_11:08:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,309 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 11:08:58 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-07 11:08:38 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-07 11:08:21 | Panadugama (Nilwala Ganga) | 5.39 | 🟡 Alert | -0.117 |  |
| 2026-10-07 11:07:18 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.178 |  |
| 2026-10-07 11:06:38 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.062 |  |
| 2026-10-07 11:05:48 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.131 |  |
| 2026-10-07 11:05:37 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 11:04:42 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 11:04:34 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.158 |  |
| 2026-10-07 11:04:21 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 11:04:09 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:04:08 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-07 11:04:05 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-10-07 11:03:58 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-10-07 11:03:53 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-10-07 11:03:46 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:03:45 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | -0.023 |  |
| 2026-10-07 11:03:43 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-10-07 11:03:38 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-07 11:03:35 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:03:13 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.149 |  |
| 2026-10-07 11:02:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:02:47 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:02:23 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.031 |  |
| 2026-10-07 11:02:12 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-10-07 11:02:07 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:02:00 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-10-07 11:01:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:01:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:01:30 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:01:24 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:00:51 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-07 11:00:46 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:00:40 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 11:08:21 | Panadugama (Nilwala Ganga) | 5.39 | 🟡 Alert | -0.117 |  |
| 2026-10-07 11:04:08 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-07 11:08:38 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-07 11:04:21 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 11:00:51 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-07 11:04:42 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 11:05:37 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 11:03:46 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:02:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:06:20 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:01:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:00:46 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:02:07 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:04:09 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:03:35 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:01:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:02:47 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:01:30 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:01:24 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 11:03:38 | Siyambalanduwa (Heda Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-07 11:03:43 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-10-07 10:07:16 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-10-07 11:04:05 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-10-07 11:03:53 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-10-07 11:03:58 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-10-07 11:08:58 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-07 11:02:00 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-10-07 11:03:45 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | -0.023 |  |
| 2026-10-07 10:05:56 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-07 11:02:12 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-10-07 11:02:23 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.031 |  |
| 2026-10-07 11:00:40 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.040 |  |
| 2026-10-07 11:06:38 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.062 |  |
| 2026-10-07 10:07:49 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.072 |  |
| 2026-10-07 10:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.118 |  |
| 2026-10-07 11:05:48 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.131 |  |
| 2026-10-07 11:03:13 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.149 |  |
| 2026-10-07 11:04:34 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.158 |  |
| 2026-10-07 11:07:18 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)