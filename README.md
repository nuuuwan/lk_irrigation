# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_10:08:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,165 measurements** from **39** stations.
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
| 2026-10-08 10:08:15 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-10-08 10:07:55 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.074 |  |
| 2026-10-08 10:07:23 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:06:55 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.212 |  |
| 2026-10-08 10:06:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:06:40 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-08 10:06:34 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:05:53 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.069 |  |
| 2026-10-08 10:05:23 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-08 10:04:54 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-08 10:04:52 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:04:45 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.150 |  |
| 2026-10-08 10:04:28 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-10-08 10:04:15 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.181 |  |
| 2026-10-08 10:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | -0.025 |  |
| 2026-10-08 10:03:57 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.040 |  |
| 2026-10-08 10:03:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-08 10:02:59 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:02:45 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:02:40 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:02:39 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | -0.022 |  |
| 2026-10-08 10:02:32 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:02:18 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-08 10:02:07 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.059 |  |
| 2026-10-08 10:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-08 10:02:02 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.031 |  |
| 2026-10-08 10:01:50 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-10-08 10:01:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-08 10:01:33 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.029 |  |
| 2026-10-08 10:01:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:01:16 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-10-08 10:01:05 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-08 10:00:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 10:01:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-08 10:05:23 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-08 10:02:18 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-08 10:01:05 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-08 10:06:40 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-08 10:04:52 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:00:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:01:33 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:01:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 09:06:42 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:02:59 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:02:40 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:06:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:07:23 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:02:32 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:02:45 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:06:34 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 10:03:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-08 10:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-08 10:04:54 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-08 09:09:08 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.017 |  |
| 2026-10-08 10:01:16 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-10-08 09:10:07 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-10-08 10:02:39 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | -0.022 |  |
| 2026-10-08 10:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | -0.025 |  |
| 2026-10-08 10:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.029 |  |
| 2026-10-08 10:08:15 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-10-08 10:02:02 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.031 |  |
| 2026-10-08 10:03:57 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.040 |  |
| 2026-10-08 10:01:50 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-10-08 10:04:28 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-10-08 09:07:58 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-08 10:02:07 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.059 |  |
| 2026-10-08 10:05:53 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.069 |  |
| 2026-10-08 10:07:55 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.074 |  |
| 2026-10-08 09:01:22 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.081 |  |
| 2026-10-08 10:04:45 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.150 |  |
| 2026-10-08 10:04:15 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.181 |  |
| 2026-10-08 10:06:55 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)