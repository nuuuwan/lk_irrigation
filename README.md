# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_00:12:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 00:12:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-03 00:12:35 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-01-03 00:11:43 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -1.440 |  |
| 2026-01-03 00:11:18 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -1.440 |  |
| 2026-01-03 00:10:11 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-01-03 00:08:35 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:07:54 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:07:33 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-01-03 00:05:57 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:05:30 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:05:20 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-01-03 00:05:10 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-03 00:05:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.103 |  |
| 2026-01-03 00:05:08 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:04:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-03 00:04:14 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-03 00:03:52 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:49 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:34 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:27 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:09 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:02:57 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:02:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-03 00:02:32 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.037 |  |
| 2026-01-03 00:02:15 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:01:44 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.151 |  |
| 2026-01-03 00:01:40 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:01:37 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | -0.015 |  |
| 2026-01-03 00:01:30 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:01:23 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:01:18 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-03 00:01:14 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:53:43 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.159 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 00:12:35 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-01-03 00:04:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-03 00:12:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-03 00:02:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 22:46:44 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-03 00:01:40 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:34 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:09 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:27 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:07:54 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:52 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:08:35 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:01:30 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:01:14 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:01:23 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:05:57 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:03:49 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:36 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:02:15 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:02:57 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:05:30 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:05:08 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:15:28 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-03 00:10:11 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-01-03 00:05:20 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-01-03 00:05:10 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-03 00:04:14 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-03 00:01:18 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-03 00:07:33 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-01-03 00:01:37 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | -0.015 |  |
| 2026-01-02 23:01:37 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.024 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-03 00:02:32 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.037 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-02 22:07:05 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.058 |  |
| 2026-01-03 00:05:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.103 |  |
| 2026-01-03 00:01:44 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.151 |  |
| 2026-01-03 00:11:43 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -1.440 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)