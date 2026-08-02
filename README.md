# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_23:16:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,290 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 23:16:51 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.101 |  |
| 2026-08-02 23:15:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-02 23:13:02 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.046 |  |
| 2026-08-02 23:12:43 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:12:38 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:08:59 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-02 23:08:14 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-02 23:06:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 23:06:42 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-08-02 23:06:41 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-08-02 23:06:41 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:06:28 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-02 23:06:19 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-02 23:05:59 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | 0.577 | 🔺 Rising |
| 2026-08-02 23:05:22 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:05:18 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-02 23:05:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:04:49 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 23:04:39 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-08-02 23:04:14 | Nawalapitiya (Mahaweli Ganga) | 4.05 | 🟡 Alert | 0.435 | 🔺 Rising |
| 2026-08-02 23:03:48 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:03:32 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:03:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:03:05 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-02 23:02:58 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-08-02 23:02:47 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:02:39 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:02:16 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-08-02 23:01:43 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:01:27 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:01:11 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:01:10 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:00:55 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:00:33 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 23:04:14 | Nawalapitiya (Mahaweli Ganga) | 4.05 | 🟡 Alert | 0.435 | 🔺 Rising |
| 2026-08-02 23:05:59 | Kithulgala (Kelani Ganga) | 2.75 | 🟢 Normal | 0.577 | 🔺 Rising |
| 2026-08-02 23:06:42 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-08-02 23:04:39 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-08-02 22:21:52 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-08-02 23:08:59 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-02 23:06:41 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-08-02 23:06:28 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-02 23:08:14 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-02 23:03:05 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-02 23:06:19 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-02 22:01:22 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-02 23:15:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-02 23:06:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 23:04:49 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 23:00:55 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:01:10 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:01:43 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:03:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:00:33 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:03:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:01:27 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:06:41 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:03:48 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:02:47 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:05:22 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:03:32 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:05:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:02:39 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:00:59 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:12:38 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:01:11 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:12:43 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:05:18 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-02 23:02:58 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-08-02 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-02 23:02:16 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-08-02 23:13:02 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.046 |  |
| 2026-08-02 23:16:51 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)