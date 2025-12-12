# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_11:15:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,805 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 11:15:39 | Padiyathalawa (Maduru Oya) | 1.47 | 🟢 Normal | -0.008 |  |
| 2025-12-12 11:14:17 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.100 |  |
| 2025-12-12 11:12:45 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:11:36 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:11:32 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.043 |  |
| 2025-12-12 11:11:16 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:08:58 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.149 |  |
| 2025-12-12 11:08:57 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-12 11:07:25 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:07:06 | Manampitiya (Mahaweli Ganga) | 3.40 | 🟡 Alert | -0.057 |  |
| 2025-12-12 11:06:28 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:06:10 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:06:04 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-12 11:05:49 | Moragaswewa (Deduru Oya) | 1.74 | 🟢 Normal | -0.029 |  |
| 2025-12-12 11:05:26 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -0.037 |  |
| 2025-12-12 11:05:11 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2025-12-12 11:05:02 | Weraganthota (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2025-12-12 11:04:40 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-12 11:04:17 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-12 11:03:46 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.041 |  |
| 2025-12-12 11:03:41 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.039 |  |
| 2025-12-12 11:03:30 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2025-12-12 11:03:26 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:03:05 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-12 11:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 11:02:37 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.020 |  |
| 2025-12-12 11:02:29 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:02:26 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 11:02:24 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-12 11:02:11 | Horowpothana (Yan Oya) | 5.88 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-12 11:02:08 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2025-12-12 11:02:02 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:02:02 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-12 11:01:51 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:01:28 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 11:01:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-12 11:01:08 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2025-12-12 11:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:00:49 | Thanthirimale (Malwathu Oya) | 4.27 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-12 11:00:47 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.032 |  |
| 2025-12-12 10:59:48 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 11:07:06 | Manampitiya (Mahaweli Ganga) | 3.40 | 🟡 Alert | -0.057 |  |
| 2025-12-12 11:05:02 | Weraganthota (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2025-12-12 11:02:11 | Horowpothana (Yan Oya) | 5.88 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-12 11:06:04 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-12 11:01:28 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 11:00:49 | Thanthirimale (Malwathu Oya) | 4.27 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-12 11:04:40 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-12 11:02:26 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 11:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 11:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:02:02 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:12:45 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:03:26 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:07:25 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:02:29 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:11:36 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:06:28 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:06:10 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-12 11:15:39 | Padiyathalawa (Maduru Oya) | 1.47 | 🟢 Normal | -0.008 |  |
| 2025-12-12 11:08:57 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-12 11:03:05 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-12 11:04:17 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-12 11:02:24 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-12 11:02:02 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-12 10:59:48 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-12 11:05:11 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2025-12-12 11:02:37 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.020 |  |
| 2025-12-12 11:05:49 | Moragaswewa (Deduru Oya) | 1.74 | 🟢 Normal | -0.029 |  |
| 2025-12-12 11:02:08 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2025-12-12 11:00:47 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.032 |  |
| 2025-12-12 11:05:26 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -0.037 |  |
| 2025-12-12 11:03:41 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.039 |  |
| 2025-12-12 11:01:08 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2025-12-12 11:03:30 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2025-12-12 11:03:46 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.041 |  |
| 2025-12-12 11:11:32 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.043 |  |
| 2025-12-12 11:01:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-12 11:14:17 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.100 |  |
| 2025-12-12 11:08:58 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)