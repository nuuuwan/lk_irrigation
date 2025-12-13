# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_18:08:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,979 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 18:08:33 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.019 |  |
| 2025-12-13 18:07:46 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:06:54 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:06:19 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-13 18:05:51 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:04:42 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:04:42 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.115 |  |
| 2025-12-13 18:04:34 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2025-12-13 18:04:10 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:04:00 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:56 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-13 18:03:20 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:03:14 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:08 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:05 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-13 18:03:00 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2025-12-13 18:02:46 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 18:02:22 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.090 |  |
| 2025-12-13 18:02:10 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-13 18:02:01 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:01:57 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2025-12-13 18:01:51 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.077 |  |
| 2025-12-13 18:01:32 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:01:28 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.073 |  |
| 2025-12-13 18:01:22 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-13 18:01:22 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:01:18 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.036 |  |
| 2025-12-13 18:01:16 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:01:12 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:01:11 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:01:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-13 18:01:04 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.012 |  |
| 2025-12-13 18:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:00:24 | Horowpothana (Yan Oya) | 5.59 | 🟢 Normal | -0.050 |  |
| 2025-12-13 18:00:13 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:22:13 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.059 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 18:01:57 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2025-12-13 18:04:34 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2025-12-13 18:02:10 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-13 18:03:05 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 18:01:22 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-13 18:01:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-13 18:03:56 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-13 18:01:22 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:08 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:14 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:04:42 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:02:22 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:06:19 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:05:51 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:02:46 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:01:11 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:01:32 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:04:10 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:07:46 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:20 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:01:12 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:02:01 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:04:00 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:01:16 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:06:54 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:00:13 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-13 18:01:04 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.012 |  |
| 2025-12-13 18:08:33 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.019 |  |
| 2025-12-13 18:01:18 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.036 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-13 18:00:24 | Horowpothana (Yan Oya) | 5.59 | 🟢 Normal | -0.050 |  |
| 2025-12-13 18:03:00 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2025-12-13 18:01:28 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.073 |  |
| 2025-12-13 18:01:51 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.077 |  |
| 2025-12-13 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.090 |  |
| 2025-12-13 18:04:42 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)