# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_09:09:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,473 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 09:09:58 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:09:48 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:08:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-04-07 09:08:26 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-07 09:08:10 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-07 09:07:47 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-07 09:07:19 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:07:12 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:06:41 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:05:32 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.041 |  |
| 2026-04-07 09:05:25 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:05:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:05:08 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-07 09:05:04 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.099 |  |
| 2026-04-07 09:04:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:04:32 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.379 |  |
| 2026-04-07 09:04:05 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.073 |  |
| 2026-04-07 09:03:45 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.100 |  |
| 2026-04-07 09:03:32 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:03:20 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-04-07 09:03:18 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-04-07 09:03:18 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:03:14 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:03:09 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:03:05 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-07 09:03:02 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-04-07 09:02:50 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 09:02:48 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:02:45 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.060 |  |
| 2026-04-07 09:02:20 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.133 |  |
| 2026-04-07 09:02:14 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2026-04-07 09:02:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-07 09:01:38 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 09:01:32 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.041 |  |
| 2026-04-07 09:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:01:10 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:00:32 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:00:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.070 |  |
| 2026-04-07 08:26:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 09:05:08 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-07 09:02:50 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 09:08:26 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-07 09:02:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-07 09:08:10 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-07 09:01:38 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 09:07:47 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-07 09:05:25 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:05:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:02:48 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:09:58 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:04:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:01:10 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:03:09 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:06:41 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:00:32 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:09:48 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 08:03:56 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-07 09:08:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-04-07 09:03:14 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:07:12 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:03:18 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:07:19 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:02:45 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-07 09:03:18 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-04-07 09:03:05 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-07 09:03:02 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-04-07 09:03:20 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-04-07 09:05:32 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.041 |  |
| 2026-04-07 09:01:32 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.041 |  |
| 2026-04-07 09:02:14 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2026-04-07 09:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.060 |  |
| 2026-04-07 09:00:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.070 |  |
| 2026-04-07 09:04:05 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.073 |  |
| 2026-04-07 09:05:04 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.099 |  |
| 2026-04-07 09:03:45 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.100 |  |
| 2026-04-07 09:02:20 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.133 |  |
| 2026-04-07 09:04:32 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.379 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)