# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_00:04:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,308 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 00:04:01 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.878 | 🔺 Rising |
| 2026-05-03 00:03:22 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:03:14 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 00:03:13 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-03 00:03:06 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-05-03 00:02:51 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-05-03 00:02:38 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:02:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.050 |  |
| 2026-05-03 00:02:28 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:02:16 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.027 |  |
| 2026-05-03 00:02:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-03 00:01:44 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:01:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-03 00:01:18 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:01:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 00:01:16 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:00:51 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:00:48 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-03 00:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:00:12 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.013 |  |
| 2026-05-02 23:46:15 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.878 | 🔺 Rising |
| 2026-05-02 23:40:51 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-02 23:39:48 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.027 |  |
| 2026-05-02 23:27:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.034 |  |
| 2026-05-02 23:26:39 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-02 23:24:31 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:19:25 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-05-02 23:14:57 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:13:48 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 00:04:01 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.878 | 🔺 Rising |
| 2026-05-02 23:19:25 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-05-03 00:00:48 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-02 23:04:34 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-02 23:26:39 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-03 00:01:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-02 23:40:51 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-03 00:01:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 00:03:14 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 23:01:56 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:00:51 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:02:10 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:01:44 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:01:16 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:17 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:14:57 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:02:36 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:08:22 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:02:28 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:02:38 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:03:37 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:24:31 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:03:22 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-02 23:04:22 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:01:18 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 22:06:49 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-03 00:03:13 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-03 00:02:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-03 00:03:06 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-05-03 00:00:12 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.013 |  |
| 2026-05-03 00:02:16 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.027 |  |
| 2026-05-03 00:02:51 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-05-02 23:05:20 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.049 |  |
| 2026-05-03 00:02:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.050 |  |
| 2026-05-02 20:09:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)