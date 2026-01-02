# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_21:31:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,935 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 21:31:42 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:11:36 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-02 21:08:13 | Padiyathalawa (Maduru Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:08:03 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.038 |  |
| 2026-01-02 21:06:50 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.028 |  |
| 2026-01-02 21:06:03 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:05:44 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-02 21:05:34 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:05:22 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-01-02 21:04:57 | Horowpothana (Yan Oya) | 2.72 | 🟢 Normal | -0.028 |  |
| 2026-01-02 21:04:57 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:04:44 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.054 |  |
| 2026-01-02 21:04:41 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:04:40 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:04:20 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 21:04:13 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 21:04:12 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.039 |  |
| 2026-01-02 21:03:44 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:03:37 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:03:37 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:03:31 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-01-02 21:03:01 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:02:15 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:02:14 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 21:02:08 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-01-02 21:01:59 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:01:48 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:01:39 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:01:37 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:01:21 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-02 21:01:20 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-02 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:01:18 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:00:58 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:00:57 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.236 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 21:00:57 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-01-02 21:01:20 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-02 21:05:44 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-02 21:01:21 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-02 21:11:36 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-02 21:04:20 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 21:02:14 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 21:04:13 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 21:04:41 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:01:37 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:03:37 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:31:42 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:03:01 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:01:48 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:01:59 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:05:34 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:00:58 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:06:50 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-02 21:05:22 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-01-02 21:04:40 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:08:13 | Padiyathalawa (Maduru Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:04:57 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:03:37 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:01:39 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:03:44 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:02:15 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:01:18 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:06:03 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-02 21:03:31 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-01-02 21:02:08 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-01-02 21:04:57 | Horowpothana (Yan Oya) | 2.72 | 🟢 Normal | -0.028 |  |
| 2026-01-02 21:06:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.028 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-02 21:08:03 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.038 |  |
| 2026-01-02 21:04:12 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.039 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-02 21:04:44 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)