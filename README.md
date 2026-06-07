# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_04:06:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,452 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 04:06:11 | Glencourse (Kelani Ganga) | 11.53 | 🟢 Normal | -0.070 |  |
| 2026-06-08 04:05:45 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-08 04:05:37 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.029 |  |
| 2026-06-08 04:05:30 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:05:28 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 04:04:57 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:04:49 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.094 |  |
| 2026-06-08 04:04:29 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:04:15 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.008 |  |
| 2026-06-08 04:03:43 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-06-08 04:03:00 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.050 |  |
| 2026-06-08 04:02:55 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-06-08 04:02:48 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:02:38 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.144 |  |
| 2026-06-08 04:02:36 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:01:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:01:50 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.021 |  |
| 2026-06-08 04:01:41 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.004 |  |
| 2026-06-08 04:01:41 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.010 |  |
| 2026-06-08 04:01:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:01:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:00:49 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:00:19 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-06-08 03:55:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:39:14 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 03:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-06-08 03:03:55 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-08 03:05:32 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-08 04:05:28 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 04:05:45 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-08 04:01:41 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.004 |  |
| 2026-06-08 04:04:57 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:05:40 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:01:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:02:36 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:03:43 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:02:48 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:01:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:39:14 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:01:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:14:12 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:05:30 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:02:20 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:00:49 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:04:29 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:13:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:01:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:04:15 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.008 |  |
| 2026-06-08 03:09:11 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-06-08 04:01:41 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.010 |  |
| 2026-06-08 04:00:19 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-06-08 04:01:50 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.021 |  |
| 2026-06-08 04:05:37 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.029 |  |
| 2026-06-08 04:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-06-08 04:02:55 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-06-08 04:03:00 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.050 |  |
| 2026-06-08 03:02:21 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.068 |  |
| 2026-06-08 04:06:11 | Glencourse (Kelani Ganga) | 11.53 | 🟢 Normal | -0.070 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-08 04:04:49 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.094 |  |
| 2026-06-08 04:02:38 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.144 |  |
| 2026-06-08 03:06:14 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)