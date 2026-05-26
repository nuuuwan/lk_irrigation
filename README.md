# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_20:09:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,415 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 20:09:46 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.050 |  |
| 2026-05-26 20:08:42 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 20:07:50 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-05-26 20:07:28 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-05-26 20:06:37 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:06:16 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-05-26 20:05:54 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-05-26 20:05:43 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 20:05:04 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.039 |  |
| 2026-05-26 20:04:10 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-26 20:04:07 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:04:07 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:03:50 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:03:39 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:03:12 | Glencourse (Kelani Ganga) | 12.06 | 🟢 Normal | -0.040 |  |
| 2026-05-26 20:03:11 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:03:08 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-05-26 20:03:04 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:02:59 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:02:58 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.040 |  |
| 2026-05-26 20:02:44 | Hanwella (Kelani Ganga) | 4.64 | 🟢 Normal | -0.041 |  |
| 2026-05-26 20:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-26 20:02:22 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:02:05 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-05-26 20:02:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:02:00 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-05-26 20:01:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:01:14 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-26 20:01:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:00:09 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:20:01 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 19:13:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.009 |  |
| 2026-05-26 20:02:00 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-05-26 20:04:10 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-26 20:08:42 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 20:05:43 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 19:06:11 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 20:01:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:00:09 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:04:07 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:01:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:02:59 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:02:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:03:11 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:04:07 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:03:39 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:03:04 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:02:22 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:04:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:06:37 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 20:03:50 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 19:11:53 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2026-05-26 20:07:50 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-05-26 20:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-26 20:05:54 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-05-26 20:01:14 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-26 19:06:01 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.011 |  |
| 2026-05-26 20:02:05 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-05-26 19:16:28 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.016 |  |
| 2026-05-26 20:07:28 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 20:06:16 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-05-26 20:03:08 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-05-26 20:05:04 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.039 |  |
| 2026-05-26 20:02:58 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.040 |  |
| 2026-05-26 20:03:12 | Glencourse (Kelani Ganga) | 12.06 | 🟢 Normal | -0.040 |  |
| 2026-05-26 20:02:44 | Hanwella (Kelani Ganga) | 4.64 | 🟢 Normal | -0.041 |  |
| 2026-05-26 20:09:46 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)