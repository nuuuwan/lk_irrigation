# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_01:25:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 01:25:48 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-11-09 01:22:28 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-09 01:22:15 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-09 01:20:37 | Glencourse (Kelani Ganga) | 13.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-09 01:11:39 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.106 |  |
| 2026-11-09 01:11:14 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-11-09 01:09:09 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.146 |  |
| 2026-11-09 01:08:19 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-11-09 01:07:58 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-09 01:07:07 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-11-09 01:06:10 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-09 01:04:44 | Thawalama (Gin Ganga) | 4.03 | 🟡 Alert | -0.096 |  |
| 2026-11-09 01:03:44 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.051 |  |
| 2026-11-09 01:03:25 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:03:08 | Dunamale (Aththanagalu Oya) | 4.05 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-09 01:02:58 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.019 |  |
| 2026-11-09 01:02:43 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:34 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:20 | Giriulla (Maha Oya) | 4.16 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-09 01:02:17 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:16 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:07 | Hanwella (Kelani Ganga) | 5.07 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-09 01:02:02 | Moragaswewa (Deduru Oya) | 3.37 | 🟢 Normal | -0.021 |  |
| 2026-11-09 01:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-09 01:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.64 | 🟡 Alert | 0.024 | 🔺 Rising |
| 2026-11-09 01:01:24 | Ellagawa (Kalu Ganga) | 8.13 | 🟢 Normal | -0.021 |  |
| 2026-11-09 01:00:36 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.122 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 01:08:19 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-11-09 01:03:08 | Dunamale (Aththanagalu Oya) | 4.05 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-09 01:07:58 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-09 01:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.64 | 🟡 Alert | 0.024 | 🔺 Rising |
| 2026-11-09 01:22:15 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-09 00:16:41 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | 0.000 |  |
| 2026-11-09 01:04:44 | Thawalama (Gin Ganga) | 4.03 | 🟡 Alert | -0.096 |  |
| 2026-11-09 01:02:20 | Giriulla (Maha Oya) | 4.16 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-09 01:06:10 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-09 01:02:07 | Hanwella (Kelani Ganga) | 5.07 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-09 01:22:28 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-08 23:05:11 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-09 01:20:37 | Glencourse (Kelani Ganga) | 13.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-08 23:04:45 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 00:12:24 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-09 00:12:33 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 00:04:44 | Horowpothana (Yan Oya) | 3.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 01:02:43 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:17 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:03:25 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:16 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:34 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:07:07 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-09 01:11:14 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 01:02:58 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.019 |  |
| 2026-11-09 01:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-09 01:01:24 | Ellagawa (Kalu Ganga) | 8.13 | 🟢 Normal | -0.021 |  |
| 2026-11-09 01:25:48 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-11-09 01:02:02 | Moragaswewa (Deduru Oya) | 3.37 | 🟢 Normal | -0.021 |  |
| 2026-11-09 00:15:16 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.042 |  |
| 2026-11-09 01:03:44 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.051 |  |
| 2026-11-09 01:11:39 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.106 |  |
| 2026-11-09 01:00:36 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.122 |  |
| 2026-11-09 01:09:09 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.146 |  |
| 2026-11-09 00:08:35 | Holombuwa (Kelani Ganga) | 2.19 | 🟢 Normal | -0.381 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)