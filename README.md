# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_23:32:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,019 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 23:32:22 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.007 |  |
| 2026-11-04 23:28:15 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:15:00 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:10:47 | Magura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-04 23:09:57 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-04 23:09:45 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:08:54 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.021 |  |
| 2026-11-04 23:08:52 | Thanamalwila (Kirindi Oya) | 3.21 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-11-04 23:08:43 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-04 23:08:01 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-04 23:07:14 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:07:04 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.046 |  |
| 2026-11-04 23:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-11-04 23:05:17 | Giriulla (Maha Oya) | 2.85 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-11-04 23:05:10 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-11-04 23:04:44 | Urawa (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-04 23:04:37 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:04:04 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-11-04 23:03:34 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -2.673 |  |
| 2026-11-04 23:03:12 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-11-04 23:03:08 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.061 |  |
| 2026-11-04 23:02:55 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-04 23:02:43 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 23:02:42 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-04 23:02:37 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-11-04 23:02:33 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:02:27 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.103 |  |
| 2026-11-04 23:02:13 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-04 23:02:10 | Moragaswewa (Deduru Oya) | 4.11 | 🟢 Normal | -0.049 |  |
| 2026-11-04 23:01:49 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-04 23:01:34 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-11-04 23:01:13 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-11-04 23:00:27 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:00:22 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 23:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-11-04 23:08:52 | Thanamalwila (Kirindi Oya) | 3.21 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-11-04 23:05:17 | Giriulla (Maha Oya) | 2.85 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-11-04 23:02:42 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-04 23:08:43 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-04 23:09:57 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-04 23:04:44 | Urawa (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-04 23:02:55 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-04 23:02:13 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-04 22:02:45 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-04 23:08:01 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-04 23:10:47 | Magura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-04 23:02:43 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 23:07:14 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:28:15 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:01:13 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:02:36 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:09:45 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:15:00 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:00:27 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:32:22 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.007 |  |
| 2026-11-04 23:04:04 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-11-04 23:01:49 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-04 23:02:37 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-11-04 23:05:10 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-11-04 23:01:34 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-11-04 23:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-11-04 23:00:22 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-04 23:08:54 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.021 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 23:03:12 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-04 23:07:04 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.046 |  |
| 2026-11-04 23:02:10 | Moragaswewa (Deduru Oya) | 4.11 | 🟢 Normal | -0.049 |  |
| 2026-11-04 22:00:22 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.050 |  |
| 2026-11-04 23:03:08 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.061 |  |
| 2026-11-04 23:02:27 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.103 |  |
| 2026-11-04 23:03:34 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -2.673 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)