# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_20:24:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,459 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 20:24:52 | Padiyathalawa (Maduru Oya) | 1.95 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-20 20:11:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-20 20:10:43 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 20:10:30 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 20:10:23 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 20:09:52 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-20 20:09:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:09:28 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.038 |  |
| 2026-02-20 20:09:23 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-20 20:08:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:08:04 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 20:07:52 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:07:47 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:07:05 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.160 |  |
| 2026-02-20 20:05:40 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:05:19 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 20:04:41 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-20 20:04:21 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:04:01 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.033 |  |
| 2026-02-20 20:03:52 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:03:27 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.049 |  |
| 2026-02-20 20:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-02-20 20:02:53 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-02-20 20:02:51 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:42 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.039 |  |
| 2026-02-20 20:02:37 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-02-20 20:02:27 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:24 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.575 | 🔺 Rising |
| 2026-02-20 20:02:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:19 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:04 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-02-20 20:02:02 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:01:52 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:00:55 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-20 20:00:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 19:53:01 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.575 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 20:02:04 | Manampitiya (Mahaweli Ganga) | 3.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-02-20 20:02:24 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.575 | 🔺 Rising |
| 2026-02-20 20:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-02-20 20:11:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-20 20:09:52 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-20 20:24:52 | Padiyathalawa (Maduru Oya) | 1.95 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-20 20:09:23 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-20 20:10:30 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 20:08:04 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 20:00:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 20:05:19 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 20:10:43 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 20:10:23 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 20:07:47 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:03:52 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:02 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:01:52 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:07:52 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:19 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:05:40 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:08:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:51 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:27 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:09:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:04:21 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:02:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-20 20:04:41 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-20 20:00:55 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-20 20:02:53 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-02-20 20:04:01 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.033 |  |
| 2026-02-20 20:09:28 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.038 |  |
| 2026-02-20 20:02:42 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.039 |  |
| 2026-02-20 20:03:27 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.049 |  |
| 2026-02-20 20:02:37 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-20 20:07:05 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)