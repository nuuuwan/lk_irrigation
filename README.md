# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_06:37:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,608 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 06:37:40 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 06:27:05 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:22:20 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 06:14:06 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.059 |  |
| 2025-12-12 06:12:24 | Horowpothana (Yan Oya) | 4.86 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2025-12-12 06:11:43 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-12 06:11:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | 6.822 | 🔺 Rising |
| 2025-12-12 06:10:16 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.002 |  |
| 2025-12-12 06:09:26 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 06:08:30 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2025-12-12 06:08:20 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 06:07:58 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2025-12-12 06:07:56 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.043 |  |
| 2025-12-12 06:07:27 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | -0.045 |  |
| 2025-12-12 06:06:50 | Yaka Wewa (Ma Oya) | 1.26 | 🟢 Normal | -0.028 |  |
| 2025-12-12 06:06:39 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2025-12-12 06:06:26 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -36.000 |  |
| 2025-12-12 06:06:23 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -36.000 |  |
| 2025-12-12 06:05:41 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:05:33 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.050 |  |
| 2025-12-12 06:05:11 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-12 06:04:48 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -15.126 |  |
| 2025-12-12 06:04:45 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.050 |  |
| 2025-12-12 06:04:12 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.133 |  |
| 2025-12-12 06:02:59 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 06:02:57 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.046 |  |
| 2025-12-12 06:02:49 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -15.126 |  |
| 2025-12-12 06:02:48 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-12 06:02:37 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2025-12-12 06:01:58 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-12 06:01:49 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.031 |  |
| 2025-12-12 06:01:48 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:01:30 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-12 06:01:26 | Moragaswewa (Deduru Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2025-12-12 06:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:01:20 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-12 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:01:08 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.122 |  |
| 2025-12-12 05:44:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 6.822 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 06:11:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | 6.822 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-12 06:12:24 | Horowpothana (Yan Oya) | 4.86 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2025-12-12 06:06:39 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2025-12-12 06:02:48 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-12 06:02:59 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 06:01:30 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-12 06:05:11 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-12 06:22:20 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 06:09:26 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 06:08:20 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 06:37:40 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 06:11:43 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 06:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:01:48 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:27:05 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:05:41 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-12 06:10:16 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.002 |  |
| 2025-12-12 06:07:58 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2025-12-12 06:01:58 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-12 06:01:20 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-12 06:01:26 | Moragaswewa (Deduru Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2025-12-12 06:02:37 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2025-12-12 06:08:30 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2025-12-12 06:06:50 | Yaka Wewa (Ma Oya) | 1.26 | 🟢 Normal | -0.028 |  |
| 2025-12-12 06:01:49 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.031 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-12 06:07:56 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.043 |  |
| 2025-12-12 06:07:27 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | -0.045 |  |
| 2025-12-12 06:02:57 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.046 |  |
| 2025-12-12 06:04:45 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.050 |  |
| 2025-12-12 06:05:33 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.050 |  |
| 2025-12-12 06:14:06 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.059 |  |
| 2025-12-12 06:01:08 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.122 |  |
| 2025-12-12 06:04:12 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.133 |  |
| 2025-12-12 06:04:48 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -15.126 |  |
| 2025-12-12 06:06:26 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)