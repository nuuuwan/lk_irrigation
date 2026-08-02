# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_15:18:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,998 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 15:18:16 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-02 15:10:25 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-02 15:09:44 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-02 15:09:28 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:09:05 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:08:16 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.006 |  |
| 2026-08-02 15:08:16 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-08-02 15:07:08 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-08-02 15:06:57 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-08-02 15:06:28 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-08-02 15:06:27 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-08-02 15:05:50 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-02 15:05:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-02 15:04:51 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | -0.050 |  |
| 2026-08-02 15:04:48 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-08-02 15:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-02 15:04:02 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:04:00 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 15:03:43 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:03:42 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-08-02 15:03:27 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-08-02 15:03:08 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-08-02 15:03:06 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:03:01 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.050 |  |
| 2026-08-02 15:03:00 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-02 15:02:54 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-08-02 15:02:41 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.010 |  |
| 2026-08-02 15:02:37 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:02:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:02:24 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.039 |  |
| 2026-08-02 15:02:20 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:02:13 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:02:06 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-08-02 15:02:02 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:01:52 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-02 15:01:22 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-02 15:01:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:00:57 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:00:42 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-02 15:00:37 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 15:05:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-02 15:18:16 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-02 15:09:44 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-02 15:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-02 15:03:00 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-02 15:01:22 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-02 15:04:00 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 15:05:50 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-02 15:01:52 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-02 15:02:20 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:09:28 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:01:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:00:57 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:03:43 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:04:02 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:02:37 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:02:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:00:37 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:02:02 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:09:05 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:03:42 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:03:06 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-02 15:08:16 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.006 |  |
| 2026-08-02 15:08:16 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-08-02 15:03:27 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-08-02 15:02:41 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.010 |  |
| 2026-08-02 15:00:42 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-02 15:07:08 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-08-02 15:04:48 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-08-02 15:06:28 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-08-02 15:06:27 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-08-02 15:02:54 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-08-02 15:03:08 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-08-02 15:02:06 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-08-02 15:06:57 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-08-02 15:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-08-02 15:02:24 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.039 |  |
| 2026-08-02 15:04:51 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | -0.050 |  |
| 2026-08-02 15:03:01 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)