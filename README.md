# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_21:40:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,222 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 21:40:06 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:13:40 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-02 21:13:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-05-02 21:11:19 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:08:28 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-05-02 21:06:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-02 21:06:35 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-02 21:06:29 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-02 21:06:24 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-05-02 21:06:16 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:06:02 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:05:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:05:28 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:04:27 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-02 21:04:25 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:04:20 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.054 |  |
| 2026-05-02 21:04:15 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-05-02 21:04:12 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-05-02 21:03:34 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-02 21:03:21 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-05-02 21:03:14 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-02 21:03:14 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-05-02 21:03:06 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.021 |  |
| 2026-05-02 21:02:46 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:02:39 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.050 |  |
| 2026-05-02 21:02:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-05-02 21:02:30 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-05-02 21:02:15 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:02:12 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 21:02:08 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:51 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:30 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 21:01:24 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:17 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:13 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.123 |  |
| 2026-05-02 21:00:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 21:01:30 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 21:13:40 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-02 21:06:35 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-02 21:06:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-02 21:03:14 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-02 21:02:12 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 21:00:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 21:04:25 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:02:46 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:02:15 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:24 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:17 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:40:06 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:05:28 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:05:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:06:02 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:11:19 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:51 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-02 21:03:34 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-02 21:06:29 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-02 21:04:27 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-02 21:03:21 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-05-02 21:04:15 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-05-02 21:06:24 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-05-02 21:13:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-05-02 21:03:14 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-05-02 21:08:28 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-05-02 21:02:30 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-05-02 21:04:12 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-05-02 21:03:06 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.021 |  |
| 2026-05-02 21:02:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-05-02 21:02:39 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.050 |  |
| 2026-05-02 21:04:20 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.054 |  |
| 2026-05-02 21:01:13 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.123 |  |
| 2026-05-02 20:09:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)