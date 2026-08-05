# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_11:20:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,524 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 11:20:07 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:14:06 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.038 |  |
| 2026-08-05 11:12:54 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.026 |  |
| 2026-08-05 11:12:51 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:10:37 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:10:24 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:09:20 | Rathnapura (Kalu Ganga) | 4.67 | 🟢 Normal | -0.091 |  |
| 2026-08-05 11:09:19 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | -0.028 |  |
| 2026-08-05 11:09:04 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:08:50 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:07:55 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:07:49 | Kithulgala (Kelani Ganga) | 2.86 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-05 11:06:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:05:15 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:04:53 | Peradeniya (Mahaweli Ganga) | 5.30 | 🟡 Alert | 0.306 | 🔺 Rising |
| 2026-08-05 11:04:46 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-08-05 11:04:31 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.067 |  |
| 2026-08-05 11:04:05 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:59 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.080 |  |
| 2026-08-05 11:03:55 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:45 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:44 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:03:36 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:29 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:24 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.065 |  |
| 2026-08-05 11:03:23 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.060 |  |
| 2026-08-05 11:03:21 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.034 |  |
| 2026-08-05 11:03:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:14 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:02:56 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:02:34 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:02:33 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:02:31 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.020 |  |
| 2026-08-05 11:02:31 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.031 |  |
| 2026-08-05 11:02:30 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:01:56 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:01:40 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 11:01:22 | Nawalapitiya (Mahaweli Ganga) | 2.94 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-05 11:00:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 11:04:53 | Peradeniya (Mahaweli Ganga) | 5.30 | 🟡 Alert | 0.306 | 🔺 Rising |
| 2026-08-05 11:01:22 | Nawalapitiya (Mahaweli Ganga) | 2.94 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-05 11:07:49 | Kithulgala (Kelani Ganga) | 2.86 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-05 11:01:40 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 11:03:36 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:20:07 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:45 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:23 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:06:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:02:33 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:02:30 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:14 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:29 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:01:56 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:03:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:10:24 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:08:50 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:10:37 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:12:51 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:04:05 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-05 11:09:04 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:03:44 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:02:56 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:07:55 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:02:34 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:00:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-05 11:02:31 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.020 |  |
| 2026-08-05 11:04:46 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-08-05 11:12:54 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.026 |  |
| 2026-08-05 11:09:19 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | -0.028 |  |
| 2026-08-05 11:02:31 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.031 |  |
| 2026-08-05 11:03:21 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.034 |  |
| 2026-08-05 11:14:06 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.038 |  |
| 2026-08-05 11:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.060 |  |
| 2026-08-05 11:03:24 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.065 |  |
| 2026-08-05 11:04:31 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.067 |  |
| 2026-08-05 11:03:59 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.080 |  |
| 2026-08-05 11:09:20 | Rathnapura (Kalu Ganga) | 4.67 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)