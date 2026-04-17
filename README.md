# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_14:21:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,580 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 14:21:36 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.008 |  |
| 2026-04-17 14:13:19 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:11:12 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:10:45 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-04-17 14:09:36 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-04-17 14:08:17 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-04-17 14:07:16 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 14:06:32 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-17 14:06:28 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-04-17 14:06:20 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:05:33 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:04:35 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-17 14:04:33 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:04:08 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:03:55 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-04-17 14:03:49 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:03:32 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:03:24 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-17 14:03:23 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:03:20 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:03:13 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-04-17 14:02:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:02:15 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.060 |  |
| 2026-04-17 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-04-17 14:02:08 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:01:58 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.030 |  |
| 2026-04-17 14:01:47 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-17 14:01:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:01:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:01:38 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.053 |  |
| 2026-04-17 14:01:24 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:01:17 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-17 14:01:13 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:01:04 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-04-17 14:00:58 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:00:49 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.020 |  |
| 2026-04-17 14:00:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:00:24 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 14:01:47 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-17 14:03:24 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-17 14:04:35 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-17 14:06:32 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-17 14:07:16 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 14:05:33 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:01:13 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 13:18:53 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:02:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:13:19 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:03:32 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:03:23 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:00:24 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:04:08 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:03:20 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:06:20 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:11:12 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:02:08 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-17 14:21:36 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.008 |  |
| 2026-04-17 14:10:45 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-04-17 14:09:36 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-04-17 14:04:33 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:03:49 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:01:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:00:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:01:24 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-17 14:03:13 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-04-17 14:03:55 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-04-17 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-04-17 14:06:28 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-04-17 14:01:04 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-04-17 14:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-17 14:01:17 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-17 14:00:49 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.020 |  |
| 2026-04-17 14:08:17 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-04-17 14:01:58 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.030 |  |
| 2026-04-17 14:01:38 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.053 |  |
| 2026-04-17 14:02:15 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)