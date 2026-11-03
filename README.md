# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_00:03:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 00:03:29 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-04 00:03:28 | Giriulla (Maha Oya) | 3.40 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-11-04 00:03:26 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.033 |  |
| 2026-11-04 00:03:19 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 00:02:57 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.050 |  |
| 2026-11-04 00:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-11-04 00:02:41 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.062 |  |
| 2026-11-04 00:02:23 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-04 00:02:14 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.141 |  |
| 2026-11-04 00:02:01 | Ellagawa (Kalu Ganga) | 3.00 | 🟢 Normal | -3.933 |  |
| 2026-11-04 00:01:55 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-11-04 00:01:43 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 00:01:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-04 00:01:25 | Peradeniya (Mahaweli Ganga) | 3.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 00:00:12 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:57:57 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:41:05 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-03 23:39:26 | Moraketiya (Walawe Ganga) | 3.24 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-11-03 23:26:42 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:25:40 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 22:03:37 | Urawa (Nilwala Ganga) | 3.20 | 🟡 Alert | 0.212 | 🔺 Rising |
| 2026-11-03 23:39:26 | Moraketiya (Walawe Ganga) | 3.24 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-11-04 00:03:29 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-04 00:03:28 | Giriulla (Maha Oya) | 3.40 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-11-03 23:02:11 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-04 00:01:55 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-11-03 23:02:06 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 23:07:05 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-03 22:00:10 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-03 23:06:28 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-04 00:01:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-04 00:01:25 | Peradeniya (Mahaweli Ganga) | 3.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 23:41:05 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-03 23:05:08 | Moragaswewa (Deduru Oya) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:49:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 00:01:43 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:04:55 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:26:42 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:19:04 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 00:00:12 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:03:03 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:22:03 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.008 |  |
| 2026-11-04 00:03:19 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 00:02:23 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-03 23:02:27 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-11-04 00:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-11-03 23:02:34 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-11-03 23:01:15 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-11-04 00:03:26 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.033 |  |
| 2026-11-03 22:08:07 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.037 |  |
| 2026-11-04 00:02:57 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.050 |  |
| 2026-11-04 00:02:41 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.062 |  |
| 2026-11-03 23:07:01 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.071 |  |
| 2026-11-04 00:02:14 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.141 |  |
| 2026-11-03 23:01:24 | Thanamalwila (Kirindi Oya) | 2.31 | 🟢 Normal | -0.251 |  |
| 2026-11-04 00:02:01 | Ellagawa (Kalu Ganga) | 3.00 | 🟢 Normal | -3.933 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)