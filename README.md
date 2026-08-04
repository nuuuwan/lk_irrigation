# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_23:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,084 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 23:15:19 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:12:45 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-08-04 23:11:00 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | -0.060 |  |
| 2026-08-04 23:10:08 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-04 23:07:03 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | -0.238 |  |
| 2026-08-04 23:06:44 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:06:07 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.019 |  |
| 2026-08-04 23:06:07 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:05:54 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.039 |  |
| 2026-08-04 23:05:50 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-08-04 23:05:20 | Glencourse (Kelani Ganga) | 13.38 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-04 23:05:07 | Nawalapitiya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:04:42 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-04 23:04:30 | Peradeniya (Mahaweli Ganga) | 4.58 | 🟢 Normal | -0.778 |  |
| 2026-08-04 23:04:02 | Deraniyagala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.213 |  |
| 2026-08-04 23:03:35 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:03:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 23:03:09 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-04 23:03:02 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:02:57 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-08-04 23:02:56 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-04 23:02:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:02:32 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 23:02:30 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.035 |  |
| 2026-08-04 23:02:26 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-08-04 23:02:26 | Rathnapura (Kalu Ganga) | 5.82 | 🟡 Alert | -0.077 |  |
| 2026-08-04 23:01:33 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-04 23:01:33 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:01:12 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:00:57 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:00:49 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.013 |  |
| 2026-08-04 23:00:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:59:06 | Peradeniya (Mahaweli Ganga) | 4.65 | 🟢 Normal | -0.778 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 22:08:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.031 |  |
| 2026-08-04 23:02:26 | Rathnapura (Kalu Ganga) | 5.82 | 🟡 Alert | -0.077 |  |
| 2026-08-04 23:05:20 | Glencourse (Kelani Ganga) | 13.38 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-04 23:03:09 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-04 23:02:32 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 23:02:56 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-04 23:03:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 23:00:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:05:07 | Nawalapitiya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:00:57 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:15:19 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:06:44 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:01:12 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:02:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:01:33 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:03:35 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:03:02 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:06:07 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 22:01:10 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:10:08 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-04 23:04:42 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-04 23:01:33 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-04 23:00:49 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.013 |  |
| 2026-08-04 23:06:07 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.019 |  |
| 2026-08-04 23:12:45 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-08-04 23:05:50 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-08-04 23:02:57 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-08-04 23:02:26 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-08-04 22:00:57 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-08-04 23:02:30 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.035 |  |
| 2026-08-04 23:05:54 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.039 |  |
| 2026-08-04 23:11:00 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | -0.060 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-04 23:04:02 | Deraniyagala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.213 |  |
| 2026-08-04 23:07:03 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | -0.238 |  |
| 2026-08-04 23:04:30 | Peradeniya (Mahaweli Ganga) | 4.58 | 🟢 Normal | -0.778 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)