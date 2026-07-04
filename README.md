# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_21:09:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,360 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 21:09:04 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.054 |  |
| 2026-07-04 21:08:24 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 21:08:07 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 21:07:45 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.090 |  |
| 2026-07-04 21:07:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.086 |  |
| 2026-07-04 21:06:48 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 21:06:19 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:05:59 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.060 |  |
| 2026-07-04 21:05:57 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:05:31 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-04 21:05:28 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-07-04 21:05:24 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:05:08 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:04:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-04 21:04:26 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:04:22 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:04:17 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:04:16 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-07-04 21:04:04 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:03:20 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:03:16 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:03:11 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-07-04 21:03:01 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:02:58 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:02:58 | Hanwella (Kelani Ganga) | 3.03 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-04 21:02:34 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-04 21:02:22 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-04 21:01:46 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:01:44 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:01:37 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:01:35 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-04 21:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 21:00:59 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.050 |  |
| 2026-07-04 21:00:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:32:30 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 21:03:11 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-07-04 21:04:16 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-07-04 21:01:35 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-04 21:04:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-04 21:02:58 | Hanwella (Kelani Ganga) | 3.03 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-04 21:02:34 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-04 21:05:31 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-04 21:02:22 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-04 21:08:07 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 21:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 20:02:52 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 21:06:48 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 21:08:24 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:00:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:01:46 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:03:16 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:02:58 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:01:44 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:05:08 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:05:57 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:04:04 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:04:22 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:04:17 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:01:37 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:05:24 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:04:26 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:03:20 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 20:05:21 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:03:01 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:06:19 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 21:05:28 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-07-04 21:00:59 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.050 |  |
| 2026-07-04 21:09:04 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.054 |  |
| 2026-07-04 21:05:59 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.060 |  |
| 2026-07-04 21:07:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.086 |  |
| 2026-07-04 21:07:45 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)