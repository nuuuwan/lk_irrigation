# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_15:24:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 15:24:41 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.008 |  |
| 2025-12-08 15:21:02 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.022 |  |
| 2025-12-08 15:14:52 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | -0.035 |  |
| 2025-12-08 15:10:28 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.036 |  |
| 2025-12-08 15:09:48 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.065 |  |
| 2025-12-08 15:09:16 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.062 |  |
| 2025-12-08 15:07:55 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:07:43 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.037 |  |
| 2025-12-08 15:06:03 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.029 |  |
| 2025-12-08 15:05:48 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.059 |  |
| 2025-12-08 15:05:36 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-08 15:05:26 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:05:13 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.029 |  |
| 2025-12-08 15:05:13 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.034 |  |
| 2025-12-08 15:04:25 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-08 15:04:15 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2025-12-08 15:03:56 | Galgamuwa (Mee Oya) | 1.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 15:03:45 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:03:41 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.050 |  |
| 2025-12-08 15:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.41 | 🟢 Normal | -0.039 |  |
| 2025-12-08 15:03:24 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-08 15:02:30 | Weraganthota (Mahaweli Ganga) | -0.72 | 🟢 Normal | -0.159 |  |
| 2025-12-08 15:02:28 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-08 15:02:16 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:48 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-08 15:01:45 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-08 15:01:37 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:30 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.022 |  |
| 2025-12-08 15:01:24 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-08 15:01:23 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:20 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:17 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:16 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 15:01:00 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:00:25 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:00:15 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 15:01:24 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-08 15:02:28 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-08 15:03:56 | Galgamuwa (Mee Oya) | 1.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 15:01:48 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-08 15:01:16 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 15:01:00 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:00:25 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:17 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:23 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:07:55 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:03:45 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-08 14:00:29 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:37 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:02:16 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:05:26 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:20 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:24:41 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.008 |  |
| 2025-12-08 15:04:25 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-08 15:01:45 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-08 15:03:24 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-08 14:13:03 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.014 |  |
| 2025-12-08 15:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2025-12-08 15:05:36 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-08 15:01:30 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.022 |  |
| 2025-12-08 15:21:02 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.022 |  |
| 2025-12-08 15:06:03 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.029 |  |
| 2025-12-08 15:05:13 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.029 |  |
| 2025-12-08 15:05:13 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.034 |  |
| 2025-12-08 15:14:52 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | -0.035 |  |
| 2025-12-08 15:10:28 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.036 |  |
| 2025-12-08 15:07:43 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.037 |  |
| 2025-12-08 15:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.41 | 🟢 Normal | -0.039 |  |
| 2025-12-08 15:03:41 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.050 |  |
| 2025-12-08 15:04:15 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2025-12-08 15:05:48 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.059 |  |
| 2025-12-08 15:09:16 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.062 |  |
| 2025-12-08 15:09:48 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.065 |  |
| 2025-12-08 15:02:30 | Weraganthota (Mahaweli Ganga) | -0.72 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)