# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_23:29:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,367 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 23:29:48 | Urawa (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.015 |  |
| 2025-12-11 23:26:55 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2025-12-11 23:25:22 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-11 23:07:58 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | -0.074 |  |
| 2025-12-11 23:06:39 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.009 |  |
| 2025-12-11 23:05:49 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:05:45 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 23:05:34 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-11 23:05:10 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.566 | 🔺 Rising |
| 2025-12-11 23:05:06 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.054 |  |
| 2025-12-11 23:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 23:04:26 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-11 23:03:56 | Horowpothana (Yan Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:03:53 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 23:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-11 23:03:28 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.019 |  |
| 2025-12-11 23:03:19 | Padiyathalawa (Maduru Oya) | 3.40 | 🟢 Normal | -0.050 |  |
| 2025-12-11 23:03:14 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-11 23:02:57 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-11 23:02:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:02:39 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 23:02:23 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.048 |  |
| 2025-12-11 23:02:17 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-11 23:02:06 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:01:43 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-11 23:01:43 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:01:37 | Siyambalanduwa (Heda Oya) | 1.59 | 🟢 Normal | -0.042 |  |
| 2025-12-11 23:01:09 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-11 23:01:08 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-11 23:00:55 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.042 |  |
| 2025-12-11 22:49:48 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.048 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 23:05:10 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.566 | 🔺 Rising |
| 2025-12-11 23:02:57 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 23:26:55 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2025-12-11 23:05:34 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-11 23:01:09 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-11 23:25:22 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-11 23:02:17 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-11 23:01:43 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-11 23:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-11 23:05:45 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:01:23 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 23:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 23:02:39 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 23:03:53 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 23:01:43 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:03:56 | Horowpothana (Yan Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:02:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:02:06 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:05:49 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:06:39 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.009 |  |
| 2025-12-11 23:03:14 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-11 22:01:26 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.010 |  |
| 2025-12-11 23:04:26 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-11 23:01:08 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-11 23:29:48 | Urawa (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.015 |  |
| 2025-12-11 23:03:28 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.019 |  |
| 2025-12-11 22:05:49 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-11 23:00:55 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.042 |  |
| 2025-12-11 23:01:37 | Siyambalanduwa (Heda Oya) | 1.59 | 🟢 Normal | -0.042 |  |
| 2025-12-11 23:02:23 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.048 |  |
| 2025-12-11 23:03:19 | Padiyathalawa (Maduru Oya) | 3.40 | 🟢 Normal | -0.050 |  |
| 2025-12-11 23:05:06 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.054 |  |
| 2025-12-11 23:07:58 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | -0.074 |  |
| 2025-12-11 22:07:16 | Thaldena (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)