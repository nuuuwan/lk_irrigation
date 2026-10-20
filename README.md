# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_00:09:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,525 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 00:09:28 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:08:52 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:08:40 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.028 |  |
| 2026-10-21 00:07:55 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-10-21 00:07:31 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-10-21 00:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.018 |  |
| 2026-10-21 00:06:18 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-10-21 00:05:48 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:05:35 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-10-21 00:05:23 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-21 00:04:23 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.117 |  |
| 2026-10-21 00:04:23 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 00:04:18 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-10-21 00:04:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:04:07 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.027 |  |
| 2026-10-21 00:04:03 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:03:44 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 00:03:38 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:03:21 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-21 00:03:18 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:03:06 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:02:39 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.049 |  |
| 2026-10-21 00:02:37 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:02:25 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.070 |  |
| 2026-10-21 00:02:17 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:02:07 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:01:39 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 00:01:37 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:01:10 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:01:00 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:00:32 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:00:31 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-10-21 00:00:10 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:00:02 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:46:39 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:34:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 00:00:31 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-21 00:03:21 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-21 00:05:23 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-20 23:03:23 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-20 23:09:48 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 00:04:23 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 00:01:39 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 00:03:44 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 00:01:00 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:01:37 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:03:06 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:00:10 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:04:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:09:28 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:02:07 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:03:38 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:08:52 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 00:05:35 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-10-21 00:05:48 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:00:32 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:01:10 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:04:03 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:02:37 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:03:18 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:02:17 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-10-21 00:06:18 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-10-21 00:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.018 |  |
| 2026-10-21 00:07:31 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-10-21 00:07:55 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-10-21 00:04:18 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-10-21 00:04:07 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.027 |  |
| 2026-10-21 00:08:40 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -0.028 |  |
| 2026-10-21 00:02:39 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.049 |  |
| 2026-10-21 00:02:25 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.070 |  |
| 2026-10-21 00:04:23 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)