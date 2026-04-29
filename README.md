# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_17:38:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,395 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 17:38:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:13:59 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:12:26 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 17:10:42 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:09:39 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-29 17:08:45 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:07:12 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:07:04 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-29 17:07:02 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:06:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:06:52 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | -0.060 |  |
| 2026-04-29 17:06:40 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.032 |  |
| 2026-04-29 17:06:20 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-29 17:05:59 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-04-29 17:05:56 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:05:50 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:04:44 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 17:04:21 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-04-29 17:04:11 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-29 17:03:36 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-29 17:03:30 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-04-29 17:03:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.165 |  |
| 2026-04-29 17:03:02 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-04-29 17:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-04-29 17:02:41 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 17:02:22 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-29 17:02:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:02:12 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-29 17:02:10 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-29 17:02:07 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.053 |  |
| 2026-04-29 17:01:57 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:45 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-04-29 17:01:36 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-29 17:01:36 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:28 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:23 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:18 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 17:01:13 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-04-29 17:00:54 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:00:40 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.076 |  |
| 2026-04-29 17:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 17:04:11 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-29 17:02:10 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-29 17:02:22 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-29 17:09:39 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-29 17:07:04 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-29 17:01:36 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-29 17:01:18 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 17:02:41 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 17:04:44 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 17:12:26 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 17:07:12 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:00:54 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:38:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:28 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:13:59 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:57 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:05:50 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:02:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:23 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:01:36 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:05:56 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:10:42 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:06:20 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-29 17:03:36 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-29 17:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-04-29 17:02:12 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-29 17:04:21 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-04-29 17:01:45 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-04-29 17:03:02 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-04-29 17:03:30 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-04-29 17:06:40 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.032 |  |
| 2026-04-29 17:05:59 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-04-29 17:01:13 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-04-29 17:02:07 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.053 |  |
| 2026-04-29 17:06:52 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | -0.060 |  |
| 2026-04-29 17:00:40 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.076 |  |
| 2026-04-29 17:03:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)