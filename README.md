# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_19:12:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,839 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 19:12:35 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2025-12-15 19:10:32 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:09:29 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.028 |  |
| 2025-12-15 19:08:36 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2025-12-15 19:08:17 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:07:32 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2025-12-15 19:06:19 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.019 |  |
| 2025-12-15 19:06:06 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-15 19:05:56 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.028 |  |
| 2025-12-15 19:04:35 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-15 19:04:16 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:04:03 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2025-12-15 19:03:56 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:03:55 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-15 19:03:33 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:03:32 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:03:23 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 8.471 | 🔺 Rising |
| 2025-12-15 19:03:07 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:03:06 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 8.471 | 🔺 Rising |
| 2025-12-15 19:02:48 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2025-12-15 19:02:30 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:02:22 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2025-12-15 19:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 19:02:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:02:14 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:02:12 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-15 19:01:54 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.020 |  |
| 2025-12-15 19:01:41 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:01:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-15 19:01:19 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2025-12-15 19:01:15 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:00:45 | Horowpothana (Yan Oya) | 3.64 | 🟢 Normal | -0.079 |  |
| 2025-12-15 19:00:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 19:03:23 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 8.471 | 🔺 Rising |
| 2025-12-15 19:02:12 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-15 19:01:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-15 19:04:16 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:01:15 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:02:30 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:10:32 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:03:07 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:02:27 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:02:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:03:32 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:03:56 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:08:17 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:03:33 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:02:14 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:04:32 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:01:41 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:00:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-15 19:12:35 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2025-12-15 19:02:22 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2025-12-15 19:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 19:03:55 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-15 19:04:35 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:06:03 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:01:10 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-15 19:06:19 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.019 |  |
| 2025-12-15 19:06:06 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-15 19:07:32 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.019 |  |
| 2025-12-15 19:01:19 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2025-12-15 19:01:54 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.020 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 19:04:03 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2025-12-15 19:05:56 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.028 |  |
| 2025-12-15 19:09:29 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.028 |  |
| 2025-12-15 19:02:48 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2025-12-15 19:08:36 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 19:00:45 | Horowpothana (Yan Oya) | 3.64 | 🟢 Normal | -0.079 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)