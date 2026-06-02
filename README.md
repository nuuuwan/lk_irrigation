# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_16:05:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 16:05:53 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:05:47 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:05:16 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:05:16 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.081 |  |
| 2026-06-02 16:05:06 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-06-02 16:05:04 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.038 |  |
| 2026-06-02 16:04:54 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:04:46 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-06-02 16:04:45 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:03:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-06-02 16:03:48 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:03:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-02 16:03:16 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-02 16:03:08 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:02:58 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-02 16:02:45 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:02:37 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:02:35 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-02 16:02:29 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-06-02 16:02:15 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:02:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:01:45 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:01:22 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.010 |  |
| 2026-06-02 16:01:20 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:01:13 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:00:29 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:00:16 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:00:16 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 15:32:22 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 15:05:39 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-02 16:02:58 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-02 15:07:09 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 16:02:37 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:03:08 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:03:48 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 16:04:45 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 15:05:15 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-02 16:05:53 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:00:16 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:01:20 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:00:16 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:01:45 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 15:02:21 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:05:16 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 15:06:55 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-02 15:03:49 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:05:47 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:01:13 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 15:00:21 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:02:15 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:02:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:04:54 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:02:45 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:00:29 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-02 15:06:17 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-02 16:01:22 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.010 |  |
| 2026-06-02 16:03:16 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-02 16:02:35 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-02 16:03:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-02 15:01:16 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-06-02 16:02:29 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-06-02 16:05:06 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-06-02 15:00:39 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | -0.027 |  |
| 2026-06-02 16:04:46 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-06-02 16:03:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-06-02 16:05:04 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.038 |  |
| 2026-06-02 16:05:16 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)