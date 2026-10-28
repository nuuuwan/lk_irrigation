# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_17:12:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,456 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 17:12:17 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.019 |  |
| 2026-10-28 17:09:48 | Urawa (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.127 |  |
| 2026-10-28 17:08:20 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.066 |  |
| 2026-10-28 17:08:18 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | 0.056 | 🔺 Rising |
| 2026-10-28 17:07:46 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-28 17:07:28 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.063 |  |
| 2026-10-28 17:06:44 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 17:05:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.70 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 17:05:04 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.040 |  |
| 2026-10-28 17:04:45 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-28 17:04:44 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:04:30 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.026 | 🔺 Rising |
| 2026-10-28 17:04:27 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:04:26 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:04:26 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.090 |  |
| 2026-10-28 17:04:17 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-28 17:03:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:03:50 | Ellagawa (Kalu Ganga) | 10.41 | 🟡 Alert | 0.000 |  |
| 2026-10-28 17:03:20 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-10-28 17:03:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:03:13 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:59 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:02:52 | Moragaswewa (Deduru Oya) | 3.00 | 🟢 Normal | -0.034 |  |
| 2026-10-28 17:02:50 | Putupaula (Kalu Ganga) | 3.70 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 17:02:44 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.012 |  |
| 2026-10-28 17:02:27 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:26 | Galgamuwa (Mee Oya) | 2.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-28 17:02:22 | Dunamale (Aththanagalu Oya) | 3.27 | 🟢 Normal | -0.099 |  |
| 2026-10-28 17:02:12 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:02:11 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:05 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.017 |  |
| 2026-10-28 17:01:39 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:01:38 | Pitabeddara (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-28 17:01:32 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:01:31 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-28 17:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 17:01:12 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:01:03 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.081 |  |
| 2026-10-28 17:01:02 | Magura (Kalu Ganga) | 4.19 | 🟡 Alert | 0.189 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 17:08:18 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | 0.056 | 🔺 Rising |
| 2026-10-28 17:04:30 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.026 | 🔺 Rising |
| 2026-10-28 17:06:44 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 17:05:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.70 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 17:01:02 | Magura (Kalu Ganga) | 4.19 | 🟡 Alert | 0.189 | 🔺 Rising |
| 2026-10-28 17:02:50 | Putupaula (Kalu Ganga) | 3.70 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 17:03:50 | Ellagawa (Kalu Ganga) | 10.41 | 🟡 Alert | 0.000 |  |
| 2026-10-28 17:08:20 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.066 |  |
| 2026-10-28 17:04:45 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-28 17:01:38 | Pitabeddara (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-28 17:01:31 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-28 17:04:17 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-28 17:02:26 | Galgamuwa (Mee Oya) | 2.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-28 17:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 17:02:59 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:01:32 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:02:12 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:04:26 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:04:27 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:03:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:04:44 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:03:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:11 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:01:12 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:03:13 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:01:39 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:27 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:44 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.012 |  |
| 2026-10-28 17:02:05 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.017 |  |
| 2026-10-28 17:12:17 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.019 |  |
| 2026-10-28 17:07:46 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-28 17:03:20 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-10-28 17:02:52 | Moragaswewa (Deduru Oya) | 3.00 | 🟢 Normal | -0.034 |  |
| 2026-10-28 17:05:04 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.040 |  |
| 2026-10-28 17:07:28 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.063 |  |
| 2026-10-28 17:01:03 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.081 |  |
| 2026-10-28 17:04:26 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.090 |  |
| 2026-10-28 17:02:22 | Dunamale (Aththanagalu Oya) | 3.27 | 🟢 Normal | -0.099 |  |
| 2026-10-28 17:09:48 | Urawa (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)