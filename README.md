# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_00:22:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,427 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 00:22:51 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | -0.082 |  |
| 2026-11-11 00:22:08 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:20:50 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.139 |  |
| 2026-11-11 00:15:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 00:14:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 00:13:39 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.042 |  |
| 2026-11-11 00:12:57 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:10:07 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-11 00:09:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.051 |  |
| 2026-11-11 00:08:50 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 00:07:46 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.029 |  |
| 2026-11-11 00:07:35 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-11 00:07:24 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 00:07:19 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-11 00:06:53 | Rathnapura (Kalu Ganga) | 5.56 | 🟡 Alert | -0.116 |  |
| 2026-11-11 00:05:16 | Magura (Kalu Ganga) | 4.13 | 🟡 Alert | -0.048 |  |
| 2026-11-11 00:04:45 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.060 |  |
| 2026-11-11 00:04:29 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.064 |  |
| 2026-11-11 00:04:18 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-11 00:03:47 | Moraketiya (Walawe Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:03:46 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-11 00:03:24 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:03:19 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-11-11 00:03:15 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:03:08 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.086 |  |
| 2026-11-11 00:02:44 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:02:27 | Thawalama (Gin Ganga) | 4.43 | 🟡 Alert | 0.092 | 🔺 Rising |
| 2026-11-11 00:02:18 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-11 00:02:09 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | -0.041 |  |
| 2026-11-11 00:01:45 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.059 |  |
| 2026-11-11 00:01:39 | Dunamale (Aththanagalu Oya) | 4.41 | 🟠 Minor Flood | -0.034 |  |
| 2026-11-11 00:01:32 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:01:12 | Peradeniya (Mahaweli Ganga) | 5.31 | 🟡 Alert | -0.196 |  |
| 2026-11-11 00:01:09 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.072 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 00:02:18 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-11 00:08:50 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 00:07:24 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 00:15:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 00:01:39 | Dunamale (Aththanagalu Oya) | 4.41 | 🟠 Minor Flood | -0.034 |  |
| 2026-11-11 00:02:27 | Thawalama (Gin Ganga) | 4.43 | 🟡 Alert | 0.092 | 🔺 Rising |
| 2026-11-11 00:05:16 | Magura (Kalu Ganga) | 4.13 | 🟡 Alert | -0.048 |  |
| 2026-11-11 00:06:53 | Rathnapura (Kalu Ganga) | 5.56 | 🟡 Alert | -0.116 |  |
| 2026-11-11 00:01:12 | Peradeniya (Mahaweli Ganga) | 5.31 | 🟡 Alert | -0.196 |  |
| 2026-11-11 00:03:19 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-11-11 00:10:07 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-11 00:03:46 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-11 00:04:18 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-11 00:07:19 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 22:02:07 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-11 00:01:32 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:22:08 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:12:57 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:03:15 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-11 00:02:44 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:03:47 | Moraketiya (Walawe Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:03:24 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:07:35 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-10 23:02:36 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-11 00:07:46 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.029 |  |
| 2026-11-11 00:02:09 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | -0.041 |  |
| 2026-11-11 00:13:39 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.042 |  |
| 2026-11-11 00:09:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.051 |  |
| 2026-11-11 00:01:45 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.059 |  |
| 2026-11-11 00:04:45 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.060 |  |
| 2026-11-11 00:04:29 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.064 |  |
| 2026-11-11 00:01:09 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.072 |  |
| 2026-11-11 00:22:51 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | -0.082 |  |
| 2026-11-11 00:03:08 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.086 |  |
| 2026-11-11 00:20:50 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.139 |  |
| 2026-11-10 23:07:02 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | -0.393 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)