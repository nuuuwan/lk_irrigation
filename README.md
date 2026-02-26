# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_22:17:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,932 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 22:17:35 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-02-26 22:14:31 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.006 |  |
| 2026-02-26 22:13:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-26 22:13:13 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-26 22:09:19 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-26 22:09:00 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-26 22:07:28 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.018 |  |
| 2026-02-26 22:06:59 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-02-26 22:06:55 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-02-26 22:06:37 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-02-26 22:04:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-26 22:04:33 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:04:17 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:04:16 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:04:01 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:03:30 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:03:23 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 22:02:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:53 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:40 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-26 22:02:36 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:20 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-26 22:02:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:02:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:35 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:29 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:14 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-26 22:01:11 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:11 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:01:07 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:01:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-02-26 22:00:37 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:00:36 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 22:06:55 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-26 22:01:14 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-26 22:09:19 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-26 22:13:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-26 22:04:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-26 22:00:36 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 22:03:23 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 22:09:00 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-26 22:02:40 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-26 22:02:20 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-26 22:01:07 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:01:11 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:02:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:04:16 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:13:13 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-26 22:01:29 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:04:01 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:35 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:03:30 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:53 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:36 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:11 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:04:17 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:04:33 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:00:37 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:14:31 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.006 |  |
| 2026-02-26 22:17:35 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-02-26 22:01:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-02-26 22:07:28 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.018 |  |
| 2026-02-26 22:06:37 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-02-26 22:06:59 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)