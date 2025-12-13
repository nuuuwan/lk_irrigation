# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_09:16:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,627 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 09:16:51 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:14:24 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.017 |  |
| 2025-12-13 09:07:36 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:07:25 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2025-12-13 09:07:21 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:06:17 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:06:06 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2025-12-13 09:06:05 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:05:48 | Weraganthota (Mahaweli Ganga) | -0.42 | 🟢 Normal | -0.107 |  |
| 2025-12-13 09:05:37 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2025-12-13 09:05:33 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-13 09:04:58 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.989 | 🔺 Rising |
| 2025-12-13 09:04:54 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.051 |  |
| 2025-12-13 09:04:35 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:04:17 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:03:52 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 09:03:47 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-13 09:03:34 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2025-12-13 09:03:26 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.012 |  |
| 2025-12-13 09:03:13 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:03:07 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:03:05 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:02:59 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:02:50 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:02:46 | Horowpothana (Yan Oya) | 5.99 | 🟢 Normal | -0.058 |  |
| 2025-12-13 09:02:40 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:02:34 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | -0.039 |  |
| 2025-12-13 09:02:30 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2025-12-13 09:02:22 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-13 09:02:18 | Thanthirimale (Malwathu Oya) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:02:17 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.59 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:01:53 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:01:52 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:01:29 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.093 |  |
| 2025-12-13 09:01:16 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:01:09 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:00:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:00:25 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:00:11 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 09:04:58 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.989 | 🔺 Rising |
| 2025-12-13 09:02:22 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-13 09:05:33 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-13 09:03:52 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 09:02:40 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:06:05 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:03:07 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:16:51 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:01:16 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:03:13 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:04:17 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:03:05 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:06:17 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:01:52 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:02:50 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:07:36 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:02:17 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:07:21 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:02:59 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 09:04:35 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:01:09 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:00:25 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:02:18 | Thanthirimale (Malwathu Oya) | 4.22 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.59 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:00:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:00:11 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-13 09:03:26 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.012 |  |
| 2025-12-13 09:14:24 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.017 |  |
| 2025-12-13 09:07:25 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2025-12-13 09:03:47 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-13 09:05:37 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2025-12-13 09:02:30 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2025-12-13 09:03:34 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2025-12-13 09:02:34 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | -0.039 |  |
| 2025-12-13 09:04:54 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.051 |  |
| 2025-12-13 09:02:46 | Horowpothana (Yan Oya) | 5.99 | 🟢 Normal | -0.058 |  |
| 2025-12-13 09:06:06 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2025-12-13 09:01:29 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.093 |  |
| 2025-12-13 09:05:48 | Weraganthota (Mahaweli Ganga) | -0.42 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)