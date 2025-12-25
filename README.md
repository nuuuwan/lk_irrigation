# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_13:05:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 13:05:38 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2025-12-25 13:04:50 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.033 |  |
| 2025-12-25 13:04:42 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-25 13:04:31 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-25 13:04:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-25 13:03:30 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:03:26 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:03:23 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:03:18 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.062 |  |
| 2025-12-25 13:03:13 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 13:03:05 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-25 13:02:50 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.046 |  |
| 2025-12-25 13:02:50 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:02:43 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.061 |  |
| 2025-12-25 13:02:41 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-25 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 13:02:12 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.021 |  |
| 2025-12-25 13:02:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:02:01 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:01:53 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-25 13:01:12 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 13:01:06 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:00:49 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2025-12-25 13:00:43 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.020 |  |
| 2025-12-25 13:00:07 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:00:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:21:20 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.061 |  |
| 2025-12-25 12:20:00 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:10:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-25 12:10:41 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.033 |  |
| 2025-12-25 12:10:06 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.046 |  |
| 2025-12-25 12:07:31 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 13:01:53 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-25 12:10:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-25 13:03:13 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 13:04:31 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-25 13:01:12 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 13:02:50 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:00:07 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:48 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:20:00 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:01:06 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:03:30 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:03:26 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:00:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:41 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:02:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:06:49 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:03:23 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:01:16 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:02:01 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:04:00 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:03:05 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-25 13:04:42 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-25 13:02:41 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-25 13:04:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-25 12:02:14 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-25 13:00:49 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2025-12-25 13:00:43 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.020 |  |
| 2025-12-25 13:02:12 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.021 |  |
| 2025-12-25 12:07:31 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.024 |  |
| 2025-12-25 12:02:53 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2025-12-25 13:04:50 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.033 |  |
| 2025-12-25 12:06:06 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.038 |  |
| 2025-12-25 13:02:50 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.046 |  |
| 2025-12-25 13:02:43 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.061 |  |
| 2025-12-25 12:21:20 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.061 |  |
| 2025-12-25 13:03:18 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.062 |  |
| 2025-12-25 13:05:38 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2025-12-25 12:05:13 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)