# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_04:04:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,218 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 04:04:45 | Badalgama (Maha Oya) | 4.16 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-10-15 04:04:37 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-15 04:03:39 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-15 04:03:38 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-15 04:03:23 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-10-15 04:03:10 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-10-15 04:02:48 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-10-15 04:02:38 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-15 04:02:30 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-15 04:02:17 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-15 04:02:11 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.113 |  |
| 2026-10-15 04:01:59 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 04:01:17 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.060 |  |
| 2026-10-15 04:01:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 04:01:05 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 04:00:11 | Magura (Kalu Ganga) | 4.15 | 🟡 Alert | -0.263 |  |
| 2026-10-15 03:46:30 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | -0.263 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 03:09:32 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 04:02:30 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-15 03:06:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | 0.014 | 🔺 Rising |
| 2026-10-15 04:00:11 | Magura (Kalu Ganga) | 4.15 | 🟡 Alert | -0.263 |  |
| 2026-10-15 04:03:39 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-15 02:01:20 | Glencourse (Kelani Ganga) | 13.44 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-10-15 04:04:45 | Badalgama (Maha Oya) | 4.16 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-10-15 04:02:48 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-10-15 03:07:05 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-15 04:04:37 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-15 03:00:26 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-15 04:02:38 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-15 03:03:09 | Giriulla (Maha Oya) | 3.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-15 04:01:59 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 04:01:05 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:01:11 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:10:13 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-15 04:01:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:04:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:05:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:04:35 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:10:16 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 04:02:17 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-15 03:11:54 | Pitabeddara (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.007 |  |
| 2026-10-15 03:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-10-15 04:03:10 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-10-15 03:05:10 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-10-15 04:03:23 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-10-15 03:03:43 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-10-15 03:05:39 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.051 |  |
| 2026-10-15 04:01:17 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.060 |  |
| 2026-10-15 03:03:51 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.069 |  |
| 2026-10-15 04:02:11 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.113 |  |
| 2026-10-15 03:11:02 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | -0.145 |  |
| 2026-10-15 03:04:14 | Rathnapura (Kalu Ganga) | 4.51 | 🟢 Normal | -0.217 |  |
| 2026-10-15 03:10:17 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -4.797 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)