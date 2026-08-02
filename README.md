# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_13:24:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 13:24:42 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:12:57 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-08-02 13:10:06 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:08:03 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.075 |  |
| 2026-08-02 13:08:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:07:42 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.023 |  |
| 2026-08-02 13:07:27 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.028 |  |
| 2026-08-02 13:07:21 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-02 13:06:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-08-02 13:06:04 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:05:31 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:05:31 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.054 |  |
| 2026-08-02 13:04:52 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:04:32 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-08-02 13:04:19 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:04:16 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.090 |  |
| 2026-08-02 13:03:32 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.059 |  |
| 2026-08-02 13:03:18 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-02 13:03:12 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:02:52 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-08-02 13:02:43 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-02 13:02:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-02 13:02:29 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:02:19 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:02:14 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-08-02 13:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:01:42 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-02 13:01:33 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-02 13:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.061 |  |
| 2026-08-02 13:01:15 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:01:11 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.110 |  |
| 2026-08-02 13:00:53 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:00:45 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:00:34 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 13:02:52 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-08-02 13:02:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-02 13:07:21 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-02 13:03:18 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-02 13:02:43 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-02 13:02:19 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:00:45 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:05:31 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:08:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:00:34 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:10:06 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:02:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:02:29 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:04:19 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:06:04 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:04:52 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:01:15 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:05:31 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:00:53 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:24:42 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:04:27 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 12:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:03:12 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:12:57 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-08-02 13:01:33 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-02 13:01:42 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-02 13:04:32 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-08-02 13:02:14 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-08-02 13:07:42 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.023 |  |
| 2026-08-02 13:07:27 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.028 |  |
| 2026-08-02 13:06:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-08-02 13:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.054 |  |
| 2026-08-02 13:03:32 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.059 |  |
| 2026-08-02 13:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.061 |  |
| 2026-08-02 13:08:03 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.075 |  |
| 2026-08-02 13:04:16 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.090 |  |
| 2026-08-02 13:01:11 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.110 |  |
| 2026-08-02 12:01:47 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)