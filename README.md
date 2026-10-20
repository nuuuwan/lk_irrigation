# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_05:44:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,785 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 05:44:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | 1.161 | 🔺 Rising |
| 2026-10-20 05:44:07 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.006 |  |
| 2026-10-20 05:36:29 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.026 |  |
| 2026-10-20 05:22:47 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-20 05:14:43 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.026 |  |
| 2026-10-20 05:14:40 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-10-20 05:14:24 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-10-20 05:13:46 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.026 |  |
| 2026-10-20 05:10:19 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-20 05:09:24 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-20 05:08:33 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.005 |  |
| 2026-10-20 05:07:20 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 05:07:12 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-20 05:06:59 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:06:48 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:06:29 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.027 |  |
| 2026-10-20 05:06:01 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-10-20 05:06:00 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-10-20 05:05:53 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.066 |  |
| 2026-10-20 05:05:04 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-20 05:04:34 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:03:47 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.189 |  |
| 2026-10-20 05:03:34 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:03:29 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 04:00:34 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-20 05:44:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | 1.161 | 🔺 Rising |
| 2026-10-20 05:14:40 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-10-20 05:02:23 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.453 | 🔺 Rising |
| 2026-10-20 05:22:47 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-20 05:07:12 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-20 05:09:24 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-20 05:02:28 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 05:07:20 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 05:01:24 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 05:10:19 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-20 05:03:34 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:02:13 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:03:10 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-20 03:07:57 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:04:34 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:06:48 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:06:59 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 05:08:33 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.005 |  |
| 2026-10-20 05:44:07 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.006 |  |
| 2026-10-20 05:05:04 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-20 05:01:13 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-10-20 05:02:23 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-20 05:03:29 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-20 05:01:08 | Moragaswewa (Deduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-20 05:06:01 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-10-20 05:06:00 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-10-20 05:14:43 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.026 |  |
| 2026-10-20 05:36:29 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.026 |  |
| 2026-10-20 05:06:29 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.027 |  |
| 2026-10-20 04:21:07 | Panadugama (Nilwala Ganga) | 4.91 | 🟢 Normal | -0.031 |  |
| 2026-10-20 05:00:27 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.041 |  |
| 2026-10-20 05:01:37 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-20 05:05:53 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.066 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-20 05:03:47 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)