# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_14:12:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 14:12:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-02 14:10:50 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:09:12 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.028 |  |
| 2026-08-02 14:09:09 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-02 14:09:06 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-02 14:07:37 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.069 |  |
| 2026-08-02 14:07:19 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-08-02 14:06:03 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -8.182 |  |
| 2026-08-02 14:05:41 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -8.182 |  |
| 2026-08-02 14:05:06 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.021 |  |
| 2026-08-02 14:04:59 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:04:57 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 14:04:56 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:04:50 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.077 |  |
| 2026-08-02 14:04:20 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-08-02 14:04:20 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 14:03:58 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:03:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:03:11 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.010 |  |
| 2026-08-02 14:03:05 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 14:03:04 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-08-02 14:02:54 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-02 14:02:50 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.061 |  |
| 2026-08-02 14:02:17 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.060 |  |
| 2026-08-02 14:01:26 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:01:26 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:01:25 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.020 |  |
| 2026-08-02 14:01:14 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:00:50 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:00:49 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-08-02 14:00:37 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 13:43:08 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:30:40 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 14:09:06 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-02 14:12:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-02 13:07:21 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-02 14:09:09 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-02 14:02:54 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-02 14:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 14:00:37 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 14:03:05 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 14:04:57 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 14:01:26 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:01:26 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:00:50 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:03:58 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:02:17 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:06:04 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:04:20 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:10:50 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:04:56 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:04:59 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:03:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:01:14 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:24:42 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:43:08 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 13:30:40 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-02 14:03:11 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.010 |  |
| 2026-08-02 14:03:04 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-08-02 14:00:49 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-08-02 14:04:20 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-08-02 14:01:25 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.020 |  |
| 2026-08-02 14:07:19 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-08-02 14:05:06 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.021 |  |
| 2026-08-02 14:09:12 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.028 |  |
| 2026-08-02 13:07:27 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.028 |  |
| 2026-08-02 14:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.060 |  |
| 2026-08-02 14:02:50 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.061 |  |
| 2026-08-02 14:07:37 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.069 |  |
| 2026-08-02 14:04:50 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.077 |  |
| 2026-08-02 14:06:03 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -8.182 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)