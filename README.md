# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_05:02:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 05:02:19 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.061 |  |
| 2026-10-18 05:02:16 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.099 |  |
| 2026-10-18 05:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-18 05:01:14 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-10-18 05:01:14 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:01:14 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:01:08 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-10-18 05:01:04 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-10-18 05:01:02 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.017 |  |
| 2026-10-18 04:58:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | -0.316 |  |
| 2026-10-18 04:54:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.38 | 🟡 Alert | -0.316 |  |
| 2026-10-18 04:47:10 | Panadugama (Nilwala Ganga) | 6.19 | 🟠 Minor Flood | -0.012 |  |
| 2026-10-18 04:44:42 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.047 |  |
| 2026-10-18 04:24:31 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.048 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 04:02:42 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 04:47:10 | Panadugama (Nilwala Ganga) | 6.19 | 🟠 Minor Flood | -0.012 |  |
| 2026-10-18 04:58:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | -0.316 |  |
| 2026-10-18 04:01:28 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 04:03:34 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-18 05:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-18 04:02:16 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-18 04:02:26 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 04:05:25 | Horowpothana (Yan Oya) | 2.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-18 04:04:09 | Hanwella (Kelani Ganga) | 4.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:01:14 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:01:14 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:06:01 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:04:27 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:01:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:05:01 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-18 04:03:50 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-18 03:04:52 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-18 04:02:26 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-10-18 05:01:02 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.017 |  |
| 2026-10-18 04:06:52 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-18 05:01:08 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-10-18 04:02:08 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.031 |  |
| 2026-10-18 03:16:36 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.034 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-18 04:44:42 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.047 |  |
| 2026-10-18 04:01:21 | Moraketiya (Walawe Ganga) | 1.52 | 🟢 Normal | -0.052 |  |
| 2026-10-18 04:05:36 | Urawa (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.057 |  |
| 2026-10-18 04:04:52 | Thawalama (Gin Ganga) | 3.90 | 🟢 Normal | -0.057 |  |
| 2026-10-18 05:01:14 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-10-18 05:01:04 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-10-18 04:06:12 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.060 |  |
| 2026-10-18 05:02:19 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.061 |  |
| 2026-10-18 05:02:16 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.099 |  |
| 2026-10-18 04:03:51 | Giriulla (Maha Oya) | 2.82 | 🟢 Normal | -0.124 |  |
| 2026-10-18 04:03:52 | Glencourse (Kelani Ganga) | 12.57 | 🟢 Normal | -0.240 |  |
| 2026-10-18 04:07:26 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | -0.276 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)