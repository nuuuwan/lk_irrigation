# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_11:10:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 11:10:19 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | 101.288 | 🔺 Rising |
| 2026-02-22 11:10:03 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.149 |  |
| 2026-02-22 11:09:20 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 101.288 | 🔺 Rising |
| 2026-02-22 11:09:02 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.062 |  |
| 2026-02-22 11:08:33 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.018 |  |
| 2026-02-22 11:08:30 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-22 11:07:30 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.119 |  |
| 2026-02-22 11:07:23 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.036 |  |
| 2026-02-22 11:07:02 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.037 |  |
| 2026-02-22 11:05:34 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 11:05:08 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.718 | 🔺 Rising |
| 2026-02-22 11:04:57 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.068 |  |
| 2026-02-22 11:04:18 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.127 |  |
| 2026-02-22 11:04:17 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.146 |  |
| 2026-02-22 11:04:04 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.089 |  |
| 2026-02-22 11:03:43 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.109 |  |
| 2026-02-22 11:03:41 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.156 |  |
| 2026-02-22 11:03:30 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-22 11:03:14 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-02-22 11:03:12 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-22 11:03:09 | Weraganthota (Mahaweli Ganga) | -1.03 | 🟢 Normal | -0.067 |  |
| 2026-02-22 11:03:00 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.060 |  |
| 2026-02-22 11:02:58 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-02-22 11:02:54 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.160 |  |
| 2026-02-22 11:02:40 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-02-22 11:02:39 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 11:02:39 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-22 11:02:35 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-22 11:02:32 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-02-22 11:02:31 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-02-22 11:02:24 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-22 11:02:14 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2026-02-22 11:02:11 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-02-22 11:01:53 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 11:01:42 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-22 11:01:40 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-02-22 11:01:18 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-22 11:01:06 | Manampitiya (Mahaweli Ganga) | 4.31 | 🟠 Minor Flood | -0.070 |  |
| 2026-02-22 11:00:46 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 11:01:06 | Manampitiya (Mahaweli Ganga) | 4.31 | 🟠 Minor Flood | -0.070 |  |
| 2026-02-22 11:10:19 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | 101.288 | 🔺 Rising |
| 2026-02-22 11:05:08 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.718 | 🔺 Rising |
| 2026-02-22 11:02:40 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-02-22 11:02:24 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-22 10:15:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-22 11:02:39 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-22 11:01:18 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-22 11:02:35 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-22 11:03:12 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-22 11:05:34 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 11:00:46 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 11:02:39 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 11:01:53 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 11:03:30 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-22 11:08:30 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-22 11:02:58 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-02-22 11:01:42 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-22 11:08:33 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.018 |  |
| 2026-02-22 11:02:32 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-02-22 11:02:11 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-02-22 11:03:14 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-02-22 11:07:23 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.036 |  |
| 2026-02-22 11:07:02 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.037 |  |
| 2026-02-22 11:01:40 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-02-22 11:02:14 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2026-02-22 11:03:00 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.060 |  |
| 2026-02-22 11:09:02 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.062 |  |
| 2026-02-22 11:03:09 | Weraganthota (Mahaweli Ganga) | -1.03 | 🟢 Normal | -0.067 |  |
| 2026-02-22 11:04:57 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.068 |  |
| 2026-02-22 11:04:04 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.089 |  |
| 2026-02-22 11:02:31 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-02-22 11:03:43 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.109 |  |
| 2026-02-22 11:07:30 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.119 |  |
| 2026-02-22 11:04:18 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.127 |  |
| 2026-02-22 11:04:17 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.146 |  |
| 2026-02-22 11:10:03 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.149 |  |
| 2026-02-22 11:03:41 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.156 |  |
| 2026-02-22 11:02:54 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)