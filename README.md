# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_06:32:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,914 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 06:32:47 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:25:43 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:15:46 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:13:19 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 06:11:54 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:09:44 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.027 |  |
| 2026-09-09 06:09:18 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-09 06:07:32 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:07:24 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:07:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:06:42 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-09 06:05:50 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:05:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.116 |  |
| 2026-09-09 06:05:22 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-09-09 06:05:11 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:04:30 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:04:07 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.060 |  |
| 2026-09-09 06:03:52 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-09 06:03:49 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-09-09 06:03:35 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:03:34 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.019 |  |
| 2026-09-09 06:03:23 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:02:57 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:02:48 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:02:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:02:24 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-09 06:02:21 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.385 |  |
| 2026-09-09 06:02:07 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-09 06:01:56 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:01:54 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-09-09 06:01:51 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-09 06:01:46 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:01:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:01:42 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.111 |  |
| 2026-09-09 06:01:39 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-09-09 06:01:24 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-09 06:01:14 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:00:49 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-09 06:00:11 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 06:02:07 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-09 06:02:24 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-09 06:01:24 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-09 06:09:18 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-09 06:06:42 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-09 06:00:49 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-09 06:01:51 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-09 06:13:19 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 06:03:52 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-09 06:07:32 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:01:14 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:07:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:00:11 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:01:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:01:56 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:11:54 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:32:47 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:07:24 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:04:30 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:05:50 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:03:23 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:02:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:15:46 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:02:57 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:03:35 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:01:46 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:25:43 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:02:48 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 06:03:34 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.019 |  |
| 2026-09-09 06:01:39 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-09-09 06:01:54 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-09-09 06:05:22 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-09-09 06:09:44 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.027 |  |
| 2026-09-09 06:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-09-09 06:04:07 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.060 |  |
| 2026-09-09 06:01:42 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.111 |  |
| 2026-09-09 06:05:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.116 |  |
| 2026-09-09 06:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.385 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)