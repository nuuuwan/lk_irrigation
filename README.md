# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_06:23:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,604 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 06:23:15 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | -0.002 |  |
| 2026-05-21 06:12:11 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.027 |  |
| 2026-05-21 06:11:55 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:10:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:10:25 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.018 |  |
| 2026-05-21 06:10:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:09:40 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:08:55 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-21 06:08:11 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:06:34 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.038 |  |
| 2026-05-21 06:06:19 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:06:14 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:06:02 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:05:24 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-05-21 06:05:09 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.021 |  |
| 2026-05-21 06:04:25 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:04:21 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:04:01 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 06:02:20 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-21 06:08:55 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-21 06:02:21 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-21 06:01:44 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 06:02:52 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-21 06:02:16 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 06:00:58 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:06:14 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:08:11 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:04:25 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:06:02 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:09:40 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:11:55 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:01:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:00:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:04:21 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:06:19 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:03:36 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:02:34 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:10:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-05-21 06:23:15 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | -0.002 |  |
| 2026-05-21 06:05:24 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-05-21 06:02:58 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-05-21 06:00:31 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-21 06:03:19 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-05-21 06:01:21 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-05-21 06:00:24 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-05-21 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-05-21 06:01:12 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-05-21 06:02:28 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.013 |  |
| 2026-05-21 06:04:01 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.016 |  |
| 2026-05-21 06:10:25 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.018 |  |
| 2026-05-21 06:05:09 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.021 |  |
| 2026-05-21 06:12:11 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.027 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-21 05:07:22 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.034 |  |
| 2026-05-21 06:06:34 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.038 |  |
| 2026-05-21 06:02:17 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.060 |  |
| 2026-05-21 06:00:59 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)