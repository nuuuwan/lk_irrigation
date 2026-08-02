# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_12:16:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,882 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 12:16:03 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 12:14:26 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | -0.017 |  |
| 2026-08-02 12:09:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -4.500 |  |
| 2026-08-02 12:08:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | -4.500 |  |
| 2026-08-02 12:08:44 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:06:47 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-02 12:06:11 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:05:47 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:05:32 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:04:49 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-02 12:04:29 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-02 12:04:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-08-02 12:04:27 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:04:23 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.030 |  |
| 2026-08-02 12:04:12 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-08-02 12:04:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:04:08 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 12:04:03 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.108 |  |
| 2026-08-02 12:03:55 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:03:47 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-08-02 12:03:44 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:03:40 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:03:13 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 12:03:08 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-02 12:02:59 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-08-02 12:02:47 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-02 12:02:36 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.060 |  |
| 2026-08-02 12:02:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:47 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.112 |  |
| 2026-08-02 12:01:44 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-08-02 12:01:42 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-02 12:01:28 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:24 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:23 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:13 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-02 12:01:08 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.034 |  |
| 2026-08-02 12:00:30 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 12:04:29 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-02 12:02:47 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-02 12:01:13 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-02 12:01:42 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-02 12:03:13 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 12:16:03 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 12:04:08 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 12:06:47 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-02 12:01:23 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:28 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:03:44 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:24 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:02:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:03:55 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:05:47 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:06:11 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:08:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:02:36 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:05:32 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:04:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:00:30 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:03:40 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:04:27 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:08:44 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:04:49 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-02 12:03:08 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-02 12:02:59 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-08-02 12:14:26 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | -0.017 |  |
| 2026-08-02 12:01:44 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-08-02 12:03:47 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-08-02 12:04:12 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-08-02 12:04:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-08-02 12:04:23 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.030 |  |
| 2026-08-02 12:01:08 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.034 |  |
| 2026-08-02 12:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.060 |  |
| 2026-08-02 12:04:03 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.108 |  |
| 2026-08-02 12:01:47 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.112 |  |
| 2026-08-02 12:09:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -4.500 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)