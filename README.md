# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_03:18:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,513 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 03:18:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:14:51 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:08:06 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | -0.025 |  |
| 2026-06-26 03:07:48 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.003 |  |
| 2026-06-26 03:07:39 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-06-26 03:07:26 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.038 |  |
| 2026-06-26 03:06:27 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.563 |  |
| 2026-06-26 03:06:24 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -36.000 |  |
| 2026-06-26 03:06:23 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -36.000 |  |
| 2026-06-26 03:06:11 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -60.000 |  |
| 2026-06-26 03:06:08 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -60.000 |  |
| 2026-06-26 03:05:29 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-06-26 03:05:23 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.563 |  |
| 2026-06-26 03:05:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-26 03:04:31 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.005 |  |
| 2026-06-26 03:04:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:03:59 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.083 |  |
| 2026-06-26 03:03:54 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-26 03:03:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-06-26 03:03:17 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:03:14 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.022 |  |
| 2026-06-26 03:03:07 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:56 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:50 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-06-26 03:02:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:45 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:38 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 03:02:21 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -162.000 |  |
| 2026-06-26 03:02:17 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -162.000 |  |
| 2026-06-26 03:02:01 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:01:49 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 03:01:42 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-26 03:01:32 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.040 |  |
| 2026-06-26 03:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.026 |  |
| 2026-06-26 03:01:10 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-26 03:01:05 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:00:56 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 02:52:05 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 02:51:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 02:49:31 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.083 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 03:05:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-26 03:02:38 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 03:01:49 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 03:01:05 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:00:56 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:03:17 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:45 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:14:51 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:18:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:04:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:01 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:56 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:07:48 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.003 |  |
| 2026-06-26 03:04:31 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.005 |  |
| 2026-06-26 03:03:54 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-26 03:01:42 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-26 03:05:29 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-26 02:05:47 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-26 03:01:10 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-26 01:27:35 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.014 |  |
| 2026-06-26 03:03:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-06-26 03:07:39 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-06-26 03:03:14 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.022 |  |
| 2026-06-26 03:08:06 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | -0.025 |  |
| 2026-06-26 03:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.026 |  |
| 2026-06-26 03:07:26 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.038 |  |
| 2026-06-26 03:02:50 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-06-26 03:01:32 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.040 |  |
| 2026-06-26 03:03:59 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.083 |  |
| 2026-06-26 03:06:27 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.563 |  |
| 2026-06-26 03:06:24 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -36.000 |  |
| 2026-06-26 03:06:11 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -60.000 |  |
| 2026-06-26 03:02:21 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -162.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)