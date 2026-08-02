# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_22:21:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 22:21:52 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-08-02 22:17:56 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:15:58 | Nawalapitiya (Mahaweli Ganga) | 3.70 | 🟡 Alert | 0.802 | 🔺 Rising |
| 2026-08-02 22:14:50 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-08-02 22:08:24 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.027 |  |
| 2026-08-02 22:08:19 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-02 22:08:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:07:07 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-02 22:06:10 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-08-02 22:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-02 22:05:49 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.041 |  |
| 2026-08-02 22:05:43 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.159 |  |
| 2026-08-02 22:05:37 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-02 22:05:33 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-08-02 22:05:31 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:05:26 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 22:04:17 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:04:16 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:04:13 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 22:04:03 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-08-02 22:03:38 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:03:24 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-02 22:02:59 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:02:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:02:14 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-02 22:02:07 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-08-02 22:01:42 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-02 22:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:01:22 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-02 22:01:19 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 22:01:09 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:01:05 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 22:00:52 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:00:38 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:00:18 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-02 21:59:12 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 22:15:58 | Nawalapitiya (Mahaweli Ganga) | 3.70 | 🟡 Alert | 0.802 | 🔺 Rising |
| 2026-08-02 22:06:10 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-08-02 22:04:03 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-08-02 22:05:33 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-08-02 22:14:50 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-08-02 22:21:52 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-08-02 22:05:37 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-02 22:03:24 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-02 22:01:22 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-02 22:07:07 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-02 22:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-02 22:01:05 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 22:05:26 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 22:04:13 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 22:01:19 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 22:03:38 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:00:18 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:00:52 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:00:38 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:04:16 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:08:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:03:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 21:59:12 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:04:17 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:17:56 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:02:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:02:59 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:01:09 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:00:59 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:05:31 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 22:08:19 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-02 22:02:07 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-08-02 22:01:42 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-02 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-02 22:08:24 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.027 |  |
| 2026-08-02 22:02:14 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-02 22:05:49 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.041 |  |
| 2026-08-02 22:05:43 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)