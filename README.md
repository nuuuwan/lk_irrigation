# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_16:17:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,040 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 16:17:38 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | -0.042 |  |
| 2026-11-11 16:14:45 | Magura (Kalu Ganga) | 3.38 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2026-11-11 16:13:59 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-11 16:11:40 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-11 16:09:19 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-11-11 16:08:40 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:08:20 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 16:07:58 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | -0.125 |  |
| 2026-11-11 16:07:11 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-11-11 16:06:27 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | -0.039 |  |
| 2026-11-11 16:05:53 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | -0.031 |  |
| 2026-11-11 16:05:43 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-11 16:05:33 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.038 |  |
| 2026-11-11 16:05:25 | Moragaswewa (Deduru Oya) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-11-11 16:05:13 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-11 16:05:13 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | -0.019 |  |
| 2026-11-11 16:05:11 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | -0.028 |  |
| 2026-11-11 16:05:03 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-11-11 16:05:02 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-11 16:04:48 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-11 16:04:40 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.109 |  |
| 2026-11-11 16:04:36 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-11 16:04:34 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 16:04:17 | Moragaswewa (Deduru Oya) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-11-11 16:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.52 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 16:03:28 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.080 |  |
| 2026-11-11 16:02:35 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:02:34 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.050 |  |
| 2026-11-11 16:02:27 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 16:02:20 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 16:02:19 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:02:09 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.019 |  |
| 2026-11-11 16:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-11 16:01:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:01:28 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 16:01:25 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 16:01:24 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.167 |  |
| 2026-11-11 16:01:16 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-11 16:00:54 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:00:45 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 16:08:20 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 16:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.52 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 16:05:53 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | -0.031 |  |
| 2026-11-11 16:05:13 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | -0.019 |  |
| 2026-11-11 16:06:27 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | -0.039 |  |
| 2026-11-11 16:14:45 | Magura (Kalu Ganga) | 3.38 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2026-11-11 16:07:11 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-11-11 16:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-11 16:05:13 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-11 16:13:59 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-11 16:04:36 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-11 16:04:48 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-11 16:05:43 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-11 16:01:25 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 16:04:34 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 16:01:28 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 16:02:27 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 16:11:40 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-11 16:05:25 | Moragaswewa (Deduru Oya) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-11-11 16:00:45 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-11 16:02:20 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 16:09:19 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-11-11 16:00:54 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:01:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:08:40 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:02:35 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:02:19 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-11-11 16:02:09 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.019 |  |
| 2026-11-11 16:05:02 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-11 16:01:16 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-11 16:05:11 | Ellagawa (Kalu Ganga) | 8.45 | 🟢 Normal | -0.028 |  |
| 2026-11-11 16:05:33 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.038 |  |
| 2026-11-11 16:17:38 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | -0.042 |  |
| 2026-11-11 16:05:03 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-11-11 16:02:34 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.050 |  |
| 2026-11-11 16:03:28 | Hanwella (Kelani Ganga) | 3.98 | 🟢 Normal | -0.080 |  |
| 2026-11-11 16:04:40 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.109 |  |
| 2026-11-11 16:07:58 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | -0.125 |  |
| 2026-11-11 16:01:24 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)