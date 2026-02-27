# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_14:16:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,525 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 14:16:05 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.008 |  |
| 2026-02-27 14:14:49 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:13:41 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:10:46 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-02-27 14:09:42 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:06:58 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:06:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:06:37 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:06:36 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:05:44 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:05:39 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:05:35 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:04:20 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:04:13 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:03:57 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:03:47 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:03:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:03:16 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.039 |  |
| 2026-02-27 14:02:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 14:02:20 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:02:18 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -21.484 |  |
| 2026-02-27 14:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 14:02:10 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:02:10 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.015 |  |
| 2026-02-27 14:02:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:01:45 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:01:38 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:01:37 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 14:01:36 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:01:30 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.070 |  |
| 2026-02-27 14:01:28 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2026-02-27 14:01:27 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:01:23 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:01:20 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:01:18 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.003 |  |
| 2026-02-27 14:01:16 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -21.484 |  |
| 2026-02-27 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 14:00:50 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:00:43 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:00:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:39:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 13:30:50 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 14:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 14:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 14:01:37 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 14:02:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 14:02:10 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:00:50 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:01:38 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:00:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:01:23 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:04:13 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:13:41 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:06:37 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:04:20 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:06:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:14:49 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:03:47 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:06:36 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:06:58 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:05:44 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:01:45 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:05:35 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:05:39 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 14:01:18 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.003 |  |
| 2026-02-27 14:16:05 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.008 |  |
| 2026-02-27 13:09:00 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-02-27 14:10:46 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-02-27 14:03:57 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:09:42 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:03:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:02:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:01:27 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:00:43 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:01:20 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:02:20 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-27 14:02:10 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.015 |  |
| 2026-02-27 14:03:16 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.039 |  |
| 2026-02-27 14:01:28 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2026-02-27 14:01:30 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.070 |  |
| 2026-02-27 14:02:18 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -21.484 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)