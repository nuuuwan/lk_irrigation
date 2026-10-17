# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_13:34:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 13:34:48 | Thanthirimale (Malwathu Oya) | 2.56 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-10-17 13:16:23 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.091 |  |
| 2026-10-17 13:12:29 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.018 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |
| 2026-10-17 13:08:56 | Magura (Kalu Ganga) | 3.37 | 🟢 Normal | -50.400 |  |
| 2026-10-17 13:08:31 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-10-17 13:08:21 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:08:08 | Baddegama (Gin Ganga) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:08:01 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.101 |  |
| 2026-10-17 13:07:48 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-17 13:07:21 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | -0.057 |  |
| 2026-10-17 13:06:18 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-10-17 13:05:50 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:05:50 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | -0.019 |  |
| 2026-10-17 13:05:43 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.041 |  |
| 2026-10-17 13:05:30 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-10-17 13:05:05 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 13:04:05 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:03:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:03:32 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-17 13:03:31 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-10-17 13:03:25 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:03:07 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -72.000 |  |
| 2026-10-17 13:03:05 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -72.000 |  |
| 2026-10-17 13:02:55 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:02:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:02:41 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:02:36 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 13:02:36 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-10-17 13:02:22 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.039 |  |
| 2026-10-17 13:02:21 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.073 |  |
| 2026-10-17 13:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.73 | 🟡 Alert | -0.020 |  |
| 2026-10-17 13:02:10 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:02:06 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-17 13:01:47 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | -0.020 |  |
| 2026-10-17 13:01:47 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:01:17 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-10-17 13:01:12 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.048 |  |
| 2026-10-17 13:00:44 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 13:00:24 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | -0.046 |  |
| 2026-10-17 13:00:20 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 13:02:36 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 13:07:48 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-17 13:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.73 | 🟡 Alert | -0.020 |  |
| 2026-10-17 13:00:44 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 13:05:05 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 13:34:48 | Thanthirimale (Malwathu Oya) | 2.56 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-10-17 13:08:21 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:02:55 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:05:50 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:04:05 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:03:56 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-17 13:08:08 | Baddegama (Gin Ganga) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:02:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:02:41 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:03:25 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:00:20 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:02:10 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-17 13:02:36 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-10-17 13:08:31 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-10-17 13:12:29 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.018 |  |
| 2026-10-17 13:05:50 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | -0.019 |  |
| 2026-10-17 13:03:32 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-17 13:01:47 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | -0.020 |  |
| 2026-10-17 13:01:17 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-10-17 13:02:06 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-17 13:05:30 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-10-17 13:03:31 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-10-17 13:02:22 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.039 |  |
| 2026-10-17 13:06:18 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-10-17 13:05:43 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.041 |  |
| 2026-10-17 13:00:24 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | -0.046 |  |
| 2026-10-17 13:01:12 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.048 |  |
| 2026-10-17 13:07:21 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | -0.057 |  |
| 2026-10-17 13:02:21 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.073 |  |
| 2026-10-17 13:16:23 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.091 |  |
| 2026-10-17 13:08:01 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.101 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |
| 2026-10-17 13:03:07 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)