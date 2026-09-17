# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_14:24:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 14:24:09 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:24:03 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-17 14:14:39 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 14:12:28 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 14:12:27 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 14:10:07 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:08:07 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:07:22 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-09-17 14:07:19 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-09-17 14:06:26 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.037 |  |
| 2026-09-17 14:06:19 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-09-17 14:05:49 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:05:16 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 14:05:11 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:04:54 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-17 14:04:48 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:04:41 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 14:04:23 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:04:12 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:03:53 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:03:38 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:03:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:02:49 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | 0.235 | 🔺 Rising |
| 2026-09-17 14:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.59 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-17 14:02:45 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 14:02:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:02:18 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 14:02:12 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:01:32 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:01:29 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:01:25 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:01:23 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:01:21 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:00:54 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:00:48 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:00:44 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 14:00:12 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 13:59:47 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 14:02:49 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | 0.235 | 🔺 Rising |
| 2026-09-17 14:02:45 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 14:07:22 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-09-17 14:02:18 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 14:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.59 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-17 14:04:54 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-17 14:00:44 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 14:00:12 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 14:14:39 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 14:24:03 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-17 14:05:16 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 14:12:28 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 14:04:41 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 14:12:27 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 14:01:29 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:03:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:10:07 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:02:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:03:38 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:04:48 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:04:23 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:05:11 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:00:48 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:03:53 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:08:07 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:00:54 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:01:21 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:24:09 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:05:49 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 14:01:23 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:02:12 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:01:25 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:04:12 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:01:32 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-17 14:07:19 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-09-17 13:59:47 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-09-17 14:06:26 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.037 |  |
| 2026-09-17 14:06:19 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)