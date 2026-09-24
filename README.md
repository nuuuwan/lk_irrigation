# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_04:04:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Norwood — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 04:04:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:04:12 | Norwood (Kelani Ganga) | 1.75 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-25 04:03:50 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-25 04:03:45 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 04:03:33 | Nawalapitiya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-25 04:03:14 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 04:03:01 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 04:02:39 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | -0.303 |  |
| 2026-09-25 04:02:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:02:08 | Hanwella (Kelani Ganga) | 6.27 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-25 04:01:46 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:29 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:00:43 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:00:39 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | -0.021 |  |
| 2026-09-25 03:17:40 | Panadugama (Nilwala Ganga) | 6.61 | 🟠 Minor Flood | -0.018 |  |
| 2026-09-25 03:17:04 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 03:06:35 | Baddegama (Gin Ganga) | 4.61 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 04:03:14 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 03:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 03:17:40 | Panadugama (Nilwala Ganga) | 6.61 | 🟠 Minor Flood | -0.018 |  |
| 2026-09-25 04:04:12 | Norwood (Kelani Ganga) | 1.75 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-25 03:10:06 | Thawalama (Gin Ganga) | 4.30 | 🟡 Alert | -0.009 |  |
| 2026-09-25 03:05:00 | Rathnapura (Kalu Ganga) | 6.43 | 🟡 Alert | -0.010 |  |
| 2026-09-25 04:00:39 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | -0.021 |  |
| 2026-09-25 04:03:33 | Nawalapitiya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-25 04:02:08 | Hanwella (Kelani Ganga) | 6.27 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-25 03:05:47 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-25 04:03:01 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 03:09:04 | Holombuwa (Kelani Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-25 03:05:49 | Kithulgala (Kelani Ganga) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 04:03:45 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 03:08:02 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 03:02:22 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 03:00:50 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:00:43 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 03:05:35 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:29 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:46 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:02:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 03:05:32 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:04:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 03:08:35 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-25 03:04:40 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.010 |  |
| 2026-09-25 04:03:50 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-25 03:02:25 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | -0.020 |  |
| 2026-09-25 03:07:48 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.028 |  |
| 2026-09-25 03:07:12 | Glencourse (Kelani Ganga) | 14.74 | 🟢 Normal | -0.032 |  |
| 2026-09-25 03:17:04 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.062 |  |
| 2026-09-25 03:03:11 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | -0.072 |  |
| 2026-09-25 04:02:39 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | -0.303 |  |

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)