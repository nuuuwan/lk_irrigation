# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_07:21:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,723 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 07:21:03 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:18:30 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:15:06 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:14:48 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.002 |  |
| 2025-12-30 07:14:46 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2025-12-30 07:12:46 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:12:32 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:12:13 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:10:59 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:10:46 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.164 |  |
| 2025-12-30 07:10:15 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.027 |  |
| 2025-12-30 07:09:01 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:08:01 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:07:52 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2025-12-30 07:07:26 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:06:45 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:06:27 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-30 07:06:11 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:05:36 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:05:15 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-30 07:04:48 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:04:16 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.022 |  |
| 2025-12-30 07:03:38 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:03:28 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:03:23 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.001 |  |
| 2025-12-30 07:03:08 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:02:40 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:02:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-30 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.107 |  |
| 2025-12-30 07:02:12 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.066 |  |
| 2025-12-30 07:01:56 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:01:53 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-30 07:01:48 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2025-12-30 07:01:33 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:01:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:00:36 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:00:34 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:35:18 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:31:37 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 07:02:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-30 07:01:53 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-30 07:14:48 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.002 |  |
| 2025-12-30 07:03:23 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.001 |  |
| 2025-12-30 07:01:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:01:56 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:00:34 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:08:01 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:01:33 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:18:30 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:06:11 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:12:46 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:06:45 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:12:32 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:03:28 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:03:08 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:05:36 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:15:06 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:04:48 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:03:38 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:07:26 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:10:59 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:12:57 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:00:36 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:21:03 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:12:13 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:09:01 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:02:40 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 07:05:15 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-30 07:06:27 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-30 07:14:46 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2025-12-30 07:07:52 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2025-12-30 07:01:48 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2025-12-30 07:04:16 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.022 |  |
| 2025-12-30 07:10:15 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.027 |  |
| 2025-12-30 07:02:12 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.066 |  |
| 2025-12-30 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.107 |  |
| 2025-12-30 07:10:46 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)