# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_04:08:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,647 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 04:08:22 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.085 |  |
| 2026-02-22 04:08:01 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-22 04:07:54 | Thawalama (Gin Ganga) | 3.28 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-22 04:07:19 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-02-22 04:07:01 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.121 |  |
| 2026-02-22 04:06:59 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-22 04:06:35 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.092 |  |
| 2026-02-22 04:06:17 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.645 |  |
| 2026-02-22 04:06:13 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.068 |  |
| 2026-02-22 04:05:54 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-22 04:05:29 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.256 |  |
| 2026-02-22 04:04:55 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.041 |  |
| 2026-02-22 04:04:37 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.087 |  |
| 2026-02-22 04:04:22 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-22 04:03:58 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 04:03:40 | Manampitiya (Mahaweli Ganga) | 4.18 | 🟡 Alert | 0.183 | 🔺 Rising |
| 2026-02-22 04:03:24 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-22 04:03:23 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-02-22 04:03:15 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | -0.030 |  |
| 2026-02-22 04:02:47 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 04:02:46 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.384 | 🔺 Rising |
| 2026-02-22 04:02:44 | Kuda Oya (Kirindi Oya) | 3.16 | 🟢 Normal | -0.285 |  |
| 2026-02-22 04:02:39 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | -0.090 |  |
| 2026-02-22 04:02:36 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-22 04:02:20 | Thanamalwila (Kirindi Oya) | 2.80 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-02-22 04:01:56 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-22 04:01:41 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 04:01:40 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-22 04:01:28 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 04:00:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.196 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 04:03:40 | Manampitiya (Mahaweli Ganga) | 4.18 | 🟡 Alert | 0.183 | 🔺 Rising |
| 2026-02-22 03:09:14 | Urawa (Nilwala Ganga) | 2.81 | 🟡 Alert | -0.112 |  |
| 2026-02-22 04:07:19 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-02-22 04:02:46 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.384 | 🔺 Rising |
| 2026-02-22 04:03:23 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-02-22 04:02:20 | Thanamalwila (Kirindi Oya) | 2.80 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-02-22 04:00:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-02-22 04:07:54 | Thawalama (Gin Ganga) | 3.28 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-02-22 04:03:24 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-22 03:06:55 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-22 03:02:18 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-22 04:06:59 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-22 04:05:54 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-22 04:04:22 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-22 04:01:56 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-22 04:08:01 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-22 04:01:41 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 04:02:47 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 04:03:58 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 04:02:36 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-22 04:01:28 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:01:22 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-22 04:01:40 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-22 03:04:51 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-22 04:03:15 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | -0.030 |  |
| 2026-02-22 04:04:55 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.041 |  |
| 2026-02-22 03:05:01 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.053 |  |
| 2026-02-22 04:06:13 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.068 |  |
| 2026-02-22 04:08:22 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.085 |  |
| 2026-02-22 04:04:37 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.087 |  |
| 2026-02-22 04:02:39 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | -0.090 |  |
| 2026-02-22 04:06:35 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.092 |  |
| 2026-02-22 04:07:01 | Rathnapura (Kalu Ganga) | 4.85 | 🟢 Normal | -0.121 |  |
| 2026-02-22 04:05:29 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.256 |  |
| 2026-02-22 04:02:44 | Kuda Oya (Kirindi Oya) | 3.16 | 🟢 Normal | -0.285 |  |
| 2026-02-22 04:06:17 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.645 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)