# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_21:10:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,411 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 21:10:30 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | -0.009 |  |
| 2026-10-30 21:09:32 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:06:54 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:05:57 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:05:05 | Putupaula (Kalu Ganga) | 3.14 | 🟡 Alert | -0.020 |  |
| 2026-10-30 21:04:56 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:04:45 | Panadugama (Nilwala Ganga) | 5.13 | 🟡 Alert | -0.024 |  |
| 2026-10-30 21:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | -0.039 |  |
| 2026-10-30 21:04:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.091 |  |
| 2026-10-30 21:04:07 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-30 21:03:55 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-30 21:03:43 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:03:34 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 21:03:16 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 21:03:09 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-30 21:03:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:03:05 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 21:02:53 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:02:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:02:48 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.034 |  |
| 2026-10-30 21:02:48 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | -45.000 |  |
| 2026-10-30 21:02:44 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | -45.000 |  |
| 2026-10-30 21:02:38 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-30 21:02:22 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:02:16 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-10-30 21:02:16 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:02:14 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:02:10 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:01:51 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:01:50 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-10-30 21:01:49 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 21:01:37 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:00:38 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-30 21:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:00:16 | Padiyathalawa (Maduru Oya) | 1.66 | 🟢 Normal | -0.094 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 21:03:05 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 21:05:05 | Putupaula (Kalu Ganga) | 3.14 | 🟡 Alert | -0.020 |  |
| 2026-10-30 21:04:45 | Panadugama (Nilwala Ganga) | 5.13 | 🟡 Alert | -0.024 |  |
| 2026-10-30 21:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | -0.039 |  |
| 2026-10-30 21:04:07 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-30 21:03:09 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-30 21:00:38 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-30 21:03:55 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-30 21:03:16 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 21:01:49 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 21:03:34 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 21:03:43 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:02:22 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:05:57 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:02:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:01:37 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:04:56 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:02:53 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:03:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:01:51 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-30 21:10:30 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | -0.009 |  |
| 2026-10-30 21:06:54 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:02:14 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:02:16 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 20:00:18 | Pitabeddara (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:09:32 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:02:10 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-10-30 21:01:50 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-30 21:02:38 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-30 21:02:16 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-10-30 21:02:48 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.034 |  |
| 2026-10-30 20:01:16 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -0.042 |  |
| 2026-10-30 21:04:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.091 |  |
| 2026-10-30 21:00:16 | Padiyathalawa (Maduru Oya) | 1.66 | 🟢 Normal | -0.094 |  |
| 2026-10-30 21:02:48 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | -45.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)