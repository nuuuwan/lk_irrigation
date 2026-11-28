# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_19:16:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **328,223 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 19:16:05 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-28 19:15:02 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-28 19:12:29 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:11:33 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:10:34 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.018 |  |
| 2026-11-28 19:10:14 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.026 |  |
| 2026-11-28 19:09:37 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-28 19:08:14 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:07:56 | Moraketiya (Walawe Ganga) | 3.05 | 🟡 Alert | -0.028 |  |
| 2026-11-28 19:07:26 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-28 19:07:16 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:06:28 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-11-28 19:06:01 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.119 |  |
| 2026-11-28 19:05:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.090 |  |
| 2026-11-28 19:05:24 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -0.076 |  |
| 2026-11-28 19:04:59 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.063 |  |
| 2026-11-28 19:04:35 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:04:27 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-28 19:04:27 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-28 19:03:55 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.058 |  |
| 2026-11-28 19:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:03:49 | Moragaswewa (Deduru Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-11-28 19:03:21 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-28 19:03:18 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.081 |  |
| 2026-11-28 19:03:14 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-11-28 19:03:06 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-28 19:03:05 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.022 |  |
| 2026-11-28 19:02:55 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:02:24 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-11-28 19:02:21 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-28 19:02:14 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-11-28 19:02:14 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-28 19:01:50 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-28 19:01:17 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 19:00:55 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 19:04:27 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-28 18:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.09 | 🟡 Alert | -0.010 |  |
| 2026-11-28 19:03:05 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.022 |  |
| 2026-11-28 19:07:56 | Moraketiya (Walawe Ganga) | 3.05 | 🟡 Alert | -0.028 |  |
| 2026-11-28 19:03:06 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-28 19:06:28 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-11-28 19:07:26 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-28 19:09:37 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-28 19:03:21 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-28 19:04:27 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-28 19:15:02 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-28 19:16:05 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-28 19:01:17 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 18:01:41 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 19:00:55 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:08:14 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:07:16 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:02:55 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:04:35 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:11:33 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:12:29 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 19:02:21 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-28 19:01:50 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-28 19:03:49 | Moragaswewa (Deduru Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-11-28 19:02:14 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-11-28 19:02:24 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-11-28 19:10:34 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.018 |  |
| 2026-11-28 19:02:14 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-28 19:03:14 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-11-28 19:10:14 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.026 |  |
| 2026-11-28 18:03:25 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-11-28 18:03:29 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.030 |  |
| 2026-11-28 19:03:55 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.058 |  |
| 2026-11-28 19:04:59 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.063 |  |
| 2026-11-28 19:05:24 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -0.076 |  |
| 2026-11-28 19:03:18 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.081 |  |
| 2026-11-28 19:05:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.090 |  |
| 2026-11-28 19:06:01 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)