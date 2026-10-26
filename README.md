# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_04:33:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 04:33:20 | Putupaula (Kalu Ganga) | 3.18 | 🟡 Alert | -66.667 |  |
| 2026-10-27 04:32:26 | Putupaula (Kalu Ganga) | 4.18 | 🟠 Minor Flood | -66.667 |  |
| 2026-10-27 04:28:15 | Nagalagam Street (Kelani Ganga) | 1.37 | 🟡 Alert | 0.000 |  |
| 2026-10-27 04:25:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.015 | 🔺 Rising |
| 2026-10-27 04:23:17 | Panadugama (Nilwala Ganga) | 6.55 | 🟠 Minor Flood | 0.027 | 🔺 Rising |
| 2026-10-27 04:18:44 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.008 | 🔺 Rising |
| 2026-10-27 04:16:56 | Moragaswewa (Deduru Oya) | 5.30 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-10-27 04:10:39 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.148 |  |
| 2026-10-27 04:08:03 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-10-27 04:06:36 | Baddegama (Gin Ganga) | 3.76 | 🟡 Alert | 0.058 | 🔺 Rising |
| 2026-10-27 04:06:06 | Rathnapura (Kalu Ganga) | 8.68 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 04:06:01 | Holombuwa (Kelani Ganga) | 2.21 | 🟢 Normal | -0.093 |  |
| 2026-10-27 04:05:43 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-27 04:05:29 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:04:49 | Pitabeddara (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.021 |  |
| 2026-10-27 04:04:38 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-27 04:04:36 | Norwood (Kelani Ganga) | 1.69 | 🟡 Alert | -0.050 |  |
| 2026-10-27 04:04:21 | Hanwella (Kelani Ganga) | 6.76 | 🟢 Normal | -0.019 |  |
| 2026-10-27 04:04:01 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:03:56 | Urawa (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.128 |  |
| 2026-10-27 04:03:29 | Giriulla (Maha Oya) | 4.82 | 🟢 Normal | -0.189 |  |
| 2026-10-27 04:03:14 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:02:58 | Ellagawa (Kalu Ganga) | 9.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 04:02:35 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-27 04:02:34 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-27 04:02:34 | Glencourse (Kelani Ganga) | 14.64 | 🟢 Normal | -0.170 |  |
| 2026-10-27 04:02:27 | Dunamale (Aththanagalu Oya) | 4.70 | 🟠 Minor Flood | 0.026 | 🔺 Rising |
| 2026-10-27 04:02:12 | Badalgama (Maha Oya) | 5.69 | 🟡 Alert | -0.041 |  |
| 2026-10-27 04:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.051 |  |
| 2026-10-27 04:02:10 | Thawalama (Gin Ganga) | 5.30 | 🟡 Alert | -0.029 |  |
| 2026-10-27 04:02:09 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-27 04:01:14 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:01:14 | Magura (Kalu Ganga) | 5.26 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 04:00:43 | Moraketiya (Walawe Ganga) | 2.42 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-27 04:00:38 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 04:23:17 | Panadugama (Nilwala Ganga) | 6.55 | 🟠 Minor Flood | 0.027 | 🔺 Rising |
| 2026-10-27 04:02:27 | Dunamale (Aththanagalu Oya) | 4.70 | 🟠 Minor Flood | 0.026 | 🔺 Rising |
| 2026-10-27 04:25:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.015 | 🔺 Rising |
| 2026-10-27 04:06:06 | Rathnapura (Kalu Ganga) | 8.68 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 04:06:36 | Baddegama (Gin Ganga) | 3.76 | 🟡 Alert | 0.058 | 🔺 Rising |
| 2026-10-27 04:16:56 | Moragaswewa (Deduru Oya) | 5.30 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-10-27 04:01:14 | Magura (Kalu Ganga) | 5.26 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 04:18:44 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.008 | 🔺 Rising |
| 2026-10-27 04:28:15 | Nagalagam Street (Kelani Ganga) | 1.37 | 🟡 Alert | 0.000 |  |
| 2026-10-27 04:02:10 | Thawalama (Gin Ganga) | 5.30 | 🟡 Alert | -0.029 |  |
| 2026-10-27 04:02:12 | Badalgama (Maha Oya) | 5.69 | 🟡 Alert | -0.041 |  |
| 2026-10-27 04:04:36 | Norwood (Kelani Ganga) | 1.69 | 🟡 Alert | -0.050 |  |
| 2026-10-27 04:33:20 | Putupaula (Kalu Ganga) | 3.18 | 🟡 Alert | -66.667 |  |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-27 04:05:43 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 04:02:35 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-27 04:00:43 | Moraketiya (Walawe Ganga) | 2.42 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-27 04:02:58 | Ellagawa (Kalu Ganga) | 9.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 04:04:01 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:03:14 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:05:29 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:01:14 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:08:03 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-10-27 04:04:38 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-27 04:02:09 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-27 03:02:46 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-27 04:04:21 | Hanwella (Kelani Ganga) | 6.76 | 🟢 Normal | -0.019 |  |
| 2026-10-27 04:02:34 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-27 04:00:38 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-10-27 04:04:49 | Pitabeddara (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.021 |  |
| 2026-10-27 04:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.051 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-27 04:06:01 | Holombuwa (Kelani Ganga) | 2.21 | 🟢 Normal | -0.093 |  |
| 2026-10-27 04:03:56 | Urawa (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.128 |  |
| 2026-10-27 04:10:39 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.148 |  |
| 2026-10-27 03:05:23 | Peradeniya (Mahaweli Ganga) | 4.24 | 🟢 Normal | -0.151 |  |
| 2026-10-27 04:02:34 | Glencourse (Kelani Ganga) | 14.64 | 🟢 Normal | -0.170 |  |
| 2026-10-27 04:03:29 | Giriulla (Maha Oya) | 4.82 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)