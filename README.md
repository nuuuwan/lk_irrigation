# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_23:33:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,997 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 23:33:24 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.071 |  |
| 2026-11-14 23:28:18 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:10:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:10:06 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.036 |  |
| 2026-11-14 23:09:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.125 |  |
| 2026-11-14 23:08:18 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-14 23:08:06 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.037 |  |
| 2026-11-14 23:07:08 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 23:06:01 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -0.040 |  |
| 2026-11-14 23:05:30 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:05:24 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.110 |  |
| 2026-11-14 23:05:17 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:05:14 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.097 |  |
| 2026-11-14 23:04:53 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.024 |  |
| 2026-11-14 23:04:45 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:04:40 | Wellawaya (Kirindi Oya) | 1.97 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-14 23:04:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:04:27 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:04:09 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-11-14 23:03:48 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:03:47 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2026-11-14 23:03:38 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.021 |  |
| 2026-11-14 23:03:32 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:03:20 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:03:16 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:02:25 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:16 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:05 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:01 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:01:22 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:01:08 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 23:00:11 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:49:01 | Panadugama (Nilwala Ganga) | 5.13 | 🟡 Alert | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 23:07:08 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 23:05:24 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.110 |  |
| 2026-11-14 23:04:40 | Wellawaya (Kirindi Oya) | 1.97 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-14 23:08:18 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 23:01:08 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 23:02:05 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:16 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:04:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:05:17 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:03:20 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:28:18 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:25 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:00:11 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:10:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:01:22 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:02:01 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:05:30 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:03:48 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-14 22:08:44 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:04:27 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-14 23:03:16 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:04:45 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-14 23:03:32 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-14 22:00:53 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-11-14 22:18:29 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.016 |  |
| 2026-11-14 23:03:47 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2026-11-14 23:03:38 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.021 |  |
| 2026-11-14 23:04:53 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.024 |  |
| 2026-11-14 23:10:06 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.036 |  |
| 2026-11-14 23:08:06 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.037 |  |
| 2026-11-14 23:06:01 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -0.040 |  |
| 2026-11-14 23:04:09 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.040 |  |
| 2026-11-14 23:33:24 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.071 |  |
| 2026-11-14 23:05:14 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.097 |  |
| 2026-11-14 23:09:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)