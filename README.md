# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_01:27:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Norwood — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 01:27:13 | Nawalapitiya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.272 |  |
| 2026-09-25 01:16:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:13:43 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-25 01:09:09 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | -0.110 |  |
| 2026-09-25 01:08:33 | Norwood (Kelani Ganga) | 1.57 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-25 01:08:16 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-09-25 01:07:04 | Badalgama (Maha Oya) | 3.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-25 01:06:57 | Hanwella (Kelani Ganga) | 6.02 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-25 01:06:30 | Baddegama (Gin Ganga) | 4.58 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-09-25 01:06:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-09-25 01:06:13 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.068 |  |
| 2026-09-25 01:05:58 | Kithulgala (Kelani Ganga) | 2.70 | 🟢 Normal | -0.231 |  |
| 2026-09-25 01:05:32 | Rathnapura (Kalu Ganga) | 6.45 | 🟡 Alert | 0.000 |  |
| 2026-09-25 01:04:31 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 01:04:16 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-09-25 01:04:15 | Thawalama (Gin Ganga) | 4.53 | 🟡 Alert | -0.248 |  |
| 2026-09-25 01:03:50 | Glencourse (Kelani Ganga) | 14.75 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-25 01:03:43 | Peradeniya (Mahaweli Ganga) | 4.80 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-09-25 01:03:08 | Panadugama (Nilwala Ganga) | 6.64 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-25 01:03:06 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:49 | Deraniyagala (Kelani Ganga) | 2.49 | 🟢 Normal | -0.270 |  |
| 2026-09-25 01:02:41 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:26 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:26 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 01:02:25 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:09 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:01:32 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-09-25 01:01:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:01:25 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:01:23 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:00:43 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | -0.034 |  |
| 2026-09-25 01:00:23 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 01:06:30 | Baddegama (Gin Ganga) | 4.58 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-09-25 01:08:16 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-09-25 00:10:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 01:03:08 | Panadugama (Nilwala Ganga) | 6.64 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-25 01:08:33 | Norwood (Kelani Ganga) | 1.57 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-25 01:05:32 | Rathnapura (Kalu Ganga) | 6.45 | 🟡 Alert | 0.000 |  |
| 2026-09-25 01:00:43 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | -0.034 |  |
| 2026-09-25 01:04:15 | Thawalama (Gin Ganga) | 4.53 | 🟡 Alert | -0.248 |  |
| 2026-09-25 01:03:43 | Peradeniya (Mahaweli Ganga) | 4.80 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-09-25 01:03:50 | Glencourse (Kelani Ganga) | 14.75 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-25 01:06:57 | Hanwella (Kelani Ganga) | 6.02 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-25 00:02:11 | Ellagawa (Kalu Ganga) | 8.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-25 01:07:04 | Badalgama (Maha Oya) | 3.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-25 01:13:43 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-25 01:02:26 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 01:04:31 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:16:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:01:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:05:30 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:41 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:25 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:03:06 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:09 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:01:25 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:01:23 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:26 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:00:23 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-09-25 01:01:32 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-09-25 01:06:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-09-25 01:04:16 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-09-25 01:06:13 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.068 |  |
| 2026-09-25 00:13:09 | Pitabeddara (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.109 |  |
| 2026-09-25 01:09:09 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | -0.110 |  |
| 2026-09-25 01:05:58 | Kithulgala (Kelani Ganga) | 2.70 | 🟢 Normal | -0.231 |  |
| 2026-09-25 01:02:49 | Deraniyagala (Kelani Ganga) | 2.49 | 🟢 Normal | -0.270 |  |
| 2026-09-25 01:27:13 | Nawalapitiya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.272 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)