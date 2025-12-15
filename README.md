# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_16:09:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,724 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 16:09:35 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | -0.155 |  |
| 2025-12-15 16:09:34 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:09:10 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:38 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:27 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:06 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:07:38 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:07:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.076 |  |
| 2025-12-15 16:06:28 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.019 |  |
| 2025-12-15 16:06:15 | Horowpothana (Yan Oya) | 3.84 | 🟢 Normal | -0.062 |  |
| 2025-12-15 16:05:57 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:04:49 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 16:04:15 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2025-12-15 16:04:09 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.050 |  |
| 2025-12-15 16:03:59 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.031 |  |
| 2025-12-15 16:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-15 16:03:32 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:03:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.041 |  |
| 2025-12-15 16:03:24 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2025-12-15 16:03:18 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:03:15 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:03:06 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2025-12-15 16:02:52 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:02:42 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:02:41 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:02:34 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:02:32 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:02:27 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 16:02:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2025-12-15 16:02:19 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.012 |  |
| 2025-12-15 16:02:10 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:01:58 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:01:56 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:01:53 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:01:24 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-15 16:01:10 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:00:48 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:14:18 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 16:03:06 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2025-12-15 16:01:24 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-15 16:02:27 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 16:04:49 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 16:02:34 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:01:56 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:03:18 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:09:34 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:07:38 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:06 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:03:15 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:09:10 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:05:57 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:00:48 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:01:10 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:38 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:02:52 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:02:32 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:27 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:02:42 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:01:53 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-15 16:01:58 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:02:10 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:03:32 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:07:39 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:02:41 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:02:19 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.012 |  |
| 2025-12-15 16:06:28 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.019 |  |
| 2025-12-15 16:03:24 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2025-12-15 15:03:06 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.027 |  |
| 2025-12-15 16:04:15 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2025-12-15 16:02:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2025-12-15 16:03:59 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.031 |  |
| 2025-12-15 16:03:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.041 |  |
| 2025-12-15 16:04:09 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.050 |  |
| 2025-12-15 16:06:15 | Horowpothana (Yan Oya) | 3.84 | 🟢 Normal | -0.062 |  |
| 2025-12-15 16:07:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.076 |  |
| 2025-12-15 16:09:35 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)