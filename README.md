# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_16:16:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 16:16:48 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:15:34 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:14:58 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:13:21 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:11:45 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-24 16:09:50 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:09:05 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.058 |  |
| 2025-12-24 16:07:32 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 16:07:02 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 16:06:19 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-24 16:06:12 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:06:09 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | -0.072 |  |
| 2025-12-24 16:06:02 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:05:14 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:05:12 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-24 16:05:12 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-24 16:04:36 | Thanthirimale (Malwathu Oya) | 2.21 | 🟢 Normal | -0.039 |  |
| 2025-12-24 16:04:18 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:04:14 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.248 |  |
| 2025-12-24 16:03:53 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2025-12-24 16:03:53 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:43 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:15 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-24 16:03:06 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-24 16:03:05 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2025-12-24 16:02:57 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:44 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:43 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:11 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2025-12-24 16:02:08 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:07 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:01:34 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:01:32 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:00:53 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:00:03 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 16:03:53 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2025-12-24 16:05:12 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-24 16:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-24 16:06:19 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-24 16:03:06 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-24 16:05:12 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-24 16:07:32 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 16:07:02 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 16:11:45 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-24 16:02:43 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:43 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:01:34 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:15 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:00:53 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:09:50 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:16:48 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:57 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:04:18 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:05:14 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:00:03 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:53 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:01:32 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:08 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 14:03:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:44 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:06:02 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:07 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-24 15:02:26 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:06:12 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:14:58 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:15:34 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:02:11 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2025-12-24 16:03:05 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2025-12-24 16:04:36 | Thanthirimale (Malwathu Oya) | 2.21 | 🟢 Normal | -0.039 |  |
| 2025-12-24 15:05:33 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2025-12-24 16:09:05 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.058 |  |
| 2025-12-24 16:06:09 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | -0.072 |  |
| 2025-12-24 16:04:14 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.248 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)