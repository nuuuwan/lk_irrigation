# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_18:11:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,290 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 18:11:23 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-21 18:10:23 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:09:22 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 18:08:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.060 |  |
| 2026-04-21 18:08:14 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-04-21 18:07:42 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.018 |  |
| 2026-04-21 18:07:24 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.088 |  |
| 2026-04-21 18:05:38 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.112 |  |
| 2026-04-21 18:05:30 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:05:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:05:11 | Thalgahagoda (Nilwala Ganga) | 2.55 | 🟠 Minor Flood | 2.112 | 🔺 Rising |
| 2026-04-21 18:04:54 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 18:04:39 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.052 |  |
| 2026-04-21 18:04:39 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-04-21 18:04:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:04:17 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 18:03:57 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 18:03:41 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.060 |  |
| 2026-04-21 18:03:31 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.069 |  |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 18:03:02 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:02:47 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-04-21 18:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-21 18:02:33 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-04-21 18:02:21 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.049 |  |
| 2026-04-21 18:02:12 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.301 |  |
| 2026-04-21 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:43 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 18:01:34 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.044 |  |
| 2026-04-21 18:01:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:01 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:00 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-21 18:00:59 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 18:00:17 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.042 |  |
| 2026-04-21 18:00:13 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-21 18:00:07 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | 0.887 | 🔺 Rising |
| 2026-04-21 17:58:11 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-21 17:52:47 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.111 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 18:05:11 | Thalgahagoda (Nilwala Ganga) | 2.55 | 🟠 Minor Flood | 2.112 | 🔺 Rising |
| 2026-04-21 18:00:07 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | 0.887 | 🔺 Rising |
| 2026-04-21 17:58:11 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 18:01:00 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-21 18:00:13 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 18:09:22 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 18:04:54 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 18:01:43 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 18:04:17 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 18:03:57 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 18:01:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:01 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:05:30 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:04:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:05:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:10:23 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:00:59 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-21 18:11:23 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-21 18:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-21 18:04:39 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2026-04-21 18:07:42 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.018 |  |
| 2026-04-21 18:08:14 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-04-21 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-04-21 18:02:47 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-04-21 18:02:33 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-04-21 16:00:51 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-04-21 18:00:17 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.042 |  |
| 2026-04-21 18:01:34 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.044 |  |
| 2026-04-21 18:02:21 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.049 |  |
| 2026-04-21 18:04:39 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.052 |  |
| 2026-04-21 18:03:41 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | -0.060 |  |
| 2026-04-21 18:08:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.060 |  |
| 2026-04-21 18:03:31 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.069 |  |
| 2026-04-21 18:07:24 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.088 |  |
| 2026-04-21 18:05:38 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.112 |  |
| 2026-04-21 18:02:12 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.301 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)