# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_13:18:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 13:18:12 | Baddegama (Gin Ganga) | 3.50 | 🟡 Alert | -0.026 |  |
| 2026-11-14 13:11:25 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:11:24 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:10:42 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.061 |  |
| 2026-11-14 13:07:41 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-11-14 13:07:15 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-11-14 13:06:54 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:06:43 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:06:43 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-11-14 13:06:11 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.037 |  |
| 2026-11-14 13:05:24 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.014 |  |
| 2026-11-14 13:05:20 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:04:44 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 13:04:40 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:04:35 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-14 13:04:27 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-14 13:04:15 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.020 |  |
| 2026-11-14 13:03:49 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-14 13:03:40 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.030 |  |
| 2026-11-14 13:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.58 | 🟢 Normal | -0.112 |  |
| 2026-11-14 13:03:29 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.030 |  |
| 2026-11-14 13:03:23 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:03:19 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-14 13:03:08 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 13:03:05 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:03:03 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:03:02 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-14 13:02:54 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:02:46 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.044 |  |
| 2026-11-14 13:02:35 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-11-14 13:02:32 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:02:29 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:02:12 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:01:49 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:00:59 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:00:49 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 13:00:47 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:00:37 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | -0.060 |  |
| 2026-11-14 13:00:23 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 13:04:44 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 13:18:12 | Baddegama (Gin Ganga) | 3.50 | 🟡 Alert | -0.026 |  |
| 2026-11-14 13:03:29 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.030 |  |
| 2026-11-14 13:04:35 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-14 13:03:49 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-14 13:03:02 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-14 13:03:19 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-14 13:00:49 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 13:03:08 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 13:06:54 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:00:59 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:03:03 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:11:25 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:02:54 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:02:32 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:02:12 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:05:20 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:02:29 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-14 13:07:41 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-11-14 13:07:15 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.009 |  |
| 2026-11-14 13:04:40 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:03:23 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:06:43 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:00:47 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:03:05 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:00:23 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:01:49 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-14 13:05:24 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.014 |  |
| 2026-11-14 13:04:27 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-11-14 13:04:15 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.020 |  |
| 2026-11-14 13:03:40 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.030 |  |
| 2026-11-14 13:06:43 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-11-14 13:02:35 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-11-14 13:06:11 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | -0.037 |  |
| 2026-11-14 13:02:46 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.044 |  |
| 2026-11-14 13:00:37 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | -0.060 |  |
| 2026-11-14 13:10:42 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.061 |  |
| 2026-11-14 13:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.58 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)