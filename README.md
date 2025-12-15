# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_21:16:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,911 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 21:16:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-15 21:08:58 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-15 21:08:04 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.020 |  |
| 2025-12-15 21:07:50 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.031 |  |
| 2025-12-15 21:07:50 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-15 21:07:11 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:07:02 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:07:02 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-15 21:06:30 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-15 21:06:17 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.025 |  |
| 2025-12-15 21:05:59 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-15 21:05:31 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:05:12 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 21:04:16 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-15 21:04:14 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-15 21:04:03 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:04:01 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:03:50 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:03:48 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 21:03:04 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:56 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.058 |  |
| 2025-12-15 21:02:53 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.022 |  |
| 2025-12-15 21:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:49 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:48 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:00 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:01:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:01:34 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.020 |  |
| 2025-12-15 21:01:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-15 21:01:24 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:01:19 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:01:18 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:00:57 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.041 |  |
| 2025-12-15 21:00:20 | Horowpothana (Yan Oya) | 3.51 | 🟢 Normal | -0.085 |  |
| 2025-12-15 21:00:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 21:01:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-15 21:16:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-15 21:06:30 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-15 21:07:50 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-15 21:08:58 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-15 21:07:02 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-15 21:03:48 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 21:05:12 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 21:04:03 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:01:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:01:19 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:01:18 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:00 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 20:18:10 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:49 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:04:01 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:00:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:03:50 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:05:31 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:07:11 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:03:04 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:48 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:01:24 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:07:02 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:04:16 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-15 21:05:59 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-15 21:08:04 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.020 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 21:04:14 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-15 21:01:34 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.020 |  |
| 2025-12-15 21:02:53 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.022 |  |
| 2025-12-15 21:06:17 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.025 |  |
| 2025-12-15 21:07:50 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.031 |  |
| 2025-12-15 21:00:57 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.041 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 21:02:56 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.058 |  |
| 2025-12-15 21:00:20 | Horowpothana (Yan Oya) | 3.51 | 🟢 Normal | -0.085 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)