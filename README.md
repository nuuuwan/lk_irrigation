# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_15:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,710 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 15:14:58 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:12:23 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 15:10:03 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:06:24 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:50 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:36 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:27 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-01-02 15:04:11 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:11 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-01-02 15:04:06 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:03:55 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:03:23 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 15:03:21 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-01-02 15:02:57 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:02:50 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:02:50 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:02:44 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-02 15:02:44 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-01-02 15:02:35 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-01-02 15:02:27 | Katharagama (Menik Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-01-02 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-02 15:02:16 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:01:51 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:01:51 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:01:42 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:01:39 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | -0.062 |  |
| 2026-01-02 15:01:33 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:01:31 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:01:28 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:01:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-02 15:01:13 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.237 |  |
| 2026-01-02 15:01:09 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:00:46 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:00:42 | Horowpothana (Yan Oya) | 2.93 | 🟢 Normal | -0.062 |  |
| 2026-01-02 15:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:00:08 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-01-02 14:42:20 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:42:17 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:42:15 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:42:12 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:42:08 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:42:06 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 15:02:44 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-02 15:01:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-02 15:03:23 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 15:12:23 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 15:01:33 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:01:09 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:06:24 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:14:58 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:02:16 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:02:50 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:10:03 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:01:51 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:02:50 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:06 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:36 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:50 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:04:11 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:08:09 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 15:03:55 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:01:51 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:01:31 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:02:57 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:00:46 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:01:42 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:01:28 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-02 15:04:11 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-01-02 15:03:21 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-01-02 15:02:44 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-01-02 15:02:27 | Katharagama (Menik Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-01-02 15:00:08 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-01-02 15:02:35 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-01-02 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-02 15:04:27 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-01-02 15:00:42 | Horowpothana (Yan Oya) | 2.93 | 🟢 Normal | -0.062 |  |
| 2026-01-02 15:01:39 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | -0.062 |  |
| 2026-01-02 15:01:13 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.237 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)