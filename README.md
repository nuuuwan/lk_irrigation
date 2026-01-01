# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_12:13:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,688 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 12:13:13 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:10:51 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-01 12:08:41 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.013 |  |
| 2026-01-01 12:08:41 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:08:26 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-01 12:08:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-01-01 12:05:43 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-01 12:05:34 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.020 |  |
| 2026-01-01 12:05:32 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:05:13 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-01-01 12:05:11 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 12:05:08 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-01-01 12:04:56 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:04:52 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-01 12:04:36 | Horowpothana (Yan Oya) | 3.13 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-01-01 12:04:02 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.122 |  |
| 2026-01-01 12:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-01 12:03:24 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:03:10 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:03:10 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-01 12:03:06 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.040 |  |
| 2026-01-01 12:02:58 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.039 |  |
| 2026-01-01 12:02:49 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-01-01 12:02:44 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 12:02:40 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:02:24 | Siyambalanduwa (Heda Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-01-01 12:02:06 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:01:42 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 12:01:37 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 12:01:35 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:01:24 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.022 |  |
| 2026-01-01 12:01:22 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-01 12:01:14 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.071 |  |
| 2026-01-01 12:01:12 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:00:18 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:00:12 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-01 11:50:29 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:36:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:21:29 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-01-01 11:20:49 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 12:04:36 | Horowpothana (Yan Oya) | 3.13 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-01-01 12:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-01 12:01:42 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 12:02:44 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-01 12:05:43 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-01 12:10:51 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-01 11:07:08 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 12:05:11 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 12:01:37 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 12:01:12 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:01:35 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:05:32 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:04:56 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:02:40 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:03:10 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:02:06 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:00:18 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:03:24 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:08:41 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:13:13 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-01 11:36:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 12:08:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-01-01 12:08:26 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-01 12:04:52 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-01 12:05:13 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-01-01 12:00:12 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-01 12:03:10 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-01 12:08:41 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.013 |  |
| 2026-01-01 12:05:08 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-01-01 12:05:34 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.020 |  |
| 2026-01-01 12:02:49 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-01-01 12:01:24 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.022 |  |
| 2026-01-01 12:02:24 | Siyambalanduwa (Heda Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-01-01 12:01:22 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-01 12:02:58 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.039 |  |
| 2026-01-01 12:03:06 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.040 |  |
| 2026-01-01 12:01:14 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.071 |  |
| 2026-01-01 12:04:02 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)