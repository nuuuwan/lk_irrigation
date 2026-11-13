# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_00:23:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 00:23:41 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.007 |  |
| 2026-11-14 00:14:27 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-11-14 00:13:09 | Ellagawa (Kalu Ganga) | 7.07 | 🟢 Normal | -0.085 |  |
| 2026-11-14 00:12:23 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.067 |  |
| 2026-11-14 00:12:07 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.018 |  |
| 2026-11-14 00:10:12 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:09:21 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.125 |  |
| 2026-11-14 00:08:55 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.069 |  |
| 2026-11-14 00:07:44 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | -0.038 |  |
| 2026-11-14 00:07:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-14 00:07:01 | Baddegama (Gin Ganga) | 3.92 | 🟡 Alert | -0.029 |  |
| 2026-11-14 00:06:39 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.005 |  |
| 2026-11-14 00:05:34 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-11-14 00:04:59 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:04:38 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-14 00:04:17 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:04:01 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.039 |  |
| 2026-11-14 00:03:59 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.030 |  |
| 2026-11-14 00:03:43 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:03:40 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:03:15 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 00:02:43 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-11-14 00:02:34 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-11-14 00:02:23 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:02:21 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-11-14 00:02:21 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | -0.033 |  |
| 2026-11-14 00:02:17 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.62 | 🟡 Alert | -0.039 |  |
| 2026-11-14 00:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:01:56 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-11-14 00:01:43 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:01:37 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:01:10 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:00:39 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 00:00:39 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 00:07:01 | Baddegama (Gin Ganga) | 3.92 | 🟡 Alert | -0.029 |  |
| 2026-11-14 00:07:44 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | -0.038 |  |
| 2026-11-14 00:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.62 | 🟡 Alert | -0.039 |  |
| 2026-11-13 23:04:27 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.145 |  |
| 2026-11-14 00:07:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 00:03:15 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 00:10:12 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:01:10 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:02:23 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 23:03:36 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:01:37 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:14:27 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-11-14 00:06:39 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.005 |  |
| 2026-11-14 00:23:41 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.007 |  |
| 2026-11-14 00:04:17 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:03:43 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:04:59 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:02:17 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:01:43 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:03:40 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:02:43 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-11-14 00:12:07 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.018 |  |
| 2026-11-14 00:04:38 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-14 00:02:21 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-11-14 00:05:34 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-11-14 00:02:34 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-14 00:03:59 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.030 |  |
| 2026-11-14 00:01:56 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-11-14 00:02:21 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | -0.033 |  |
| 2026-11-14 00:04:01 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.039 |  |
| 2026-11-14 00:12:23 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.067 |  |
| 2026-11-14 00:08:55 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.069 |  |
| 2026-11-14 00:13:09 | Ellagawa (Kalu Ganga) | 7.07 | 🟢 Normal | -0.085 |  |
| 2026-11-14 00:09:21 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)