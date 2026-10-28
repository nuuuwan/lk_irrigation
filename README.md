# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_04:03:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,823 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 04:03:11 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:03:08 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.034 |  |
| 2026-10-29 04:02:44 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-10-29 04:02:36 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:25 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.039 |  |
| 2026-10-29 04:02:23 | Moragaswewa (Deduru Oya) | 1.83 | 🟢 Normal | -0.120 |  |
| 2026-10-29 04:02:09 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.58 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-29 04:02:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:01:47 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.041 |  |
| 2026-10-29 04:01:05 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-29 03:17:34 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.041 |  |
| 2026-10-29 03:17:32 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 03:01:34 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 03:07:26 | Baddegama (Gin Ganga) | 4.19 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-29 04:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.58 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-29 03:04:04 | Panadugama (Nilwala Ganga) | 6.03 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-29 03:10:57 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-10-29 03:11:30 | Ellagawa (Kalu Ganga) | 10.24 | 🟡 Alert | -0.009 |  |
| 2026-10-29 03:00:49 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.050 |  |
| 2026-10-29 03:02:18 | Rathnapura (Kalu Ganga) | 5.32 | 🟡 Alert | -0.073 |  |
| 2026-10-29 03:14:01 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-10-29 01:05:27 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-10-29 03:08:36 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-29 03:03:02 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-29 04:01:05 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 03:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:09 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:36 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:03:11 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 03:03:13 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 03:05:18 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 03:07:02 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 03:07:18 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 03:05:32 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-29 03:01:11 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.015 |  |
| 2026-10-29 04:03:08 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.034 |  |
| 2026-10-29 04:02:25 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.039 |  |
| 2026-10-29 03:07:06 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.039 |  |
| 2026-10-29 03:02:28 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.039 |  |
| 2026-10-29 03:07:27 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | -0.040 |  |
| 2026-10-29 04:02:44 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-10-29 04:01:47 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.041 |  |
| 2026-10-29 03:01:57 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.041 |  |
| 2026-10-29 03:05:43 | Pitabeddara (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.042 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-29 03:04:22 | Thawalama (Gin Ganga) | 2.89 | 🟢 Normal | -0.059 |  |
| 2026-10-29 04:02:23 | Moragaswewa (Deduru Oya) | 1.83 | 🟢 Normal | -0.120 |  |
| 2026-10-29 03:09:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -2.917 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)