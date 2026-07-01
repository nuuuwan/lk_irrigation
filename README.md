# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_05:13:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,939 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 05:13:30 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:12:54 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:12:31 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-07-02 05:10:28 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-07-02 05:10:09 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-02 05:09:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:07:04 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-07-02 05:06:38 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:06:37 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:05:57 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-02 05:05:24 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:04:45 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-02 05:04:24 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 05:04:10 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:04:10 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-07-02 05:04:05 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-07-02 05:03:40 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.033 |  |
| 2026-07-02 05:03:30 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:02:56 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.012 |  |
| 2026-07-02 05:02:45 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:02:30 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 05:02:23 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:02:20 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-07-02 05:02:19 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -1.059 |  |
| 2026-07-02 05:01:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-07-02 05:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -1.059 |  |
| 2026-07-02 05:01:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:01:05 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-02 05:00:21 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.144 |  |
| 2026-07-02 04:48:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.083 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 05:10:09 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-02 05:05:57 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-02 03:10:21 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-02 05:01:05 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-02 05:02:30 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 05:04:24 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:01:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:02:23 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:02:45 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:12:54 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:13:30 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:06:38 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-02 03:05:51 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 04:09:43 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-07-02 04:03:44 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:09:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:02:19 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 03:02:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:05:24 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:04:10 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:03:30 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 03:06:06 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-02 05:04:45 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-02 05:04:05 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-07-02 05:02:20 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-07-02 05:12:31 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-07-02 05:02:56 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.012 |  |
| 2026-07-02 05:10:28 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-07-02 05:04:10 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-07-02 05:07:04 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-07-02 05:01:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-07-02 05:03:40 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.033 |  |
| 2026-07-02 03:07:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.073 |  |
| 2026-07-02 05:00:21 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.144 |  |
| 2026-07-02 05:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -1.059 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)