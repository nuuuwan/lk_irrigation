# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_22:10:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,534 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 22:10:15 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.028 |  |
| 2026-10-19 22:09:58 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:07:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-19 22:07:45 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:07:09 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:06:11 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-10-19 22:06:09 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-19 22:05:43 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | -1.325 |  |
| 2026-10-19 22:05:33 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-19 22:05:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:04:43 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.067 |  |
| 2026-10-19 22:04:17 | Panadugama (Nilwala Ganga) | 5.00 | 🟡 Alert | -0.051 |  |
| 2026-10-19 22:03:39 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-10-19 22:03:29 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.039 |  |
| 2026-10-19 22:03:26 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-19 22:03:23 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:03:20 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.301 |  |
| 2026-10-19 22:02:58 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 22:02:56 | Kithulgala (Kelani Ganga) | 2.56 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-10-19 22:02:52 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-10-19 22:02:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-19 22:02:43 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 22:02:41 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-19 22:02:25 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.041 |  |
| 2026-10-19 22:01:34 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-19 22:01:28 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-10-19 22:01:03 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | -0.054 |  |
| 2026-10-19 22:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.092 |  |
| 2026-10-19 22:00:05 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.143 |  |
| 2026-10-19 21:26:43 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 21:16:08 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-19 22:04:17 | Panadugama (Nilwala Ganga) | 5.00 | 🟡 Alert | -0.051 |  |
| 2026-10-19 22:02:56 | Kithulgala (Kelani Ganga) | 2.56 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-10-19 22:06:09 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-19 21:03:28 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-19 22:01:34 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-19 22:05:33 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-19 22:02:43 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 22:02:58 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 21:02:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:03:23 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:09:58 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:07:45 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:05:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:07:09 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 22:06:11 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-10-19 22:02:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-19 22:02:41 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-19 21:06:30 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-10-19 22:03:26 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-19 22:02:52 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-10-19 22:03:39 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-10-19 22:10:15 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.028 |  |
| 2026-10-19 22:07:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-19 22:01:28 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-10-19 21:11:12 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.035 |  |
| 2026-10-19 22:03:29 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.039 |  |
| 2026-10-19 21:03:11 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.039 |  |
| 2026-10-19 22:02:25 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.041 |  |
| 2026-10-19 22:01:03 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | -0.054 |  |
| 2026-10-19 21:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.059 |  |
| 2026-10-19 22:04:43 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.067 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-19 22:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.092 |  |
| 2026-10-19 22:00:05 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.143 |  |
| 2026-10-19 22:03:20 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.301 |  |
| 2026-10-19 22:05:43 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | -1.325 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)