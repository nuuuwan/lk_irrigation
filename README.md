# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_02:18:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **237,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 02:18:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.016 |  |
| 2026-08-19 02:16:50 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-08-19 02:15:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-08-19 02:11:04 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-08-19 02:09:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-19 02:06:48 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:57 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:40 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-08-19 02:04:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:33 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:33 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -252.000 |  |
| 2026-08-19 02:04:32 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -252.000 |  |
| 2026-08-19 02:04:31 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:18 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:17 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.053 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 02:15:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-08-19 02:04:17 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-19 02:09:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-19 02:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-18 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:01:05 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:01:33 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:02:20 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:01:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:31 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:02:19 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 18:06:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:03:45 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:33 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:18 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:02:18 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:57 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:04:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-19 01:07:42 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:03:19 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-18 18:04:43 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:06:48 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:00:40 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:01:14 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:02:26 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:03:23 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-08-19 02:03:45 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-19 02:16:50 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-08-19 02:02:20 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-08-19 01:00:57 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-08-19 02:04:40 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-08-19 01:39:08 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.015 |  |
| 2026-08-19 02:18:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.016 |  |
| 2026-08-19 02:11:04 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-08-19 02:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-08-19 02:02:35 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.049 |  |
| 2026-08-19 00:11:08 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.117 |  |
| 2026-08-19 02:04:33 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)