# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_04:05:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 04:05:59 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:05:55 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -4.696 |  |
| 2025-12-25 04:05:54 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 04:05:50 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 04:05:32 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -4.696 |  |
| 2025-12-25 04:05:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-25 04:05:25 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:04:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:04:39 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.048 |  |
| 2025-12-25 04:03:19 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:03:07 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:03:01 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:03:01 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.019 |  |
| 2025-12-25 04:02:58 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:02:51 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:02:41 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.214 |  |
| 2025-12-25 04:02:18 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2025-12-25 04:02:08 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:02:07 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-25 04:01:34 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-25 04:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:01:24 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:00:49 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 03:32:10 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:30:06 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-25 03:30:02 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-25 03:18:20 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:11:48 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 03:11:18 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 03:10:53 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 03:09:38 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:09:09 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-25 03:07:51 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-25 03:07:46 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 03:30:06 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-25 04:02:18 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2025-12-25 03:09:09 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-25 01:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-25 04:05:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-25 03:07:51 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-25 03:02:18 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-25 03:02:44 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 04:00:49 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 04:05:54 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 02:35:59 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-25 04:05:50 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 02:46:44 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-25 03:03:42 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 04:02:07 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-25 04:03:07 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:03:19 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:05:59 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:03:01 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:01:24 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:05:25 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:02:08 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:18:20 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:08:39 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:04:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-25 04:02:58 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:07:08 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:04:55 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:05:50 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.019 |  |
| 2025-12-25 04:03:01 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.019 |  |
| 2025-12-25 04:01:34 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 03:04:59 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.023 |  |
| 2025-12-25 04:04:39 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.048 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-25 04:02:41 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.214 |  |
| 2025-12-25 04:05:55 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)