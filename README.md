# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_01:32:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 01:32:45 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:14:11 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.100 |  |
| 2026-01-02 01:12:30 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.017 |  |
| 2026-01-02 01:09:25 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-02 01:08:20 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:07:21 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-01-02 01:06:47 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-02 01:05:40 | Katharagama (Menik Ganga) | 1.13 | 🟢 Normal | -0.069 |  |
| 2026-01-02 01:05:24 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 01:04:32 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 01:04:11 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:03:40 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:03:38 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:03:37 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-02 01:03:31 | Siyambalanduwa (Heda Oya) | 2.01 | 🟢 Normal | 0.635 | 🔺 Rising |
| 2026-01-02 01:03:25 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:03:22 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-02 01:02:47 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-02 01:02:39 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-02 01:02:21 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:02:08 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.062 |  |
| 2026-01-02 01:02:05 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-02 01:01:30 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 01:01:06 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:00:56 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:00:46 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-02 01:00:20 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 00:05:40 | Padiyathalawa (Maduru Oya) | 4.25 | 🟡 Alert | -0.096 |  |
| 2026-01-02 01:03:31 | Siyambalanduwa (Heda Oya) | 2.01 | 🟢 Normal | 0.635 | 🔺 Rising |
| 2026-01-02 01:07:21 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-01-02 01:03:22 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-02 01:02:05 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-02 00:04:07 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-02 01:02:39 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-02 00:02:48 | Horowpothana (Yan Oya) | 3.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-02 01:05:24 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 01:04:32 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 01:01:30 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 01:09:25 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-02 01:03:25 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:04:11 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:05:31 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:02:21 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:03:40 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:08:20 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:01:06 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:00:56 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-02 00:16:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:03:38 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:00:46 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:32:45 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-02 01:02:47 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-02 01:03:37 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-02 01:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-02 01:12:30 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.017 |  |
| 2026-01-02 01:06:47 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-02 01:00:20 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-01-01 20:14:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-01-02 00:11:06 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-02 00:03:34 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.048 |  |
| 2026-01-02 01:02:08 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.062 |  |
| 2026-01-02 01:05:40 | Katharagama (Menik Ganga) | 1.13 | 🟢 Normal | -0.069 |  |
| 2026-01-02 01:14:11 | Thanamalwila (Kirindi Oya) | 1.93 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)