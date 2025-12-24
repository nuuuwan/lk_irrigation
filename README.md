# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_10:14:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,501 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 10:14:00 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2025-12-24 10:12:11 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.066 |  |
| 2025-12-24 10:08:45 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:08:23 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-24 10:08:15 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-24 10:08:07 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:07:44 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.068 |  |
| 2025-12-24 10:07:11 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:06:50 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:06:23 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:06:05 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2025-12-24 10:05:54 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:05:46 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.105 |  |
| 2025-12-24 10:05:43 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.049 |  |
| 2025-12-24 10:05:36 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:05:09 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:05:01 | Dunamale (Aththanagalu Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:04:41 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-24 10:03:48 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2025-12-24 10:03:44 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:03:40 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2025-12-24 10:03:32 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:03:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:55 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:37 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:34 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 10:02:14 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.021 |  |
| 2025-12-24 10:02:10 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:02:05 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:03 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:01:53 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:01:49 | Nagalagam Street (Kelani Ganga) | 0.26 | 🟢 Normal | -0.050 |  |
| 2025-12-24 10:01:46 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:01:23 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:01:13 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:01:07 | Thanthirimale (Malwathu Oya) | 2.44 | 🟢 Normal | -0.041 |  |
| 2025-12-24 10:00:45 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:00:17 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 10:03:48 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2025-12-24 10:08:23 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-24 10:04:41 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-24 10:08:15 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-24 10:02:34 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 10:07:44 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:01:13 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:01:53 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:08:07 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:03:44 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:08:45 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:01:46 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:03:32 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:55 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:05:36 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:01:23 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:00:17 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:03:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:37 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:06:23 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:02:05 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:05:09 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:06:50 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:02:03 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:00:45 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:02:10 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-24 10:05:01 | Dunamale (Aththanagalu Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-24 09:07:53 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.019 |  |
| 2025-12-24 10:06:05 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2025-12-24 10:14:00 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2025-12-24 10:02:14 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.021 |  |
| 2025-12-24 10:03:40 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2025-12-24 10:01:07 | Thanthirimale (Malwathu Oya) | 2.44 | 🟢 Normal | -0.041 |  |
| 2025-12-24 10:05:43 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.049 |  |
| 2025-12-24 10:01:49 | Nagalagam Street (Kelani Ganga) | 0.26 | 🟢 Normal | -0.050 |  |
| 2025-12-24 10:12:11 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.066 |  |
| 2025-12-24 10:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.068 |  |
| 2025-12-24 10:05:46 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)