# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_17:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,438 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-10-28 16:25:48 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 16:03:46 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | 0.051 | 🔺 Rising |
| 2026-10-28 16:08:09 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 16:18:05 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 16:07:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.71 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 17:01:02 | Magura (Kalu Ganga) | 4.19 | 🟡 Alert | 0.189 | 🔺 Rising |
| 2026-10-28 17:02:50 | Putupaula (Kalu Ganga) | 3.70 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 16:03:31 | Ellagawa (Kalu Ganga) | 10.41 | 🟡 Alert | -0.011 |  |
| 2026-10-28 16:04:47 | Rathnapura (Kalu Ganga) | 6.02 | 🟡 Alert | -0.069 |  |
| 2026-10-28 17:01:38 | Pitabeddara (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-10-28 17:01:31 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-28 16:03:47 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-28 17:02:26 | Galgamuwa (Mee Oya) | 2.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-28 17:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 17:02:59 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:01:32 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:03:39 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-28 17:02:12 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:08:21 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:05:22 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:03:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:11 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:01:12 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:03:13 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:01:39 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:27 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-28 17:02:44 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.012 |  |
| 2026-10-28 17:02:05 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.017 |  |
| 2026-10-28 16:07:47 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-28 17:03:20 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-10-28 16:03:31 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-10-28 17:02:52 | Moragaswewa (Deduru Oya) | 3.00 | 🟢 Normal | -0.034 |  |
| 2026-10-28 16:08:37 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.046 |  |
| 2026-10-28 16:02:51 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.049 |  |
| 2026-10-28 16:01:10 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.052 |  |
| 2026-10-28 16:04:38 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.058 |  |
| 2026-10-28 17:01:03 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.081 |  |
| 2026-10-28 17:02:22 | Dunamale (Aththanagalu Oya) | 3.27 | 🟢 Normal | -0.099 |  |
| 2026-10-28 16:03:38 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)