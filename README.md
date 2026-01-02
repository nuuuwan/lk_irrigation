# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_11:18:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,553 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 11:18:45 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:17:04 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:16:49 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:10:53 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:08:20 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-01-02 11:08:02 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.044 |  |
| 2026-01-02 11:07:40 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:07:30 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 11:07:12 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:06:19 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.018 |  |
| 2026-01-02 11:06:12 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-01-02 11:06:08 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:06:07 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-02 11:05:47 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-01-02 11:05:36 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:04:54 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.097 |  |
| 2026-01-02 11:04:45 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:04:24 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-02 11:03:41 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:03:39 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:03:34 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-01-02 11:03:28 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:02:33 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.103 |  |
| 2026-01-02 11:02:32 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:02:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-01-02 11:02:19 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-01-02 11:02:19 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:02:16 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:02:11 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-02 11:01:50 | Horowpothana (Yan Oya) | 3.32 | 🟢 Normal | -0.128 |  |
| 2026-01-02 11:01:36 | Siyambalanduwa (Heda Oya) | 1.62 | 🟢 Normal | -0.069 |  |
| 2026-01-02 11:01:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-02 11:01:22 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-01-02 11:01:04 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:00:15 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-01-02 10:47:00 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:46:59 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:46:57 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 11:02:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-01-02 11:06:12 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-01-02 11:01:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-02 11:02:11 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-02 11:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-02 11:07:30 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 11:06:07 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-02 11:02:32 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:06:54 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:10:53 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:07:12 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:03:41 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:03:28 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:02:19 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:04:45 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:07:40 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:01:04 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:03:39 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:18:45 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 10:02:33 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:14:27 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.004 |  |
| 2026-01-02 11:08:20 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-01-02 11:06:08 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:00:15 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:05:36 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:02:16 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:04:24 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:01:22 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-02 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-01-02 11:06:19 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.018 |  |
| 2026-01-02 11:05:47 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-01-02 11:03:34 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-01-02 11:02:19 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-01-02 11:08:02 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.044 |  |
| 2026-01-02 11:01:36 | Siyambalanduwa (Heda Oya) | 1.62 | 🟢 Normal | -0.069 |  |
| 2026-01-02 11:04:54 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.097 |  |
| 2026-01-02 11:02:33 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.103 |  |
| 2026-01-02 11:01:50 | Horowpothana (Yan Oya) | 3.32 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)