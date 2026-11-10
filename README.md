# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_00:03:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,408 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-11-10 23:40:29 | Magura (Kalu Ganga) | 4.15 | 🟡 Alert | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 00:02:18 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-10 23:04:11 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 22:07:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | -0.009 |  |
| 2026-11-10 23:01:25 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-11 00:01:39 | Dunamale (Aththanagalu Oya) | 4.41 | 🟠 Minor Flood | -0.034 |  |
| 2026-11-11 00:02:27 | Thawalama (Gin Ganga) | 4.43 | 🟡 Alert | 0.092 | 🔺 Rising |
| 2026-11-10 23:40:29 | Magura (Kalu Ganga) | 4.15 | 🟡 Alert | -0.007 |  |
| 2026-11-10 23:04:51 | Rathnapura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.070 |  |
| 2026-11-11 00:01:12 | Peradeniya (Mahaweli Ganga) | 5.31 | 🟡 Alert | -0.196 |  |
| 2026-11-11 00:03:19 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-11-10 23:03:44 | Glencourse (Kelani Ganga) | 13.11 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-11 00:03:46 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-10 23:02:47 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 22:02:07 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-11 00:01:32 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:01:13 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-11 00:03:15 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:08:56 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:25:23 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.003 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-11 00:02:44 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:05:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:03:47 | Moraketiya (Walawe Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-11-11 00:03:24 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:06:08 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-11-10 23:02:36 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-10 23:02:39 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | -0.034 |  |
| 2026-11-11 00:02:09 | Kuda Oya (Kirindi Oya) | 2.04 | 🟢 Normal | -0.041 |  |
| 2026-11-11 00:01:45 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.059 |  |
| 2026-11-10 23:10:45 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.061 |  |
| 2026-11-11 00:01:09 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.072 |  |
| 2026-11-10 23:02:01 | Moragaswewa (Deduru Oya) | 3.46 | 🟢 Normal | -0.080 |  |
| 2026-11-10 23:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.080 |  |
| 2026-11-11 00:03:08 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.086 |  |
| 2026-11-10 23:08:20 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.110 |  |
| 2026-11-10 23:07:02 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | -0.393 |  |
| 2026-11-10 23:05:01 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)