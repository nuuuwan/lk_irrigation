# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_17:15:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,661 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 17:15:51 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:13:03 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.009 |  |
| 2025-12-16 17:10:32 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:10:10 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:09:41 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:09:31 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.044 |  |
| 2025-12-16 17:09:27 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:07:54 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:07:04 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.028 |  |
| 2025-12-16 17:06:23 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-16 17:05:38 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:05:06 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2025-12-16 17:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.057 |  |
| 2025-12-16 17:04:18 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | -0.104 |  |
| 2025-12-16 17:04:16 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:04:03 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:03:51 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:03:44 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:03:22 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:03:00 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:02:48 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2025-12-16 17:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:02:21 | Horowpothana (Yan Oya) | 5.83 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-16 17:02:20 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:02:13 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:02:08 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.083 |  |
| 2025-12-16 17:02:07 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:51 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:49 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:47 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:01:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-16 17:01:25 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.053 |  |
| 2025-12-16 17:01:17 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:16 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:14 | Yaka Wewa (Ma Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:14 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.014 |  |
| 2025-12-16 17:01:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 16:59:18 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 17:02:21 | Horowpothana (Yan Oya) | 5.83 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-16 17:06:23 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-16 17:01:17 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:14 | Yaka Wewa (Ma Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:49 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:10:10 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:16 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:04:03 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:04:16 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:51 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:02:07 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:01:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:05:38 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:09:41 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:03:51 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:15:51 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:03:44 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:09:27 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 17:13:03 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.009 |  |
| 2025-12-16 17:10:32 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:07:54 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:01:47 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:02:20 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:03:22 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:02:13 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-16 17:03:00 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-16 16:59:18 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.012 |  |
| 2025-12-16 17:01:14 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.014 |  |
| 2025-12-16 17:05:06 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2025-12-16 17:02:48 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2025-12-16 17:07:04 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.028 |  |
| 2025-12-16 17:01:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-16 17:09:31 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.044 |  |
| 2025-12-16 17:01:25 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.053 |  |
| 2025-12-16 17:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.057 |  |
| 2025-12-16 17:02:08 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.083 |  |
| 2025-12-16 17:04:18 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)