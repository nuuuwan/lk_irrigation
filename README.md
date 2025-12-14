# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_21:04:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,988 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2025-12-14 20:15:35 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.013 |  |
| 2025-12-14 20:11:20 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-14 20:10:38 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 20:07:52 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.019 |  |
| 2025-12-14 20:07:09 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-14 20:06:27 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-14 20:05:58 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 20:07:09 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-14 21:03:32 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-14 20:03:34 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-14 20:34:51 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-14 20:02:19 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-14 20:05:58 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-14 20:11:20 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-14 21:01:54 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 20:04:31 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 20:06:27 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-14 20:04:06 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-14 21:02:09 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:00:42 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-14 20:31:47 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:01:20 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:03:09 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 20:02:54 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-14 20:04:12 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-14 20:02:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:04:05 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 20:03:55 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 21:02:12 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 20:03:00 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-14 21:00:14 | Horowpothana (Yan Oya) | 4.24 | 🟢 Normal | -0.010 |  |
| 2025-12-14 21:00:28 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.013 |  |
| 2025-12-14 20:07:52 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.019 |  |
| 2025-12-14 20:04:07 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2025-12-14 20:04:22 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2025-12-14 20:01:35 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.021 |  |
| 2025-12-14 20:03:23 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.024 |  |
| 2025-12-14 20:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.029 |  |
| 2025-12-14 21:02:49 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.030 |  |
| 2025-12-14 21:03:24 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2025-12-14 21:03:30 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | -0.072 |  |
| 2025-12-14 21:00:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.107 |  |
| 2025-12-14 19:56:05 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -2.182 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)