# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_00:16:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,140 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 00:16:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:13:24 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-01-02 00:11:06 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-01-02 00:08:05 | Thanamalwila (Kirindi Oya) | 2.04 | 🟢 Normal | -0.063 |  |
| 2026-01-02 00:07:06 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-02 00:06:14 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 00:05:52 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 00:05:40 | Padiyathalawa (Maduru Oya) | 4.25 | 🟡 Alert | -0.096 |  |
| 2026-01-02 00:05:31 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:05:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 00:04:40 | Katharagama (Menik Ganga) | 1.20 | 🟢 Normal | -0.069 |  |
| 2026-01-02 00:04:26 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:04:13 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 00:04:07 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-02 00:03:42 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:03:34 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.048 |  |
| 2026-01-02 00:03:31 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 00:03:30 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:03:21 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:03:05 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 00:02:48 | Horowpothana (Yan Oya) | 3.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-02 00:02:48 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-02 00:02:45 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 00:02:17 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.013 |  |
| 2026-01-02 00:02:12 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:02:08 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-01-02 00:01:41 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:01:39 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:01:27 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:01:26 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-01-02 00:00:46 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 23:55:37 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.005 |  |
| 2026-01-01 23:26:07 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:26:05 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 00:05:40 | Padiyathalawa (Maduru Oya) | 4.25 | 🟡 Alert | -0.096 |  |
| 2026-01-02 00:13:24 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-01-02 00:02:48 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-02 00:04:07 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-02 00:07:06 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-02 00:02:48 | Horowpothana (Yan Oya) | 3.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-02 00:02:45 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 00:05:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 00:03:31 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 00:00:46 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 00:04:13 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 00:03:05 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 00:05:52 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 00:06:14 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 00:02:12 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:03:42 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:07:27 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:05:31 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:03:30 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:04:26 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:10:31 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:01:39 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:01:27 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:01:41 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:16:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:03:21 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-01 23:55:37 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.005 |  |
| 2026-01-02 00:01:26 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-01-02 00:02:17 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.013 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-01 20:14:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-02 00:11:06 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-01-02 00:02:08 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-02 00:03:34 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.048 |  |
| 2026-01-02 00:08:05 | Thanamalwila (Kirindi Oya) | 2.04 | 🟢 Normal | -0.063 |  |
| 2026-01-02 00:04:40 | Katharagama (Menik Ganga) | 1.20 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)