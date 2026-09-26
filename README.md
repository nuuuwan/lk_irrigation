# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_14:08:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 14:08:03 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 14:07:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.043 |  |
| 2026-09-26 14:07:14 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-09-26 14:07:09 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:06:37 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-26 14:06:23 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-26 14:06:19 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.252 |  |
| 2026-09-26 14:05:59 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-26 14:05:25 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | -0.011 |  |
| 2026-09-26 14:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-26 14:04:50 | Deraniyagala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-26 14:04:31 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 14:04:26 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:04:23 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-09-26 14:04:21 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:04:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:03:59 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 14:03:42 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.009 |  |
| 2026-09-26 14:03:40 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.068 |  |
| 2026-09-26 14:03:37 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:03:34 | Hanwella (Kelani Ganga) | 5.39 | 🟢 Normal | -0.030 |  |
| 2026-09-26 14:03:34 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-26 14:03:29 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:03:21 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 14:03:18 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.272 |  |
| 2026-09-26 14:03:04 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:03:03 | Nawalapitiya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.100 |  |
| 2026-09-26 14:02:27 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:02:26 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-09-26 14:02:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:02:21 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:01:55 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:01:53 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:01:50 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:01:15 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:00:51 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 14:00:48 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-26 13:54:06 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 14:08:03 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 14:03:21 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 14:05:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.98 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-26 14:05:25 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | -0.011 |  |
| 2026-09-26 13:02:08 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-26 14:05:59 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-26 14:04:50 | Deraniyagala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-26 14:04:31 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 14:00:51 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 14:03:59 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 14:06:37 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-26 14:01:50 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:02:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:01:15 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:03:37 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:04:21 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:04:26 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:03:04 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:02:27 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:02:21 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:04:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:07:09 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:01:53 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:01:55 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:03:29 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 14:03:42 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.009 |  |
| 2026-09-26 14:00:48 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-26 14:06:23 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-26 14:03:34 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-26 14:02:26 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-09-26 14:07:14 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-09-26 14:04:23 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-09-26 14:03:34 | Hanwella (Kelani Ganga) | 5.39 | 🟢 Normal | -0.030 |  |
| 2026-09-26 13:24:23 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.031 |  |
| 2026-09-26 14:07:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.043 |  |
| 2026-09-26 14:03:40 | Kithulgala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.068 |  |
| 2026-09-26 14:03:03 | Nawalapitiya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.100 |  |
| 2026-09-26 14:06:19 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.252 |  |
| 2026-09-26 14:03:18 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.272 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)