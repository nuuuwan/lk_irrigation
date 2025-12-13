# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_05:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,358 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 05:03:30 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.036 |  |
| 2025-12-14 05:02:35 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:02:33 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-14 05:02:26 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:02:16 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:02:08 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:02:01 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:55 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:41 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.062 |  |
| 2025-12-14 05:01:16 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-14 05:01:09 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:01 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-14 05:00:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 04:43:52 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 04:20:33 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 13.714 | 🔺 Rising |
| 2025-12-14 04:20:12 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 13.714 | 🔺 Rising |
| 2025-12-14 04:17:25 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-14 04:13:23 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.036 |  |
| 2025-12-14 04:12:35 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2025-12-14 04:11:36 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 04:10:18 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.057 |  |
| 2025-12-14 04:08:30 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.067 |  |
| 2025-12-14 04:07:55 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2025-12-14 04:07:44 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.018 |  |
| 2025-12-14 04:07:03 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 04:06:24 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-14 04:06:17 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-14 04:06:01 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 04:20:33 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 13.714 | 🔺 Rising |
| 2025-12-14 04:07:55 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2025-12-14 04:12:35 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2025-12-14 05:01:16 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-14 04:06:24 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-14 05:01:01 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-14 04:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-14 04:06:17 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-14 04:07:03 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 05:02:33 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-14 04:11:36 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 05:02:26 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-14 04:02:47 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:02:16 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:41 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 04:02:30 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:00:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 04:04:33 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:09 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 04:06:01 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:02:01 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:55 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:05:25 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:02:35 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:02:08 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-14 03:10:46 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.018 |  |
| 2025-12-14 04:07:44 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.018 |  |
| 2025-12-14 04:02:23 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2025-12-14 05:03:30 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.036 |  |
| 2025-12-14 04:04:29 | Horowpothana (Yan Oya) | 5.08 | 🟢 Normal | -0.039 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-14 04:01:52 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.054 |  |
| 2025-12-14 04:10:18 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.057 |  |
| 2025-12-14 05:01:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.062 |  |
| 2025-12-14 04:08:30 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.067 |  |
| 2025-12-14 04:03:49 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -5.538 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)