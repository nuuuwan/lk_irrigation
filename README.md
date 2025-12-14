# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_04:20:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,242 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 04:20:00 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:16:57 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-15 04:11:43 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-15 04:11:43 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2025-12-15 04:10:42 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-15 04:10:38 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-15 04:08:31 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.058 |  |
| 2025-12-15 04:07:32 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-15 04:06:56 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:06:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.036 |  |
| 2025-12-15 04:05:59 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.035 |  |
| 2025-12-15 04:05:49 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.048 |  |
| 2025-12-15 04:05:05 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:04:09 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.177 |  |
| 2025-12-15 04:04:00 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-15 04:03:47 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-15 04:02:42 | Horowpothana (Yan Oya) | 4.16 | 🟢 Normal | -0.020 |  |
| 2025-12-15 04:02:38 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2025-12-15 04:02:37 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-15 04:02:26 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:02:00 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.019 |  |
| 2025-12-15 04:01:41 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2025-12-15 04:01:34 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.021 |  |
| 2025-12-15 04:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:01:01 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 1.209 | 🔺 Rising |
| 2025-12-15 04:00:49 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.055 |  |
| 2025-12-15 04:00:16 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:47:12 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.177 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 04:01:01 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 1.209 | 🔺 Rising |
| 2025-12-15 04:16:57 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-15 04:10:38 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-15 04:07:32 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-15 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-15 01:03:44 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-15 04:10:42 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-15 04:03:47 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-15 03:01:28 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:11 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:02:26 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:03:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:20:00 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:08:10 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:05:05 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:06:56 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:00:16 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 03:16:16 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.005 |  |
| 2025-12-15 04:11:43 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-15 04:11:43 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2025-12-15 04:02:37 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-15 04:04:00 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-15 02:01:24 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-15 04:02:00 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.019 |  |
| 2025-12-15 04:02:38 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2025-12-15 04:02:42 | Horowpothana (Yan Oya) | 4.16 | 🟢 Normal | -0.020 |  |
| 2025-12-15 04:01:34 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.021 |  |
| 2025-12-15 04:05:59 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.035 |  |
| 2025-12-15 04:06:02 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.036 |  |
| 2025-12-15 04:01:41 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2025-12-15 04:05:49 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.048 |  |
| 2025-12-15 04:00:49 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.055 |  |
| 2025-12-15 04:08:31 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.058 |  |
| 2025-12-15 03:16:52 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.124 |  |
| 2025-12-15 04:04:09 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)