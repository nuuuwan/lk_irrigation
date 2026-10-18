# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_20:21:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,562 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 20:21:51 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.008 |  |
| 2026-10-18 20:19:13 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:15:05 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | -0.021 |  |
| 2026-10-18 20:14:23 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:13:51 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.063 |  |
| 2026-10-18 20:13:19 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:08:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.027 |  |
| 2026-10-18 20:08:15 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 20:07:32 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-18 20:06:53 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.029 |  |
| 2026-10-18 20:06:48 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 20:06:43 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:06:14 | Norwood (Kelani Ganga) | 1.77 | 🟡 Alert | 0.033 | 🔺 Rising |
| 2026-10-18 20:05:39 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.032 |  |
| 2026-10-18 20:05:32 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-18 20:05:29 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:05:12 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-10-18 20:05:05 | Rathnapura (Kalu Ganga) | 4.63 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-10-18 20:05:04 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:04:47 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:04:24 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-10-18 20:04:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 20:03:25 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-10-18 20:03:24 | Deraniyagala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.489 |  |
| 2026-10-18 20:03:05 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | -0.060 |  |
| 2026-10-18 20:02:59 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-18 20:02:54 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-18 20:02:45 | Moragaswewa (Deduru Oya) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-10-18 20:02:29 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.101 |  |
| 2026-10-18 20:02:15 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 20:02:12 | Putupaula (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-18 20:02:09 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.070 |  |
| 2026-10-18 20:02:06 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:01:49 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-10-18 20:01:45 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:01:11 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-18 20:00:52 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 20:08:15 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 20:06:14 | Norwood (Kelani Ganga) | 1.77 | 🟡 Alert | 0.033 | 🔺 Rising |
| 2026-10-18 20:15:05 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | -0.021 |  |
| 2026-10-18 20:03:25 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | 0.465 | 🔺 Rising |
| 2026-10-18 20:05:05 | Rathnapura (Kalu Ganga) | 4.63 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-10-18 20:05:12 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-10-18 20:07:32 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-18 20:02:54 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-18 20:06:48 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 20:02:15 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 20:04:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 20:19:13 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:05:04 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:01:45 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:04:47 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:14:23 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:06:43 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:05:29 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:02:06 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 20:21:51 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.008 |  |
| 2026-10-18 20:04:24 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-10-18 20:02:59 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 20:05:32 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-18 20:01:11 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-18 20:02:12 | Putupaula (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-18 20:08:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.027 |  |
| 2026-10-18 20:06:53 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.029 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-18 20:02:45 | Moragaswewa (Deduru Oya) | 2.67 | 🟢 Normal | -0.030 |  |
| 2026-10-18 20:05:39 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.032 |  |
| 2026-10-18 20:00:52 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.041 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-18 20:03:05 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | -0.060 |  |
| 2026-10-18 20:01:49 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-10-18 20:13:51 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.063 |  |
| 2026-10-18 20:02:09 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.070 |  |
| 2026-10-18 20:02:29 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.101 |  |
| 2026-10-18 20:03:24 | Deraniyagala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.489 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)