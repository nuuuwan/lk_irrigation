# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_17:20:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,068 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 17:20:26 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:17:10 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.044 |  |
| 2026-05-02 17:14:11 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:12:05 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:12:02 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-05-02 17:10:37 | Kithulgala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:10:32 | Kithulgala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:09:05 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:08:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-05-02 17:08:50 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-02 17:08:31 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:07:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.133 |  |
| 2026-05-02 17:07:29 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:07:25 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:06:31 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:06:10 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-05-02 17:06:05 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.087 |  |
| 2026-05-02 17:05:25 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:05:08 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.005 |  |
| 2026-05-02 17:05:03 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:05:02 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:04:57 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.077 |  |
| 2026-05-02 17:04:27 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:04:13 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:03:45 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 17:03:29 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-05-02 17:02:55 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:02:44 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-02 17:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-05-02 17:02:25 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:02:22 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:01:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:01:44 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:01:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 17:01:27 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:01:12 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.031 |  |
| 2026-05-02 17:00:53 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:00:27 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 17:12:02 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-05-02 16:15:18 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-02 17:02:44 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-02 17:01:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 17:03:45 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 17:08:50 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-02 16:19:10 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-02 17:10:37 | Kithulgala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:02:25 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:02:55 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:01:44 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:05:03 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:14:11 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:05:02 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:01:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:02:22 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:04:27 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:07:29 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:09:05 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:00:53 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:08:31 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:20:26 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:06:31 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-02 17:05:08 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.005 |  |
| 2026-05-02 17:08:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-05-02 17:12:05 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:05:25 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:04:13 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:07:25 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:00:27 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-02 17:06:10 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-05-02 17:03:29 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-05-02 17:01:12 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.031 |  |
| 2026-05-02 17:17:10 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.044 |  |
| 2026-05-02 17:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-05-02 17:04:57 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.077 |  |
| 2026-05-02 17:06:05 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.087 |  |
| 2026-05-02 17:07:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)