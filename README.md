# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_11:12:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,645 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 11:12:36 | Peradeniya (Mahaweli Ganga) | 3.97 | 🟢 Normal | -0.028 |  |
| 2026-11-13 11:11:09 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-11-13 11:10:25 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-11-13 11:09:43 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.081 |  |
| 2026-11-13 11:08:26 | Baddegama (Gin Ganga) | 4.16 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-13 11:08:21 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.028 |  |
| 2026-11-13 11:08:01 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:07:23 | Thaldena (Mahaweli Ganga) | 1.11 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2026-11-13 11:07:18 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2026-11-13 11:06:50 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.046 |  |
| 2026-11-13 11:06:26 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 11:06:17 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:06:10 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | -0.019 |  |
| 2026-11-13 11:05:59 | Pitabeddara (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-11-13 11:05:55 | Putupaula (Kalu Ganga) | 2.36 | 🟢 Normal | -0.019 |  |
| 2026-11-13 11:05:34 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:04:39 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.030 |  |
| 2026-11-13 11:04:20 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-11-13 11:04:20 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | -0.040 |  |
| 2026-11-13 11:04:20 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-11-13 11:04:18 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.051 |  |
| 2026-11-13 11:03:41 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.116 |  |
| 2026-11-13 11:03:35 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | -0.045 |  |
| 2026-11-13 11:03:25 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.022 |  |
| 2026-11-13 11:03:22 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-13 11:03:08 | Katharagama (Menik Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:03:06 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 11:02:49 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-13 11:02:21 | Panadugama (Nilwala Ganga) | 6.28 | 🟠 Minor Flood | -0.024 |  |
| 2026-11-13 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.05 | 🟡 Alert | -0.020 |  |
| 2026-11-13 11:02:16 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:02:06 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 11:02:05 | Thanamalwila (Kirindi Oya) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-11-13 11:01:33 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.065 |  |
| 2026-11-13 11:01:25 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:01:12 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | -0.052 |  |
| 2026-11-13 11:00:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 11:06:26 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 11:08:26 | Baddegama (Gin Ganga) | 4.16 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-13 11:02:21 | Panadugama (Nilwala Ganga) | 6.28 | 🟠 Minor Flood | -0.024 |  |
| 2026-11-13 11:06:10 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | -0.019 |  |
| 2026-11-13 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.05 | 🟡 Alert | -0.020 |  |
| 2026-11-13 11:07:23 | Thaldena (Mahaweli Ganga) | 1.11 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2026-11-13 11:00:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-13 11:02:06 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 11:03:06 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 11:02:16 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:05:34 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:05:13 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:03:08 | Katharagama (Menik Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:08:01 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:10:25 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-11-13 11:04:20 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-11-13 11:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:06:17 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:01:25 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:05:55 | Putupaula (Kalu Ganga) | 2.36 | 🟢 Normal | -0.019 |  |
| 2026-11-13 11:03:22 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-13 11:11:09 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-11-13 11:04:20 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-11-13 11:02:49 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-13 10:02:30 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-11-13 11:03:25 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.022 |  |
| 2026-11-13 11:12:36 | Peradeniya (Mahaweli Ganga) | 3.97 | 🟢 Normal | -0.028 |  |
| 2026-11-13 11:08:21 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.028 |  |
| 2026-11-13 11:04:39 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.030 |  |
| 2026-11-13 11:04:20 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | -0.040 |  |
| 2026-11-13 11:03:35 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | -0.045 |  |
| 2026-11-13 11:06:50 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.046 |  |
| 2026-11-13 11:04:18 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.051 |  |
| 2026-11-13 11:01:12 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | -0.052 |  |
| 2026-11-13 11:05:59 | Pitabeddara (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-11-13 11:02:05 | Thanamalwila (Kirindi Oya) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-11-13 11:01:33 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.065 |  |
| 2026-11-13 11:09:43 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.081 |  |
| 2026-11-13 11:03:41 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)