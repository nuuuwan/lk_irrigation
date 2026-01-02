# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_23:24:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,004 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 23:24:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-02 23:21:06 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-01-02 23:15:28 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:13:49 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | -0.026 |  |
| 2026-01-02 23:13:14 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:12:35 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-02 23:12:15 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:08:23 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:06:22 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-01-02 23:06:07 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:04:21 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.039 |  |
| 2026-01-02 23:04:20 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:04:06 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-01-02 23:03:58 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:03:28 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:58 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-01-02 23:02:39 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:37 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:27 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-01-02 23:02:17 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-02 23:02:14 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:12 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:04 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:01:37 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.024 |  |
| 2026-01-02 23:01:28 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:01:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-02 23:01:21 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.011 |  |
| 2026-01-02 23:01:04 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:00:59 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-01-02 22:46:44 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 23:02:17 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-02 23:01:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-02 22:07:31 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-02 23:24:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-02 22:46:44 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 23:12:35 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-02 22:02:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 23:13:14 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:01:04 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:12 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:03:28 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:08:23 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:12:15 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:14 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:37 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 22:07:36 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:03:58 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:15:28 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:02:39 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 23:21:06 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-01-02 22:06:37 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:06:07 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:04:20 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:02:04 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:01:28 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-02 23:01:21 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.011 |  |
| 2026-01-02 23:02:58 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-01-02 23:06:22 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-01-02 23:02:27 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-01-02 23:01:37 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.024 |  |
| 2026-01-02 23:13:49 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | -0.026 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-02 23:00:59 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-01-02 23:04:06 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-01-02 23:04:21 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.039 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-02 22:07:05 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)