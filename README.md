# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_04:21:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,141 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 04:21:10 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | -0.037 |  |
| 2026-11-24 04:12:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.053 |  |
| 2026-11-24 04:12:06 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:12:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 04:11:43 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:11:14 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-24 04:09:25 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-24 04:08:33 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-24 04:08:09 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:07:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.066 |  |
| 2026-11-24 04:06:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 04:05:53 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | 0.522 | 🔺 Rising |
| 2026-11-24 04:05:39 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:05:35 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.205 |  |
| 2026-11-24 04:05:23 | Urawa (Nilwala Ganga) | 1.76 | 🟢 Normal | -0.128 |  |
| 2026-11-24 04:04:56 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-24 04:04:46 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | 0.788 | 🔺 Rising |
| 2026-11-24 04:03:59 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-24 04:03:31 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.139 |  |
| 2026-11-24 04:03:25 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:03:08 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | -0.092 |  |
| 2026-11-24 04:02:59 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:02:57 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:02:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:02:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-11-24 04:02:10 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 04:02:03 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.054 |  |
| 2026-11-24 04:02:03 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-11-24 04:01:45 | Giriulla (Maha Oya) | 4.44 | 🟢 Normal | -0.149 |  |
| 2026-11-24 04:01:36 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.083 |  |
| 2026-11-24 04:01:21 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:01:18 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-24 04:00:51 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:00:47 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 03:13:18 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-11-24 04:04:46 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | 0.788 | 🔺 Rising |
| 2026-11-24 04:05:53 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | 0.522 | 🔺 Rising |
| 2026-11-24 04:02:03 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-11-24 04:09:25 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-24 04:12:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 04:01:18 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-24 04:11:14 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-24 04:04:56 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-24 04:02:10 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 04:06:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 00:04:06 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.005 |  |
| 2026-11-24 04:00:51 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:01:21 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:02:59 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:02:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:08:09 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:03:25 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:12:06 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:05:39 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:48:29 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.006 |  |
| 2026-11-24 04:08:33 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-24 04:03:59 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-24 04:00:47 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 04:21:10 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | -0.037 |  |
| 2026-11-24 04:02:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-24 04:12:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.053 |  |
| 2026-11-24 04:02:03 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.054 |  |
| 2026-11-24 04:07:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.066 |  |
| 2026-11-24 04:01:36 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.083 |  |
| 2026-11-24 04:03:08 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | -0.092 |  |
| 2026-11-24 04:05:23 | Urawa (Nilwala Ganga) | 1.76 | 🟢 Normal | -0.128 |  |
| 2026-11-24 04:03:31 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.139 |  |
| 2026-11-24 04:01:45 | Giriulla (Maha Oya) | 4.44 | 🟢 Normal | -0.149 |  |
| 2026-11-24 04:05:35 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)