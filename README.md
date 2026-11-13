# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_13:29:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,726 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 13:29:09 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.018 |  |
| 2026-11-13 13:17:00 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | -0.016 |  |
| 2026-11-13 13:14:54 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.017 |  |
| 2026-11-13 13:12:41 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.147 |  |
| 2026-11-13 13:11:10 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -3.981 |  |
| 2026-11-13 13:10:51 | Moraketiya (Walawe Ganga) | 3.77 | 🟡 Alert | -0.009 |  |
| 2026-11-13 13:09:21 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.019 |  |
| 2026-11-13 13:07:39 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:07:24 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.027 |  |
| 2026-11-13 13:07:10 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.039 |  |
| 2026-11-13 13:07:03 | Thaldena (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.037 |  |
| 2026-11-13 13:06:45 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.091 |  |
| 2026-11-13 13:06:23 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | -0.019 |  |
| 2026-11-13 13:05:40 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 13:05:25 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-13 13:05:06 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.041 |  |
| 2026-11-13 13:04:22 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:04:17 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:04:10 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-13 13:03:37 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.079 |  |
| 2026-11-13 13:03:30 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:03:20 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.040 |  |
| 2026-11-13 13:02:52 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.033 |  |
| 2026-11-13 13:02:47 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.029 |  |
| 2026-11-13 13:02:35 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-13 13:02:34 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-13 13:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.020 |  |
| 2026-11-13 13:02:18 | Thanamalwila (Kirindi Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 13:02:07 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.049 |  |
| 2026-11-13 13:02:05 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:53 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:44 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.021 |  |
| 2026-11-13 13:01:41 | Ellagawa (Kalu Ganga) | 7.87 | 🟢 Normal | -0.051 |  |
| 2026-11-13 13:01:33 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:20 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-11-13 13:01:17 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:04 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:00:58 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.063 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 13:05:40 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 13:05:25 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-13 13:10:51 | Moraketiya (Walawe Ganga) | 3.77 | 🟡 Alert | -0.009 |  |
| 2026-11-13 13:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.020 |  |
| 2026-11-13 13:00:58 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-13 13:02:34 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-13 13:02:18 | Thanamalwila (Kirindi Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 13:02:35 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-13 13:04:10 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-13 13:03:30 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:07:39 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:04 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:02:05 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:53 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:04:22 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:04:17 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:33 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:01:17 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-13 13:17:00 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | -0.016 |  |
| 2026-11-13 13:14:54 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.017 |  |
| 2026-11-13 13:29:09 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.018 |  |
| 2026-11-13 13:09:21 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.019 |  |
| 2026-11-13 13:06:23 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | -0.019 |  |
| 2026-11-13 13:01:20 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-11-13 13:01:44 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.021 |  |
| 2026-11-13 13:07:24 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.027 |  |
| 2026-11-13 13:02:47 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.029 |  |
| 2026-11-13 13:02:52 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.033 |  |
| 2026-11-13 13:07:03 | Thaldena (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.037 |  |
| 2026-11-13 13:07:10 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.039 |  |
| 2026-11-13 13:03:20 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.040 |  |
| 2026-11-13 13:05:06 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.041 |  |
| 2026-11-13 13:02:07 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.049 |  |
| 2026-11-13 13:01:41 | Ellagawa (Kalu Ganga) | 7.87 | 🟢 Normal | -0.051 |  |
| 2026-11-13 13:03:37 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.079 |  |
| 2026-11-13 13:06:45 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.091 |  |
| 2026-11-13 13:12:41 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.147 |  |
| 2026-11-13 13:11:10 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -3.981 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)