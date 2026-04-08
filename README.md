# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_04:13:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,057 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 04:13:12 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 756.000 | 🔺 Rising |
| 2026-04-09 04:13:11 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 756.000 | 🔺 Rising |
| 2026-04-09 04:10:29 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-09 04:06:57 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.706 |  |
| 2026-04-09 04:06:57 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:05:34 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-04-09 04:05:16 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-09 04:05:15 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.706 |  |
| 2026-04-09 04:04:36 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-09 04:04:25 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:03:07 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-09 04:02:53 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 04:02:48 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.108 |  |
| 2026-04-09 04:02:44 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.005 |  |
| 2026-04-09 04:02:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:02:23 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:02:13 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-04-09 04:01:58 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-09 04:01:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:01:25 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:01:19 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.031 |  |
| 2026-04-09 04:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-04-09 04:01:13 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 04:00:44 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:00:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:00:33 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:00:25 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 03:53:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-04-09 03:51:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-04-09 03:25:44 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 04:13:12 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 756.000 | 🔺 Rising |
| 2026-04-08 18:05:20 | Weraganthota (Mahaweli Ganga) | 3.20 | 🟢 Normal | 5.983 | 🔺 Rising |
| 2026-04-09 03:18:13 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 3.000 | 🔺 Rising |
| 2026-04-09 04:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.378 | 🔺 Rising |
| 2026-04-09 03:06:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-09 03:20:07 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-09 04:05:16 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-09 04:01:13 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 04:02:53 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 01:04:03 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 04:00:25 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 03:10:59 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.003 |  |
| 2026-04-09 04:00:33 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 02:05:43 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:00:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:00:44 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:02:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:01:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-09 00:01:59 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:05:30 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:02:13 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:18:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:06:57 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:01:25 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:04:25 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-04-09 04:02:23 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-09 03:03:23 | Panadugama (Nilwala Ganga) | 1.76 | 🟢 Normal | -0.004 |  |
| 2026-04-09 04:02:44 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.005 |  |
| 2026-04-09 04:05:34 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-04-08 18:02:20 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 04:10:29 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-09 04:04:36 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-09 04:01:58 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-09 04:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-04-09 04:03:07 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-09 04:01:19 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.031 |  |
| 2026-04-09 04:02:48 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.108 |  |
| 2026-04-09 04:06:57 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.706 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)