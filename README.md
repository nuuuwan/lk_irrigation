# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_10:07:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,578 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 10:07:50 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:07:34 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.018 |  |
| 2025-12-14 10:06:57 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.028 |  |
| 2025-12-14 10:06:02 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.057 |  |
| 2025-12-14 10:05:38 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 10:05:34 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2025-12-14 10:05:14 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 10:04:55 | Galgamuwa (Mee Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-14 10:04:53 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2025-12-14 10:04:33 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.041 |  |
| 2025-12-14 10:04:30 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.031 |  |
| 2025-12-14 10:04:22 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:04:18 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:04:17 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.050 |  |
| 2025-12-14 10:04:05 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.011 |  |
| 2025-12-14 10:04:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:03:37 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:03:24 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:03:14 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-14 10:03:06 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2025-12-14 10:03:06 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2025-12-14 10:02:38 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 10:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | -0.020 |  |
| 2025-12-14 10:02:25 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.057 |  |
| 2025-12-14 10:02:23 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:02:16 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-14 10:02:14 | Manampitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.036 |  |
| 2025-12-14 10:02:03 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2025-12-14 10:01:29 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:01:22 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:00:46 | Thanthirimale (Malwathu Oya) | 4.34 | 🟢 Normal | -0.020 |  |
| 2025-12-14 10:00:32 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 10:00:30 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-14 10:00:15 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:00:10 | Horowpothana (Yan Oya) | 4.57 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 10:05:14 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-14 10:02:38 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 09:10:35 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-14 10:00:32 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 10:05:38 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 09:05:55 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:01:22 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:03:37 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:04:22 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:04:02 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:07:50 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:01:29 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:00:15 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:02:23 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:04:18 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:03:24 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:04:53 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2025-12-14 10:00:30 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-14 10:03:14 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-14 10:04:55 | Galgamuwa (Mee Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-14 10:02:16 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-14 10:04:05 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.011 |  |
| 2025-12-14 10:07:34 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.018 |  |
| 2025-12-14 10:05:34 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2025-12-14 10:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | -0.020 |  |
| 2025-12-14 10:03:06 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2025-12-14 10:00:46 | Thanthirimale (Malwathu Oya) | 4.34 | 🟢 Normal | -0.020 |  |
| 2025-12-14 10:06:57 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.028 |  |
| 2025-12-14 10:04:30 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.031 |  |
| 2025-12-14 10:02:14 | Manampitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.036 |  |
| 2025-12-14 09:03:23 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.039 |  |
| 2025-12-14 10:03:06 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2025-12-14 10:02:03 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2025-12-14 10:04:33 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.041 |  |
| 2025-12-14 10:04:17 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.050 |  |
| 2025-12-14 10:00:10 | Horowpothana (Yan Oya) | 4.57 | 🟢 Normal | -0.050 |  |
| 2025-12-14 10:02:25 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.057 |  |
| 2025-12-14 10:06:02 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)