# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_16:33:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,792 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 16:33:16 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:14:24 | Magura (Kalu Ganga) | 4.94 | 🟡 Alert | -0.034 |  |
| 2026-10-14 16:12:11 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.009 |  |
| 2026-10-14 16:11:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-10-14 16:10:36 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:09:56 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:09:27 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:07:54 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:07:09 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.048 |  |
| 2026-10-14 16:06:42 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 1.083 | 🔺 Rising |
| 2026-10-14 16:06:07 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-14 16:05:37 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 16:05:22 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 16:05:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 16:05:06 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-14 16:04:59 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:04:49 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-10-14 16:04:44 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-10-14 16:04:36 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-14 16:04:21 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 16:04:18 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-14 16:03:53 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-14 16:03:51 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:03:50 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-10-14 16:03:41 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-10-14 16:03:40 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.100 |  |
| 2026-10-14 16:03:39 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-10-14 16:02:51 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 16:02:48 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:02:29 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:01:57 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.067 |  |
| 2026-10-14 16:01:47 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-14 16:01:46 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-10-14 16:01:46 | Rathnapura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.073 |  |
| 2026-10-14 16:01:39 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 16:01:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-10-14 16:01:13 | Thalgahagoda (Nilwala Ganga) | 1.71 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 16:01:12 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-14 16:00:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 16:01:13 | Thalgahagoda (Nilwala Ganga) | 1.71 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 16:11:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-10-14 16:14:24 | Magura (Kalu Ganga) | 4.94 | 🟡 Alert | -0.034 |  |
| 2026-10-14 16:01:57 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.067 |  |
| 2026-10-14 16:06:42 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 1.083 | 🔺 Rising |
| 2026-10-14 16:04:18 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-14 16:06:07 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-14 16:05:06 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-14 16:01:39 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 16:02:51 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 16:05:37 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 16:05:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 16:05:22 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 16:04:21 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 16:03:51 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:00:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:33:16 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:04:59 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:02:29 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:02:48 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:07:54 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:10:36 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:09:56 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:08:21 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-14 16:12:11 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.009 |  |
| 2026-10-14 16:03:50 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-10-14 16:04:36 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-14 16:01:12 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-14 16:03:53 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-14 16:01:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-10-14 16:03:41 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-10-14 16:01:46 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-10-14 16:04:44 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-10-14 16:01:47 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-14 16:03:39 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-10-14 16:04:49 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-10-14 16:07:09 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.048 |  |
| 2026-10-14 16:01:46 | Rathnapura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.073 |  |
| 2026-10-14 16:03:40 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)