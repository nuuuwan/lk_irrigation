# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_04:35:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,045 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 04:35:18 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | -0.007 |  |
| 2026-10-17 04:29:30 | Urawa (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.024 |  |
| 2026-10-17 04:26:51 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | -0.037 |  |
| 2026-10-17 04:17:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-10-17 04:16:24 | Pitabeddara (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-17 04:12:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | -0.030 |  |
| 2026-10-17 04:12:22 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.018 |  |
| 2026-10-17 04:12:15 | Magura (Kalu Ganga) | 3.91 | 🟢 Normal | -0.041 |  |
| 2026-10-17 04:09:00 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:07:49 | Rathnapura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.128 |  |
| 2026-10-17 04:07:14 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.029 |  |
| 2026-10-17 04:07:06 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:06:13 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:05:00 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:04:45 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-10-17 04:04:33 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.061 |  |
| 2026-10-17 04:04:25 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | -0.101 |  |
| 2026-10-17 04:04:10 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.050 |  |
| 2026-10-17 04:03:50 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.020 |  |
| 2026-10-17 04:03:36 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-10-17 04:03:19 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-10-17 04:02:53 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-10-17 04:02:08 | Hanwella (Kelani Ganga) | 3.71 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-10-17 04:02:07 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-17 04:02:05 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-17 04:01:59 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-10-17 04:01:58 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 04:01:40 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-17 04:01:26 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 04:00:40 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-10-17 04:00:29 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | -0.022 |  |
| 2026-10-17 04:00:17 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 03:12:08 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 03:07:33 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-17 04:03:50 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.020 |  |
| 2026-10-17 04:12:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | -0.030 |  |
| 2026-10-17 04:02:08 | Hanwella (Kelani Ganga) | 3.71 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-10-17 04:02:07 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-17 04:02:05 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-17 04:16:24 | Pitabeddara (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-17 04:01:40 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-17 03:09:21 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-17 04:01:58 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 04:01:26 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 04:07:06 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:09:00 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:06:13 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:05:00 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:35:18 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | -0.007 |  |
| 2026-10-17 04:17:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-10-17 04:12:22 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.018 |  |
| 2026-10-17 04:00:17 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-10-17 04:02:53 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-10-17 04:03:19 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-10-17 04:00:40 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-10-17 04:00:29 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | -0.022 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-17 04:29:30 | Urawa (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.024 |  |
| 2026-10-17 04:07:14 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.029 |  |
| 2026-10-17 04:01:59 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-10-17 04:26:51 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | -0.037 |  |
| 2026-10-17 03:04:33 | Moragaswewa (Deduru Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-10-17 04:04:45 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-10-17 04:12:15 | Magura (Kalu Ganga) | 3.91 | 🟢 Normal | -0.041 |  |
| 2026-10-17 04:03:36 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-10-17 04:04:10 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.050 |  |
| 2026-10-17 04:04:33 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.061 |  |
| 2026-10-17 04:04:25 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | -0.101 |  |
| 2026-10-17 04:07:49 | Rathnapura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)