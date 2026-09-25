# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_08:17:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,400 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Norwood — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 08:17:05 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-25 08:12:34 | Rathnapura (Kalu Ganga) | 6.40 | 🟡 Alert | -0.035 |  |
| 2026-09-25 08:11:00 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:10:34 | Magura (Kalu Ganga) | 4.85 | 🟡 Alert | -0.029 |  |
| 2026-09-25 08:08:32 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-09-25 08:07:38 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:07:25 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.076 |  |
| 2026-09-25 08:06:51 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-09-25 08:06:21 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:05:35 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 08:05:27 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 08:05:25 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:05:25 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:04:59 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:04:57 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:04:47 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 08:04:20 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-09-25 08:04:19 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | -0.020 |  |
| 2026-09-25 08:04:12 | Glencourse (Kelani Ganga) | 14.40 | 🟢 Normal | -0.049 |  |
| 2026-09-25 08:04:04 | Hanwella (Kelani Ganga) | 6.31 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:03:49 | Baddegama (Gin Ganga) | 4.67 | 🟠 Minor Flood | 0.013 | 🔺 Rising |
| 2026-09-25 08:03:38 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:03:38 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:03:35 | Norwood (Kelani Ganga) | 1.60 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-25 08:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-25 08:03:28 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-25 08:03:10 | Thawalama (Gin Ganga) | 4.22 | 🟡 Alert | 0.000 |  |
| 2026-09-25 08:03:09 | Deraniyagala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.109 |  |
| 2026-09-25 08:02:28 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:02:25 | Nawalapitiya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.051 |  |
| 2026-09-25 08:02:24 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.097 |  |
| 2026-09-25 08:02:09 | Panadugama (Nilwala Ganga) | 6.54 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-25 08:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:01:33 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-25 08:01:22 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:01:22 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:00:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:00:35 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:00:19 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 08:00:13 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 08:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-25 08:03:49 | Baddegama (Gin Ganga) | 4.67 | 🟠 Minor Flood | 0.013 | 🔺 Rising |
| 2026-09-25 08:04:47 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 08:02:09 | Panadugama (Nilwala Ganga) | 6.54 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-25 08:03:35 | Norwood (Kelani Ganga) | 1.60 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-25 08:03:10 | Thawalama (Gin Ganga) | 4.22 | 🟡 Alert | 0.000 |  |
| 2026-09-25 08:10:34 | Magura (Kalu Ganga) | 4.85 | 🟡 Alert | -0.029 |  |
| 2026-09-25 08:12:34 | Rathnapura (Kalu Ganga) | 6.40 | 🟡 Alert | -0.035 |  |
| 2026-09-25 08:03:28 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-25 08:17:05 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-25 08:01:33 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-25 08:05:35 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 08:00:19 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 08:05:27 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 08:00:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:01:22 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:05:25 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:03:38 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:04:04 | Hanwella (Kelani Ganga) | 6.31 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:04:57 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:00:35 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:06:21 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:00:13 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:07:38 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:04:59 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:11:00 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:03:38 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:01:22 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:02:28 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 08:04:20 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-09-25 08:08:32 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-09-25 08:04:19 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | -0.020 |  |
| 2026-09-25 08:06:51 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-09-25 08:04:12 | Glencourse (Kelani Ganga) | 14.40 | 🟢 Normal | -0.049 |  |
| 2026-09-25 08:02:25 | Nawalapitiya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.051 |  |
| 2026-09-25 08:07:25 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.076 |  |
| 2026-09-25 08:02:24 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.097 |  |
| 2026-09-25 08:03:09 | Deraniyagala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)