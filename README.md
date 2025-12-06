# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_10:17:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,671 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 10:17:32 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:11:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.026 |  |
| 2025-12-06 10:11:13 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.071 |  |
| 2025-12-06 10:11:07 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | -0.009 |  |
| 2025-12-06 10:08:06 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.246 |  |
| 2025-12-06 10:06:17 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 10:05:55 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2025-12-06 10:05:51 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 10:05:11 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.069 |  |
| 2025-12-06 10:04:37 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:04:27 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:04:24 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-06 10:04:16 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-06 10:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2025-12-06 10:03:55 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:03:43 | Weraganthota (Mahaweli Ganga) | -0.73 | 🟢 Normal | -0.394 |  |
| 2025-12-06 10:03:36 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:03:35 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-06 10:03:27 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.023 |  |
| 2025-12-06 10:03:23 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:03:10 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.040 |  |
| 2025-12-06 10:02:46 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:02:41 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-06 10:02:33 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:02:30 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:02:25 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-06 10:02:24 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:46 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:39 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 10:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:31 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:20 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:16 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-06 10:01:14 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.053 |  |
| 2025-12-06 10:00:51 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:00:46 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.031 |  |
| 2025-12-06 09:59:41 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 09:08:32 | Thanthirimale (Malwathu Oya) | 6.95 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-06 10:04:16 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-06 10:02:25 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-06 10:03:35 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-06 10:01:39 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 10:06:17 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 10:05:51 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 10:02:33 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:02:30 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:02:46 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:20 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:59:41 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:04:37 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:03:36 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:46 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:03:55 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:01:31 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:04:27 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:17:32 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:00:51 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 10:11:07 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | -0.009 |  |
| 2025-12-06 10:01:16 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-06 10:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2025-12-06 10:04:24 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-06 10:05:55 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2025-12-06 10:02:41 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-06 10:03:27 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.023 |  |
| 2025-12-06 10:11:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.026 |  |
| 2025-12-06 10:00:46 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.031 |  |
| 2025-12-06 10:03:10 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.040 |  |
| 2025-12-06 10:01:14 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.053 |  |
| 2025-12-06 10:05:11 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.069 |  |
| 2025-12-06 09:04:15 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.071 |  |
| 2025-12-06 10:11:13 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.071 |  |
| 2025-12-06 10:08:06 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.246 |  |
| 2025-12-06 10:03:43 | Weraganthota (Mahaweli Ganga) | -0.73 | 🟢 Normal | -0.394 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)