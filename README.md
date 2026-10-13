# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_11:09:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 11:09:42 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | -0.033 |  |
| 2026-10-13 11:08:48 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:08:02 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.135 |  |
| 2026-10-13 11:07:52 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.104 |  |
| 2026-10-13 11:07:01 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.103 |  |
| 2026-10-13 11:06:42 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-13 11:06:29 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.243 |  |
| 2026-10-13 11:06:14 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:05:56 | Panadugama (Nilwala Ganga) | 6.03 | 🟠 Minor Flood | -0.065 |  |
| 2026-10-13 11:05:41 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:05:24 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:05:06 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:05:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | -0.033 |  |
| 2026-10-13 11:04:52 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:04:50 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:04:13 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-10-13 11:03:57 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:03:34 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.062 |  |
| 2026-10-13 11:03:15 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:03:10 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:03:10 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.052 |  |
| 2026-10-13 11:02:50 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.051 |  |
| 2026-10-13 11:02:36 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:02:34 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.026 |  |
| 2026-10-13 11:02:23 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-10-13 11:02:17 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:02:17 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-13 11:02:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:02:02 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.122 |  |
| 2026-10-13 11:02:01 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:01:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 11:01:50 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-13 11:01:50 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:01:14 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:00:55 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:00:52 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.104 |  |
| 2026-10-13 11:00:10 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 11:05:56 | Panadugama (Nilwala Ganga) | 6.03 | 🟠 Minor Flood | -0.065 |  |
| 2026-10-13 11:01:50 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-13 11:05:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | -0.033 |  |
| 2026-10-13 11:01:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 11:06:42 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-13 11:02:17 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:01:50 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:03:57 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:00:55 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:03:15 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:08:48 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:04:52 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:04:50 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:02:01 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:05:24 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:06:14 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:05:06 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-13 11:01:14 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:02:36 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:02:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:05:41 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:00:10 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:03:10 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-13 11:04:13 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-10-13 11:02:17 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-13 10:02:34 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.024 |  |
| 2026-10-13 11:02:34 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.026 |  |
| 2026-10-13 11:09:42 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | -0.033 |  |
| 2026-10-13 11:02:23 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-10-13 11:02:50 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.051 |  |
| 2026-10-13 11:03:10 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.052 |  |
| 2026-10-13 11:03:34 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.062 |  |
| 2026-10-13 11:07:01 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.103 |  |
| 2026-10-13 11:07:52 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.104 |  |
| 2026-10-13 11:00:52 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.104 |  |
| 2026-10-13 11:02:02 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.122 |  |
| 2026-10-13 11:08:02 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.135 |  |
| 2026-10-13 11:06:29 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.243 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)