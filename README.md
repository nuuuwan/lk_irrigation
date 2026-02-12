# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_20:21:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 20:21:44 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:20:37 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:19:13 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:15:29 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-12 20:13:46 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-12 20:13:44 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-12 20:11:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-12 20:09:31 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-02-12 20:07:09 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-02-12 20:06:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 20:06:42 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:06:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 20:06:21 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-12 20:06:17 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:06:01 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 20:05:32 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-12 20:05:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:05:14 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-12 20:05:12 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.019 |  |
| 2026-02-12 20:04:49 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-02-12 20:04:26 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:04:00 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 20:03:37 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-12 20:03:04 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-12 20:02:35 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:02:26 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:01:59 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.013 |  |
| 2026-02-12 20:01:50 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 20:01:46 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:01:43 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:01:34 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:01:25 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:01:14 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-02-12 20:00:44 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.045 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 20:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-02-12 20:04:49 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-02-12 20:01:14 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-02-12 20:05:32 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-12 20:05:14 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-12 20:13:46 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-12 20:13:44 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-12 20:03:37 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-12 20:04:00 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 20:11:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-12 20:06:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 20:06:21 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 20:06:57 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 20:01:50 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 20:06:01 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 20:15:29 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-12 20:01:34 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:01:46 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:19:13 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:04:26 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:02:35 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:20:37 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:05:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:21:44 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:01:25 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:02:26 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:06:42 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:09:31 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:01:43 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:06:17 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-12 20:07:09 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-02-12 20:03:04 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-12 20:01:59 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.013 |  |
| 2026-02-12 20:05:12 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.019 |  |
| 2026-02-12 20:00:44 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.045 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)