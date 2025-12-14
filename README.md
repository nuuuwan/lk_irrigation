# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_21:10:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,006 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 21:10:54 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2025-12-14 21:09:16 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 21:09:05 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-14 21:08:15 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 21:07:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-14 21:06:57 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2025-12-14 21:06:26 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:06:13 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:06:06 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:06:00 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:05:54 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2025-12-14 21:05:25 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:05:17 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.038 |  |
| 2025-12-14 21:05:07 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 21:04:47 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.026 |  |
| 2025-12-14 21:04:32 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-14 21:04:25 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 21:04:23 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-14 21:04:05 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:03:32 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-14 21:03:30 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | -0.072 |  |
| 2025-12-14 21:03:24 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2025-12-14 21:03:09 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:02:49 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.030 |  |
| 2025-12-14 21:02:12 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:02:09 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:01:54 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 21:01:20 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:00:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.107 |  |
| 2025-12-14 21:00:42 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:00:28 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.013 |  |
| 2025-12-14 21:00:14 | Horowpothana (Yan Oya) | 4.24 | 🟢 Normal | -0.010 |  |
| 2025-12-14 20:34:51 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-14 20:31:47 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 21:04:32 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-14 21:03:32 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-14 20:34:51 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-14 21:09:16 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 21:04:23 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-14 21:07:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-14 21:09:05 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-14 21:01:54 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 21:08:15 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 21:04:25 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 21:05:07 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 21:02:09 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:00:42 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-14 20:31:47 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:01:20 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:03:09 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:06:00 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:06:13 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:06:06 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:04:05 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:06:26 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:02:12 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:05:25 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:10:54 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2025-12-14 21:06:57 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-14 21:00:14 | Horowpothana (Yan Oya) | 4.24 | 🟢 Normal | -0.010 |  |
| 2025-12-14 21:00:28 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.013 |  |
| 2025-12-14 21:05:54 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2025-12-14 20:03:23 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.024 |  |
| 2025-12-14 21:04:47 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.026 |  |
| 2025-12-14 20:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.029 |  |
| 2025-12-14 21:02:49 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.030 |  |
| 2025-12-14 21:03:24 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2025-12-14 21:05:17 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.038 |  |
| 2025-12-14 21:03:30 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | -0.072 |  |
| 2025-12-14 21:00:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)