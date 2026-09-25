# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_12:10:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,557 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 12:10:01 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 12:09:43 | Thawalama (Gin Ganga) | 4.28 | 🟡 Alert | -0.085 |  |
| 2026-09-25 12:09:17 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | -0.009 |  |
| 2026-09-25 12:08:10 | Rathnapura (Kalu Ganga) | 6.27 | 🟡 Alert | -0.009 |  |
| 2026-09-25 12:07:35 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.027 |  |
| 2026-09-25 12:05:38 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-25 12:05:31 | Hanwella (Kelani Ganga) | 6.24 | 🟢 Normal | -0.019 |  |
| 2026-09-25 12:05:20 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.011 |  |
| 2026-09-25 12:05:10 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-09-25 12:05:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:04:58 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.033 |  |
| 2026-09-25 12:04:58 | Deraniyagala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.067 |  |
| 2026-09-25 12:04:55 | Baddegama (Gin Ganga) | 4.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 12:04:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:04:23 | Ellagawa (Kalu Ganga) | 8.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-25 12:04:13 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:04:12 | Putupaula (Kalu Ganga) | 2.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 12:04:09 | Glencourse (Kelani Ganga) | 14.17 | 🟢 Normal | -0.086 |  |
| 2026-09-25 12:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 12:04:04 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-09-25 12:03:53 | Norwood (Kelani Ganga) | 1.52 | 🟡 Alert | -0.030 |  |
| 2026-09-25 12:03:10 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:03:08 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.021 |  |
| 2026-09-25 12:02:43 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-25 12:02:38 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:32 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | -0.060 |  |
| 2026-09-25 12:02:19 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:15 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:12 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-25 12:02:06 | Panadugama (Nilwala Ganga) | 6.48 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-25 12:02:01 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-09-25 12:01:48 | Peradeniya (Mahaweli Ganga) | 4.12 | 🟢 Normal | -0.196 |  |
| 2026-09-25 12:01:47 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-25 12:01:17 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:01:03 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-09-25 12:00:40 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-25 12:00:28 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:00:14 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 12:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 12:04:55 | Baddegama (Gin Ganga) | 4.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 12:10:01 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 12:02:06 | Panadugama (Nilwala Ganga) | 6.48 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-25 12:08:10 | Rathnapura (Kalu Ganga) | 6.27 | 🟡 Alert | -0.009 |  |
| 2026-09-25 12:09:17 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | -0.009 |  |
| 2026-09-25 12:03:53 | Norwood (Kelani Ganga) | 1.52 | 🟡 Alert | -0.030 |  |
| 2026-09-25 12:09:43 | Thawalama (Gin Ganga) | 4.28 | 🟡 Alert | -0.085 |  |
| 2026-09-25 12:04:04 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-09-25 12:01:47 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-25 12:05:38 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-25 12:00:40 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-25 12:02:43 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-25 12:04:23 | Ellagawa (Kalu Ganga) | 8.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-25 12:04:12 | Putupaula (Kalu Ganga) | 2.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 12:05:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:01:17 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:19 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:04:13 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:38 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:00:28 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:04:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:03:10 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:15 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:00:14 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 12:02:12 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-25 12:05:20 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.011 |  |
| 2026-09-25 12:05:31 | Hanwella (Kelani Ganga) | 6.24 | 🟢 Normal | -0.019 |  |
| 2026-09-25 12:05:10 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-09-25 12:01:03 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-09-25 12:03:08 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | -0.021 |  |
| 2026-09-25 12:07:35 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.027 |  |
| 2026-09-25 12:04:58 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.033 |  |
| 2026-09-25 12:02:01 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-09-25 12:02:32 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | -0.060 |  |
| 2026-09-25 12:04:58 | Deraniyagala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.067 |  |
| 2026-09-25 12:04:09 | Glencourse (Kelani Ganga) | 14.17 | 🟢 Normal | -0.086 |  |
| 2026-09-25 12:01:48 | Peradeniya (Mahaweli Ganga) | 4.12 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)