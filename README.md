# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_07:41:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 07:41:09 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:12:41 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:12:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-28 07:11:33 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2025-12-28 07:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.075 |  |
| 2025-12-28 07:10:01 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-28 07:08:41 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:08:40 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-28 07:08:38 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:08:19 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2025-12-28 07:07:59 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.018 |  |
| 2025-12-28 07:07:39 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-28 07:07:02 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2025-12-28 07:06:39 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:06:35 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:05:28 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.021 |  |
| 2025-12-28 07:04:18 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.005 |  |
| 2025-12-28 07:04:11 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:04:01 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-28 07:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:03:43 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.081 |  |
| 2025-12-28 07:03:32 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:03:25 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:03:14 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 07:03:12 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-28 07:03:05 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:02:41 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.011 |  |
| 2025-12-28 07:02:29 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:02:10 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:01:53 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-28 07:01:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.106 |  |
| 2025-12-28 07:01:34 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:01:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-28 07:01:18 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:00:40 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:00:22 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 07:00:13 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 07:01:53 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-28 07:04:01 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-28 07:07:39 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-28 07:12:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-28 07:03:12 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-28 07:03:14 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 07:00:22 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 07:04:18 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.005 |  |
| 2025-12-28 07:41:09 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:08:41 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:03:32 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 06:12:56 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:03:05 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:03:25 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:06:39 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:02:29 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:06:35 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:02:10 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:00:13 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:01:18 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:04:11 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:08:38 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:00:40 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:12:41 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:01:34 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 07:08:40 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-28 07:10:01 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-28 07:01:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-28 07:07:02 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2025-12-28 07:02:41 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.011 |  |
| 2025-12-28 06:01:16 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2025-12-28 07:07:59 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.018 |  |
| 2025-12-28 07:08:19 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2025-12-28 07:05:28 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.021 |  |
| 2025-12-28 07:11:33 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2025-12-28 07:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.075 |  |
| 2025-12-28 07:03:43 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.081 |  |
| 2025-12-28 07:01:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)