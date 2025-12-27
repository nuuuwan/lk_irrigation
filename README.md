# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_06:09:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,021 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 06:09:29 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-27 06:09:24 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 06:08:53 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:08:26 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.018 |  |
| 2025-12-27 06:07:58 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.009 |  |
| 2025-12-27 06:07:12 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.004 |  |
| 2025-12-27 06:05:59 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-27 06:05:43 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:04:16 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:04:14 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:04:12 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.020 |  |
| 2025-12-27 06:04:04 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:03:36 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:03:21 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 06:03:07 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:02:54 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 06:02:44 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.356 |  |
| 2025-12-27 06:02:42 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-27 06:02:10 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 06:02:03 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:01:44 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:01:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2025-12-27 06:01:22 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:01:17 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:01:14 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 06:01:08 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:00:58 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:00:43 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.043 |  |
| 2025-12-27 06:00:42 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-27 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.012 |  |
| 2025-12-27 05:59:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.065 |  |
| 2025-12-27 05:23:22 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -36.000 |  |
| 2025-12-27 05:23:21 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2025-12-27 05:23:19 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2025-12-27 05:23:18 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2025-12-27 05:23:16 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2025-12-27 05:15:31 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:14:02 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 06:00:42 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-27 06:09:29 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-27 06:09:24 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 06:02:54 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 06:01:14 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 06:03:21 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 06:02:10 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 06:07:12 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.004 |  |
| 2025-12-27 06:04:14 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:08:53 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:03:36 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:04:16 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:04:04 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:01:17 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:01:22 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:03:07 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:02:03 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:01:44 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-27 05:03:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:01:08 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:15:39 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:00:58 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 06:05:43 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 02:19:02 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2025-12-27 06:07:58 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.009 |  |
| 2025-12-27 06:05:59 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-27 06:02:42 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-26 18:01:40 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-27 04:01:10 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2025-12-27 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.012 |  |
| 2025-12-27 06:08:26 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.018 |  |
| 2025-12-27 05:06:43 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.019 |  |
| 2025-12-27 06:04:12 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.020 |  |
| 2025-12-27 06:01:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2025-12-27 06:00:43 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.043 |  |
| 2025-12-27 05:59:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.065 |  |
| 2025-12-27 06:02:44 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.356 |  |
| 2025-12-27 05:23:22 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)