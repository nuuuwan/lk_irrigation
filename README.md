# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_18:11:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 18:11:24 | Urawa (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.110 |  |
| 2026-10-09 18:11:18 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 18:09:50 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.140 |  |
| 2026-10-09 18:08:14 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.747 | 🔺 Rising |
| 2026-10-09 18:07:26 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-09 18:06:48 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | 0.644 | 🔺 Rising |
| 2026-10-09 18:05:42 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | -0.039 |  |
| 2026-10-09 18:05:28 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:04:55 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-10-09 18:04:53 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-09 18:04:37 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.040 |  |
| 2026-10-09 18:04:28 | Norwood (Kelani Ganga) | 1.62 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-09 18:04:17 | Giriulla (Maha Oya) | 2.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 18:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | -0.078 |  |
| 2026-10-09 18:03:46 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:03:37 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-09 18:03:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.090 |  |
| 2026-10-09 18:02:56 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | -0.106 |  |
| 2026-10-09 18:02:54 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:02:50 | Badalgama (Maha Oya) | 3.95 | 🟢 Normal | -0.031 |  |
| 2026-10-09 18:02:41 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-09 18:02:30 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.033 |  |
| 2026-10-09 18:02:24 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | 0.678 | 🔺 Rising |
| 2026-10-09 18:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:56 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:54 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-09 18:01:53 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:01:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 18:01:37 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:33 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-10-09 18:01:29 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 18:01:11 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.075 |  |
| 2026-10-09 18:01:09 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:00:51 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:00:41 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 18:04:28 | Norwood (Kelani Ganga) | 1.62 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-09 18:08:14 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.747 | 🔺 Rising |
| 2026-10-09 18:02:24 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | 0.678 | 🔺 Rising |
| 2026-10-09 18:06:48 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | 0.644 | 🔺 Rising |
| 2026-10-09 18:07:26 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-09 18:02:41 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-09 18:03:37 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-09 18:01:29 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 18:04:17 | Giriulla (Maha Oya) | 2.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 18:04:53 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-09 18:01:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 18:01:53 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:00:51 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:37 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:05:28 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:56 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:02:54 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:03:46 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:11:18 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:54 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-09 18:01:33 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-10-09 18:04:55 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-10-09 18:01:09 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-10-09 18:00:41 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.024 |  |
| 2026-10-09 18:02:50 | Badalgama (Maha Oya) | 3.95 | 🟢 Normal | -0.031 |  |
| 2026-10-09 18:02:30 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.033 |  |
| 2026-10-09 18:05:42 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | -0.039 |  |
| 2026-10-09 18:04:37 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.040 |  |
| 2026-10-09 18:01:11 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.075 |  |
| 2026-10-09 18:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | -0.078 |  |
| 2026-10-09 18:03:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.090 |  |
| 2026-10-09 18:02:56 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | -0.106 |  |
| 2026-10-09 18:11:24 | Urawa (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.110 |  |
| 2026-10-09 18:09:50 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)