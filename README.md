# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_22:28:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,722 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 22:28:41 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:27:48 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:26:26 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:15:14 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:13:56 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-02-28 22:13:34 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-02-28 22:11:32 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:08:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-28 22:08:11 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.018 |  |
| 2026-02-28 22:06:08 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 2.764 | 🔺 Rising |
| 2026-02-28 22:05:49 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-28 22:05:47 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-28 22:05:32 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-28 22:05:04 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-02-28 22:04:59 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:04:20 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:03:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-28 22:03:48 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-28 22:03:43 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:03:35 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:03:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:02:42 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:02:27 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:02:11 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:02:03 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-28 22:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:01:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:01:39 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 22:01:38 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:01:29 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:00:54 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:00:53 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:00:36 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:00:11 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 22:06:08 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 2.764 | 🔺 Rising |
| 2026-02-28 22:05:04 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-02-28 22:08:29 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-28 22:03:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-28 18:00:50 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-28 21:06:36 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-28 22:05:49 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-28 22:05:32 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-28 22:01:39 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 22:05:47 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-28 22:01:29 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:00:11 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:00:54 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:01:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:02:27 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:03:35 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:00:36 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:04:16 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:15:14 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:03:43 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:27:48 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:26:26 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:04:59 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:01:38 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:03:30 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:28:41 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-28 21:02:32 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:02:42 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:04:20 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:02:11 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:17:10 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:11:32 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:13:34 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-02-28 22:03:48 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-28 22:02:03 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-28 22:13:56 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-02-28 22:08:11 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.018 |  |
| 2026-02-28 20:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.028 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)