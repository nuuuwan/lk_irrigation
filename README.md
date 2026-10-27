# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_23:27:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,771 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 23:27:32 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:20:02 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.016 |  |
| 2026-10-27 23:13:48 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-10-27 23:09:48 | Putupaula (Kalu Ganga) | 3.43 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-27 23:09:37 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-10-27 23:07:44 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-27 23:07:39 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:06:53 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 23:06:50 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-10-27 23:06:19 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:06:18 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-10-27 23:05:35 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-27 23:05:27 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -0.015 |  |
| 2026-10-27 23:05:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.74 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 23:05:04 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.056 |  |
| 2026-10-27 23:04:57 | Ellagawa (Kalu Ganga) | 10.31 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-27 23:04:51 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 23:04:05 | Giriulla (Maha Oya) | 2.83 | 🟢 Normal | -0.069 |  |
| 2026-10-27 23:04:02 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:03:45 | Rathnapura (Kalu Ganga) | 7.34 | 🟡 Alert | -0.091 |  |
| 2026-10-27 23:03:44 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:03:29 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-10-27 23:03:29 | Dunamale (Aththanagalu Oya) | 4.61 | 🟠 Minor Flood | -0.039 |  |
| 2026-10-27 23:02:48 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.062 |  |
| 2026-10-27 23:02:30 | Hanwella (Kelani Ganga) | 4.91 | 🟢 Normal | -0.090 |  |
| 2026-10-27 23:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-10-27 23:02:18 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.020 |  |
| 2026-10-27 23:01:37 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:01:05 | Moragaswewa (Deduru Oya) | 4.11 | 🟢 Normal | -0.140 |  |
| 2026-10-27 23:00:59 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.058 |  |
| 2026-10-27 23:00:52 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:00:08 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 23:05:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.74 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 23:06:53 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 23:04:51 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 23:05:27 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -0.015 |  |
| 2026-10-27 23:03:29 | Dunamale (Aththanagalu Oya) | 4.61 | 🟠 Minor Flood | -0.039 |  |
| 2026-10-27 23:09:48 | Putupaula (Kalu Ganga) | 3.43 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-27 23:04:57 | Ellagawa (Kalu Ganga) | 10.31 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-27 23:00:59 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.058 |  |
| 2026-10-27 23:03:45 | Rathnapura (Kalu Ganga) | 7.34 | 🟡 Alert | -0.091 |  |
| 2026-10-27 23:05:35 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-27 22:04:17 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-27 23:07:44 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-27 23:00:08 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-27 22:47:53 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:07:39 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:00:52 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:01:37 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:27:32 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:03:44 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-27 22:05:19 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:04:02 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:06:19 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-27 23:13:48 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-27 23:09:37 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-10-27 23:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-10-27 22:00:57 | Horowpothana (Yan Oya) | 3.39 | 🟢 Normal | -0.010 |  |
| 2026-10-27 23:20:02 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.016 |  |
| 2026-10-27 23:06:50 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-10-27 23:02:18 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.020 |  |
| 2026-10-27 23:06:18 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-10-27 23:03:29 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-10-27 23:05:04 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.056 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-27 23:02:48 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.062 |  |
| 2026-10-27 23:04:05 | Giriulla (Maha Oya) | 2.83 | 🟢 Normal | -0.069 |  |
| 2026-10-27 23:02:30 | Hanwella (Kelani Ganga) | 4.91 | 🟢 Normal | -0.090 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-27 23:01:05 | Moragaswewa (Deduru Oya) | 4.11 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)