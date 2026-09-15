# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_14:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,614 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 14:10:24 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:09:23 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-09-15 14:08:34 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-15 14:08:12 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 14:06:55 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:05:43 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.138 |  |
| 2026-09-15 14:05:22 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:05:15 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.071 |  |
| 2026-09-15 14:04:55 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-15 14:04:43 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-09-15 14:04:34 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | -0.039 |  |
| 2026-09-15 14:04:33 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-15 14:04:19 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-09-15 14:03:50 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:03:27 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:03:10 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:59 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -0.162 |  |
| 2026-09-15 14:02:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 14:02:37 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:29 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-09-15 14:02:29 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-09-15 14:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-15 14:02:23 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.101 |  |
| 2026-09-15 14:02:19 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:19 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:03 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:51 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:50 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 14:01:46 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:37 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:31 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-09-15 14:01:17 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-09-15 14:01:00 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:44:10 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 14:02:59 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -0.162 |  |
| 2026-09-15 14:02:29 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-09-15 13:12:24 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-15 14:04:55 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-15 14:08:34 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-15 14:04:33 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-15 14:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 14:01:50 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 14:08:12 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 14:02:19 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:51 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:06:55 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:00 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:03 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:03:10 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:03:50 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:05:22 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:46 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:44:10 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:03:27 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:02:19 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:01:37 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:05:27 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:10:24 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 14:04:43 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-09-15 14:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-15 14:04:19 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-09-15 14:01:17 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-09-15 14:02:29 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-09-15 14:01:31 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-09-15 14:09:23 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-09-15 14:04:34 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | -0.039 |  |
| 2026-09-15 13:12:23 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.063 |  |
| 2026-09-15 13:06:55 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.065 |  |
| 2026-09-15 14:05:15 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.071 |  |
| 2026-09-15 13:03:44 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.089 |  |
| 2026-09-15 14:02:23 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.101 |  |
| 2026-09-15 14:05:43 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)