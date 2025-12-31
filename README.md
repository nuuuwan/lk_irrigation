# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_11:14:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,770 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 11:14:24 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:13:59 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:10:11 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:09:58 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-31 11:08:24 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:08:21 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:08:10 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.130 |  |
| 2025-12-31 11:07:49 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:07:47 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:07:28 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:06:48 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:06:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-31 11:05:54 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:05:30 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:05:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 11:05:08 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:04:45 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:04:39 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:04:23 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.076 |  |
| 2025-12-31 11:03:53 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2025-12-31 11:03:51 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:03:46 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:03:45 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2025-12-31 11:03:43 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-31 11:03:18 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:03:14 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.039 |  |
| 2025-12-31 11:03:01 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:57 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:55 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:31 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:31 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:26 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:09 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-31 11:01:45 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 11:01:12 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-31 11:01:11 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.012 |  |
| 2025-12-31 11:01:08 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-31 11:00:44 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-31 11:00:34 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | -0.105 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 11:01:08 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-31 11:02:09 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-31 11:01:45 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 11:06:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-31 11:01:12 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-31 11:05:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 11:02:26 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:55 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:03:01 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:31 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:04:39 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:05:08 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:14:24 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:04:45 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:03:18 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:08:24 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-31 10:04:13 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:10:11 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:31 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:05:30 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:03:51 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:07:49 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:06:48 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:04:23 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:08:21 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:07:47 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:05:54 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:02:57 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 11:03:53 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2025-12-31 11:03:43 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-31 11:09:58 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-31 11:01:11 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.012 |  |
| 2025-12-31 11:03:45 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2025-12-31 11:00:44 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-31 11:03:14 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.039 |  |
| 2025-12-31 11:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.076 |  |
| 2025-12-31 11:00:34 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | -0.105 |  |
| 2025-12-31 11:08:10 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)