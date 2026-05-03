# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_23:21:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,165 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 23:21:43 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-05-03 23:14:36 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-05-03 23:10:56 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.046 |  |
| 2026-05-03 23:10:39 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-03 23:09:56 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:09:31 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-03 23:09:19 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:09:03 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:08:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-03 23:07:00 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:05:19 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:04:34 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-05-03 23:04:25 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:04:12 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-05-03 23:04:06 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-03 23:03:16 | Yaka Wewa (Ma Oya) | 4.00 | 🟡 Alert | 113.333 | 🔺 Rising |
| 2026-05-03 23:02:45 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.013 |  |
| 2026-05-03 23:02:17 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 23:02:10 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-05-03 23:01:32 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.028 |  |
| 2026-05-03 23:01:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 113.333 | 🔺 Rising |
| 2026-05-03 23:01:20 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:01:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:01:16 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:00:54 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:00:53 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-03 23:00:48 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:00:44 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-05-03 23:00:36 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-03 23:00:13 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 23:03:16 | Yaka Wewa (Ma Oya) | 4.00 | 🟡 Alert | 113.333 | 🔺 Rising |
| 2026-05-03 23:00:36 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-03 23:00:53 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-03 23:10:39 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 23:09:31 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-03 22:03:12 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-03 22:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 23:02:17 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 23:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:01:16 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:04:25 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:01:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:07:00 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:00:13 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:00:48 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 21:02:25 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:09:56 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:09:03 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:05:19 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:09:19 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:01:20 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 23:14:36 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-05-03 23:04:06 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-03 22:14:58 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-03 23:00:44 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-05-03 23:04:34 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-05-03 23:02:45 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.013 |  |
| 2026-05-03 23:08:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-03 23:21:43 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.020 |  |
| 2026-05-03 23:01:32 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.028 |  |
| 2026-05-03 23:04:12 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-05-03 22:02:50 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-05-03 21:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.031 |  |
| 2026-05-03 22:15:08 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.033 |  |
| 2026-05-03 23:10:56 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.046 |  |
| 2026-05-03 23:02:10 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)