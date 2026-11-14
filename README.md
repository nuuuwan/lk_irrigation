# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_15:14:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,697 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 15:14:16 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.008 |  |
| 2026-11-14 15:13:02 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:09:40 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:09:35 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 15:07:59 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-14 15:07:35 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 15:06:59 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:05:53 | Baddegama (Gin Ganga) | 3.41 | 🟢 Normal | -0.051 |  |
| 2026-11-14 15:05:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-14 15:05:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-14 15:04:56 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.051 |  |
| 2026-11-14 15:04:21 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:55 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | -0.045 |  |
| 2026-11-14 15:03:35 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:29 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-14 15:03:21 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-11-14 15:03:18 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:08 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:08 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:03:06 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:04 | Panadugama (Nilwala Ganga) | 5.34 | 🟡 Alert | -0.032 |  |
| 2026-11-14 15:02:57 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 15:02:51 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:02:37 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-11-14 15:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | -0.101 |  |
| 2026-11-14 15:02:33 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:02:16 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:02:15 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-11-14 15:02:14 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:02:11 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 15:02:10 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:02:05 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-14 15:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 15:01:19 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.071 |  |
| 2026-11-14 15:01:18 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:01:01 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.024 |  |
| 2026-11-14 15:00:56 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:00:43 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | -0.041 |  |
| 2026-11-14 15:00:20 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 15:09:35 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 15:03:04 | Panadugama (Nilwala Ganga) | 5.34 | 🟡 Alert | -0.032 |  |
| 2026-11-14 15:05:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-14 15:03:29 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-14 15:02:05 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-14 15:07:59 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-14 15:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 15:02:57 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 15:02:11 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 15:03:08 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:02:10 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:02:33 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:02:51 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:13:02 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:06:59 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:35 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:06 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:18 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:00:56 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:09:40 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:14:16 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.008 |  |
| 2026-11-14 15:02:16 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:01:18 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:03:08 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:02:14 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:00:20 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:05:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-14 15:02:37 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-11-14 15:07:35 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 15:02:15 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-11-14 15:01:01 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.024 |  |
| 2026-11-14 15:00:43 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | -0.041 |  |
| 2026-11-14 15:03:21 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-11-14 15:03:55 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | -0.045 |  |
| 2026-11-14 15:05:53 | Baddegama (Gin Ganga) | 3.41 | 🟢 Normal | -0.051 |  |
| 2026-11-14 15:04:56 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.051 |  |
| 2026-11-14 15:01:19 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.071 |  |
| 2026-11-14 15:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)