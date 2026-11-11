# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_06:14:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,639 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 06:14:22 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-11-11 06:10:28 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 06:07:37 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.083 |  |
| 2026-11-11 06:07:24 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-11 06:06:54 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.029 |  |
| 2026-11-11 06:06:08 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | -0.473 |  |
| 2026-11-11 06:05:57 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.063 |  |
| 2026-11-11 06:05:47 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 06:04:52 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.087 |  |
| 2026-11-11 06:04:29 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.118 |  |
| 2026-11-11 06:04:15 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-11 06:04:08 | Badalgama (Maha Oya) | 4.45 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-11 06:04:02 | Hanwella (Kelani Ganga) | 4.94 | 🟢 Normal | -0.043 |  |
| 2026-11-11 06:03:38 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.045 |  |
| 2026-11-11 06:03:16 | Thawalama (Gin Ganga) | 3.21 | 🟢 Normal | -0.412 |  |
| 2026-11-11 06:02:56 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-11 06:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 06:02:52 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-11 06:02:43 | Moragaswewa (Deduru Oya) | 2.69 | 🟢 Normal | -0.108 |  |
| 2026-11-11 06:02:38 | Moraketiya (Walawe Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-11-11 06:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-11-11 06:02:19 | Giriulla (Maha Oya) | 3.42 | 🟢 Normal | -0.286 |  |
| 2026-11-11 06:02:15 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-11 06:02:09 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-11-11 06:02:07 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 06:02:06 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-11 06:02:05 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 06:01:48 | Dunamale (Aththanagalu Oya) | 4.26 | 🟡 Alert | -0.048 |  |
| 2026-11-11 06:01:40 | Magura (Kalu Ganga) | 3.62 | 🟢 Normal | -288.000 |  |
| 2026-11-11 06:01:38 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | -288.000 |  |
| 2026-11-11 06:01:36 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-11-11 06:01:27 | Glencourse (Kelani Ganga) | 12.55 | 🟢 Normal | -0.151 |  |
| 2026-11-11 06:01:24 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-11 06:01:22 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.013 |  |
| 2026-11-11 06:01:09 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | -0.101 |  |
| 2026-11-11 06:01:02 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-11 06:00:18 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 06:02:15 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-11 06:10:28 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 06:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 06:01:48 | Dunamale (Aththanagalu Oya) | 4.26 | 🟡 Alert | -0.048 |  |
| 2026-11-11 06:05:57 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.063 |  |
| 2026-11-11 06:04:08 | Badalgama (Maha Oya) | 4.45 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-11 06:01:24 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-11 06:01:02 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-11 06:02:05 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 06:02:07 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 06:02:52 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-11 06:05:47 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-11 06:14:22 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-11 06:04:15 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-11 06:02:56 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-11 06:02:06 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-11 06:02:38 | Moraketiya (Walawe Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-11-11 06:01:22 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.013 |  |
| 2026-11-11 06:07:24 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-11 06:00:18 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-11-11 06:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-11-11 06:06:54 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.029 |  |
| 2026-11-11 06:02:09 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-11-11 05:09:02 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-11-11 06:01:36 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-11-11 06:04:02 | Hanwella (Kelani Ganga) | 4.94 | 🟢 Normal | -0.043 |  |
| 2026-11-11 06:03:38 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.045 |  |
| 2026-11-11 06:07:37 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.083 |  |
| 2026-11-11 06:04:52 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.087 |  |
| 2026-11-11 06:01:09 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | -0.101 |  |
| 2026-11-11 06:02:43 | Moragaswewa (Deduru Oya) | 2.69 | 🟢 Normal | -0.108 |  |
| 2026-11-11 06:04:29 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.118 |  |
| 2026-11-11 06:01:27 | Glencourse (Kelani Ganga) | 12.55 | 🟢 Normal | -0.151 |  |
| 2026-11-11 06:02:19 | Giriulla (Maha Oya) | 3.42 | 🟢 Normal | -0.286 |  |
| 2026-11-11 06:03:16 | Thawalama (Gin Ganga) | 3.21 | 🟢 Normal | -0.412 |  |
| 2026-11-11 06:06:08 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | -0.473 |  |
| 2026-11-11 06:01:40 | Magura (Kalu Ganga) | 3.62 | 🟢 Normal | -288.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)