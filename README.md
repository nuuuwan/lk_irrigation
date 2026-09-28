# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_05:03:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,957 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 05:03:27 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:03:12 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:03:04 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-28 05:02:47 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:44 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.010 |  |
| 2026-09-28 05:02:43 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-09-28 05:02:28 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-09-28 05:02:22 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.020 |  |
| 2026-09-28 05:02:19 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:16 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:15 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:08 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:06 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:01:57 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.079 |  |
| 2026-09-28 05:01:51 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:01:23 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:01:14 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-28 05:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:00:51 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.021 |  |
| 2026-09-28 05:00:46 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:00:15 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 04:00:00 | Baddegama (Gin Ganga) | 4.35 | 🟠 Minor Flood | 0.006 | 🔺 Rising |
| 2026-09-28 05:00:15 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-28 04:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.020 |  |
| 2026-09-28 04:04:01 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-09-28 05:03:04 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-27 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:01:23 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:16 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:06 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:03:27 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:03:12 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:02:15 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:01:51 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:05:37 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:03:33 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:14:57 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:00:46 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:04:38 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:08:42 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:47 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-09-28 05:02:19 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:06:46 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.003 |  |
| 2026-09-28 04:21:13 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-09-28 05:02:44 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.010 |  |
| 2026-09-28 05:01:14 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-28 05:02:43 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-09-28 04:00:14 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-09-28 04:07:25 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.020 |  |
| 2026-09-28 05:02:22 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.020 |  |
| 2026-09-28 04:06:21 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-09-28 05:00:51 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.021 |  |
| 2026-09-28 04:46:10 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.024 |  |
| 2026-09-28 05:02:28 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.051 |  |
| 2026-09-28 05:01:57 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.079 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |
| 2026-09-28 04:34:43 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -112.500 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)