# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_17:04:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,754 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 17:04:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:03:55 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.011 |  |
| 2025-12-15 17:03:51 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:03:49 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:03:46 | Horowpothana (Yan Oya) | 3.79 | 🟢 Normal | -0.052 |  |
| 2025-12-15 17:03:30 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 17:03:30 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2025-12-15 17:03:30 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.058 |  |
| 2025-12-15 17:03:23 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2025-12-15 17:02:56 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:02:48 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:02:42 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.030 |  |
| 2025-12-15 17:02:42 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:02:42 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:02:37 | Thanthirimale (Malwathu Oya) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:02:31 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 17:02:22 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2025-12-15 17:02:17 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-15 17:02:17 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | -0.052 |  |
| 2025-12-15 17:02:11 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 17:02:08 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:01:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-15 17:01:36 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:01:02 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:00:44 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:00:41 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.012 |  |
| 2025-12-15 17:00:10 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-15 16:18:46 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:12:53 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2025-12-15 16:09:35 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | -0.155 |  |
| 2025-12-15 16:09:34 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.012 |  |
| 2025-12-15 16:09:10 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:38 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:27 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:06 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:07:38 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.011 |  |
| 2025-12-15 16:07:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.076 |  |
| 2025-12-15 16:06:28 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.019 |  |
| 2025-12-15 16:06:15 | Horowpothana (Yan Oya) | 3.84 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 17:02:17 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-15 17:03:30 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 17:02:31 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 17:02:11 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 17:01:36 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:01:56 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:02:08 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:06 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:03:51 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:09:10 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:03:49 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:02:48 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:02:42 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:02:56 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-15 17:04:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:08:27 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:18:46 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:01:53 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 16:12:53 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2025-12-15 17:02:37 | Thanthirimale (Malwathu Oya) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:02:42 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:00:44 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:01:02 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:00:10 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-15 17:03:55 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.011 |  |
| 2025-12-15 17:00:41 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.012 |  |
| 2025-12-15 16:06:28 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.019 |  |
| 2025-12-15 17:03:23 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2025-12-15 17:02:42 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.030 |  |
| 2025-12-15 16:03:59 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.031 |  |
| 2025-12-15 17:01:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-15 17:03:30 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2025-12-15 17:02:22 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2025-12-15 17:02:17 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | -0.052 |  |
| 2025-12-15 17:03:46 | Horowpothana (Yan Oya) | 3.79 | 🟢 Normal | -0.052 |  |
| 2025-12-15 17:03:30 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.058 |  |
| 2025-12-15 16:07:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.076 |  |
| 2025-12-15 16:09:35 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)