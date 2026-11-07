# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_07:04:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,094 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 07:04:07 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.155 |  |
| 2026-11-07 07:03:53 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.070 |  |
| 2026-11-07 07:03:46 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.29 | 🟡 Alert | 0.000 |  |
| 2026-11-07 07:03:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-11-07 07:03:10 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:03:07 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-07 07:02:58 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.015 |  |
| 2026-11-07 07:02:56 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 07:02:53 | Giriulla (Maha Oya) | 3.41 | 🟢 Normal | -0.229 |  |
| 2026-11-07 07:02:43 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 07:02:41 | Ellagawa (Kalu Ganga) | 6.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 07:02:32 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-11-07 07:02:21 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-07 07:02:21 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-07 07:02:06 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.034 |  |
| 2026-11-07 07:02:05 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-11-07 07:01:48 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-11-07 07:01:40 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.051 |  |
| 2026-11-07 07:01:36 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.031 |  |
| 2026-11-07 07:01:20 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-07 07:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-07 07:01:03 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:00:39 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-11-07 06:33:22 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.003 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 07:02:56 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 07:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.29 | 🟡 Alert | 0.000 |  |
| 2026-11-07 07:01:48 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-11-07 06:02:21 | Badalgama (Maha Oya) | 4.28 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-07 07:03:07 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-07 06:06:55 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-07 07:02:43 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 07:02:41 | Ellagawa (Kalu Ganga) | 6.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 06:02:52 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:01:03 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:11:47 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:08:28 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:07:37 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:03:10 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 07:03:46 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-07 06:33:22 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.003 |  |
| 2026-11-07 07:01:20 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-07 07:02:21 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-07 07:02:05 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-11-07 07:02:58 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.015 |  |
| 2026-11-07 06:07:15 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-11-07 07:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-07 07:02:21 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-07 07:02:32 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-11-07 07:01:36 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.031 |  |
| 2026-11-07 06:02:28 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.031 |  |
| 2026-11-07 07:00:39 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-11-07 07:03:14 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-11-07 07:02:06 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.034 |  |
| 2026-11-07 07:01:40 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.051 |  |
| 2026-11-07 06:01:12 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2026-11-07 07:03:53 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.070 |  |
| 2026-11-07 06:07:03 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.095 |  |
| 2026-11-07 06:01:37 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.104 |  |
| 2026-11-07 07:04:07 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.155 |  |
| 2026-11-07 06:06:13 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.171 |  |
| 2026-11-07 07:02:53 | Giriulla (Maha Oya) | 3.41 | 🟢 Normal | -0.229 |  |
| 2026-11-07 06:00:39 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.288 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)