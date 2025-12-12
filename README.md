# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_15:17:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 15:17:10 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.076 |  |
| 2025-12-12 15:15:25 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.060 |  |
| 2025-12-12 15:10:40 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:09:35 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.065 |  |
| 2025-12-12 15:08:29 | Moragaswewa (Deduru Oya) | 1.57 | 🟢 Normal | -0.009 |  |
| 2025-12-12 15:07:12 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:07:11 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 15:06:20 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-12 15:06:08 | Manampitiya (Mahaweli Ganga) | 3.23 | 🟡 Alert | 323.234 | 🔺 Rising |
| 2025-12-12 15:06:04 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.118 |  |
| 2025-12-12 15:05:36 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:05:21 | Manampitiya (Mahaweli Ganga) | -0.99 | 🟢 Normal | 323.234 | 🔺 Rising |
| 2025-12-12 15:05:19 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 15:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.029 |  |
| 2025-12-12 15:04:29 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:04:25 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:03:54 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:03:21 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:03:19 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.019 |  |
| 2025-12-12 15:03:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-12 15:03:12 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 15:03:10 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:02:58 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:02:31 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:02:27 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2025-12-12 15:02:13 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2025-12-12 15:02:11 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:02:00 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:01:51 | Horowpothana (Yan Oya) | 6.31 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2025-12-12 15:01:48 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.049 |  |
| 2025-12-12 15:01:35 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:01:32 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-12 15:01:28 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:27 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:22 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:14 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:14 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:09 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 1.244 | 🔺 Rising |
| 2025-12-12 15:00:31 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.034 |  |
| 2025-12-12 15:00:21 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 15:06:08 | Manampitiya (Mahaweli Ganga) | 3.23 | 🟡 Alert | 323.234 | 🔺 Rising |
| 2025-12-12 15:01:51 | Horowpothana (Yan Oya) | 6.31 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2025-12-12 15:01:09 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 1.244 | 🔺 Rising |
| 2025-12-12 15:03:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-12 15:01:32 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-12 15:00:21 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 15:07:11 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 15:05:19 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 15:03:12 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 15:06:20 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-12 15:01:28 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 14:03:47 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:14 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:03:54 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:02:11 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:04:25 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:14 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:07:12 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:05:36 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:04:29 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:10:40 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:22 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:08:29 | Moragaswewa (Deduru Oya) | 1.57 | 🟢 Normal | -0.009 |  |
| 2025-12-12 15:03:21 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:01:35 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:02:31 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:02:00 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:03:10 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-12 15:02:13 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2025-12-12 15:03:19 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.019 |  |
| 2025-12-12 15:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.029 |  |
| 2025-12-12 15:00:31 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.034 |  |
| 2025-12-12 15:02:27 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2025-12-12 15:01:48 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.049 |  |
| 2025-12-12 15:15:25 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.060 |  |
| 2025-12-12 15:09:35 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.065 |  |
| 2025-12-12 15:17:10 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.076 |  |
| 2025-12-12 14:06:53 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.117 |  |
| 2025-12-12 15:06:04 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)