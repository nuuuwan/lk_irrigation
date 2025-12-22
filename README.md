# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_13:14:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,834 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 13:14:13 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2025-12-22 13:13:56 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:13:27 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2025-12-22 13:13:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:09:27 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:09:05 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:08:41 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2025-12-22 13:06:50 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:06:41 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:06:18 | Horowpothana (Yan Oya) | 3.48 | 🟢 Normal | -0.079 |  |
| 2025-12-22 13:06:04 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:05:58 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2025-12-22 13:05:41 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:05:25 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:05:24 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:03:38 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:03:36 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:03:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-22 13:03:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:02:55 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.113 |  |
| 2025-12-22 13:02:41 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:02:34 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 13:02:26 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:02:24 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2025-12-22 13:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-22 13:02:16 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-22 13:02:10 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2025-12-22 13:02:01 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:01:55 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:01:43 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:01:33 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.100 |  |
| 2025-12-22 13:01:27 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-22 13:01:17 | Thanthirimale (Malwathu Oya) | 4.60 | 🟢 Normal | -0.050 |  |
| 2025-12-22 13:01:13 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:01:06 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:00:51 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.063 |  |
| 2025-12-22 13:00:41 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 13:02:16 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-22 13:03:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-22 13:01:27 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-22 13:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-22 13:02:34 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 13:02:01 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:13:56 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:09:05 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:05:24 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:06:04 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:06:50 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:03:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:05:41 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:06:41 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:07:08 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:13:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:03:36 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 13:14:13 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2025-12-22 13:08:41 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2025-12-22 13:03:38 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:05:25 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:00:41 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:09:27 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:02:26 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:01:06 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:01:43 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:01:55 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:04:31 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:02:41 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-22 13:05:58 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2025-12-22 13:02:24 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2025-12-22 13:13:27 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2025-12-22 13:02:10 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2025-12-22 13:01:17 | Thanthirimale (Malwathu Oya) | 4.60 | 🟢 Normal | -0.050 |  |
| 2025-12-22 13:00:51 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.063 |  |
| 2025-12-22 13:06:18 | Horowpothana (Yan Oya) | 3.48 | 🟢 Normal | -0.079 |  |
| 2025-12-22 13:01:33 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.100 |  |
| 2025-12-22 13:02:55 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)