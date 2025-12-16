# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_18:12:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,701 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 18:12:29 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:10:51 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:10:32 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 18:09:42 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:07:47 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.051 |  |
| 2025-12-16 18:07:42 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2025-12-16 18:06:17 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:06:00 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:05:34 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.037 |  |
| 2025-12-16 18:05:21 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |
| 2025-12-16 18:04:50 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:29 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:22 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 18:04:18 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.012 |  |
| 2025-12-16 18:04:01 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:03:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:03:37 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 18:03:28 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:03:26 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:02:55 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 18:02:55 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:02:53 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:02:32 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:02:31 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.063 |  |
| 2025-12-16 18:02:07 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 18:02:01 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:01:42 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:01:38 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:01:16 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:01:14 | Yaka Wewa (Ma Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:01:09 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:00:39 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:00:34 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2025-12-16 18:00:18 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.056 |  |
| 2025-12-16 18:00:14 | Horowpothana (Yan Oya) | 5.92 | 🟢 Normal | 0.093 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 18:00:14 | Horowpothana (Yan Oya) | 5.92 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-16 18:04:22 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 18:02:55 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 18:10:32 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 18:02:07 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 18:12:29 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:03:28 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:00:39 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:01:42 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:02:53 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:02:55 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:03:37 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:01:38 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:03:26 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:02:01 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:10:51 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:01 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:06:17 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:06:00 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:05:21 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:03:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:01:16 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:29 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:02:32 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:01:14 | Yaka Wewa (Ma Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:02:31 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:01:09 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:09:42 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.010 |  |
| 2025-12-16 18:04:18 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.012 |  |
| 2025-12-16 18:07:42 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2025-12-16 18:00:34 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2025-12-16 18:05:34 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.037 |  |
| 2025-12-16 18:07:47 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.051 |  |
| 2025-12-16 18:00:18 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.056 |  |
| 2025-12-16 18:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.063 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)