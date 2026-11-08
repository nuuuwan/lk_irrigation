# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_03:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,728 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 03:03:00 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 03:03:00 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 03:02:59 | Glencourse (Kelani Ganga) | 12.97 | 🟢 Normal | -0.224 |  |
| 2026-11-09 03:02:47 | Horowpothana (Yan Oya) | 3.14 | 🟢 Normal | 0.000 |  |
| 2026-11-09 03:02:35 | Thawalama (Gin Ganga) | 3.86 | 🟢 Normal | -0.084 |  |
| 2026-11-09 03:02:27 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.039 |  |
| 2026-11-09 03:02:27 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | -0.020 |  |
| 2026-11-09 03:01:50 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | -0.144 |  |
| 2026-11-09 03:01:42 | Moragaswewa (Deduru Oya) | 3.31 | 🟢 Normal | -0.040 |  |
| 2026-11-09 03:00:14 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-11-09 02:52:22 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-09 02:33:52 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.088 |  |
| 2026-11-09 02:26:07 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.015 |  |
| 2026-11-09 02:22:00 | Giriulla (Maha Oya) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-11-09 02:17:57 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 01:08:19 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-11-09 03:03:00 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 02:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.66 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 02:07:01 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.013 | 🔺 Rising |
| 2026-11-09 02:04:52 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-09 00:16:41 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | 0.000 |  |
| 2026-11-09 02:05:53 | Baddegama (Gin Ganga) | 3.40 | 🟢 Normal | 10.588 | 🔺 Rising |
| 2026-11-09 02:04:53 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-09 02:03:42 | Hanwella (Kelani Ganga) | 5.20 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-11-08 23:05:11 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-09 02:11:38 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 01:56:52 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-09 02:02:49 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 02:22:00 | Giriulla (Maha Oya) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-11-09 03:02:47 | Horowpothana (Yan Oya) | 3.14 | 🟢 Normal | 0.000 |  |
| 2026-11-09 02:17:57 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-09 02:03:13 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 03:03:00 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:07:07 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-11-09 02:03:01 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-09 02:52:22 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-09 02:26:07 | Urawa (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.015 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 03:02:27 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | -0.020 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-09 03:00:14 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-11-09 02:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.029 |  |
| 2026-11-09 03:02:27 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.039 |  |
| 2026-11-09 03:01:42 | Moragaswewa (Deduru Oya) | 3.31 | 🟢 Normal | -0.040 |  |
| 2026-11-09 00:15:16 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.042 |  |
| 2026-11-09 02:00:42 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.052 |  |
| 2026-11-09 02:09:44 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-11-09 03:02:35 | Thawalama (Gin Ganga) | 3.86 | 🟢 Normal | -0.084 |  |
| 2026-11-09 02:33:52 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.088 |  |
| 2026-11-09 02:06:23 | Holombuwa (Kelani Ganga) | 1.93 | 🟢 Normal | -0.132 |  |
| 2026-11-09 03:01:50 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | -0.144 |  |
| 2026-11-09 03:02:59 | Glencourse (Kelani Ganga) | 12.97 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)