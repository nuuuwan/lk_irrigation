# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_01:24:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,560 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 01:24:12 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:20:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.008 |  |
| 2026-10-21 01:13:37 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:09:01 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 01:07:15 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-21 01:06:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:05:42 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-21 01:05:00 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-21 01:04:55 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.032 |  |
| 2026-10-21 01:04:27 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 01:04:08 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:04:08 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:03:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:03:30 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-10-21 01:03:01 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-10-21 01:02:53 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 01:02:36 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:02:35 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 01:02:34 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.022 |  |
| 2026-10-21 01:02:32 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:02:09 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:01:54 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.010 |  |
| 2026-10-21 01:01:54 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-21 01:01:29 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:01:26 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.020 |  |
| 2026-10-21 01:01:19 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-21 01:01:19 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:01:09 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.085 |  |
| 2026-10-21 01:01:02 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:00:48 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-10-21 01:00:06 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:54:05 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 01:01:54 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.010 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-21 01:01:54 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-21 01:02:53 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 01:04:27 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 01:09:01 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 00:01:39 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 01:02:35 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 01:02:36 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:01:19 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:03:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:04:08 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:01:02 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:02:09 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:01:29 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:06:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:09:28 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:02:32 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:24:12 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:03:38 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:13:37 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 01:20:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.008 |  |
| 2026-10-21 01:07:15 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-21 01:00:48 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:00:32 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-21 01:05:42 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-21 01:00:06 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-21 01:01:19 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-21 01:05:00 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-21 01:01:26 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.020 |  |
| 2026-10-21 01:02:34 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.022 |  |
| 2026-10-21 00:04:07 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.027 |  |
| 2026-10-21 01:04:55 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.032 |  |
| 2026-10-21 01:03:01 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-10-21 01:03:30 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-10-21 01:01:09 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)