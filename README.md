# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_03:16:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,471 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 03:16:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:13:51 | Kithulgala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.036 |  |
| 2026-04-05 03:09:38 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:09:29 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 1854.000 | 🔺 Rising |
| 2026-04-05 03:09:27 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | 1854.000 | 🔺 Rising |
| 2026-04-05 03:07:33 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.018 |  |
| 2026-04-05 03:06:33 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-05 03:05:59 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-05 03:05:50 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.040 |  |
| 2026-04-05 03:05:32 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:05:30 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:05:28 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:05:26 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-04-05 03:04:25 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.135 |  |
| 2026-04-05 03:03:53 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-04-05 03:03:48 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.035 |  |
| 2026-04-05 03:03:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:03:23 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-04-05 03:03:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 03:03:10 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:56 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:45 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-05 03:02:39 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-04-05 03:02:39 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-05 03:02:31 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:24 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:21 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:07 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-05 03:01:51 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-05 03:01:47 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-05 03:01:43 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-05 03:01:42 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-04-05 03:01:38 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 03:01:28 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-05 03:01:15 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.018 |  |
| 2026-04-05 03:01:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.005 |  |
| 2026-04-05 03:00:57 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-05 02:53:56 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 03:09:29 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 1854.000 | 🔺 Rising |
| 2026-04-05 03:03:23 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-04-05 03:05:26 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-04-05 03:01:28 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-05 03:02:45 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-05 03:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-05 03:02:07 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-05 03:01:38 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 03:05:59 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-05 03:01:47 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-05 03:03:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 03:01:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.005 |  |
| 2026-04-05 03:00:57 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:16:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:01:51 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:24 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:56 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:05:32 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:03:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:31 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:09:38 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:21 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:02:39 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-05 03:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-05 02:04:28 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-05 03:01:15 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.018 |  |
| 2026-04-05 03:07:33 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.018 |  |
| 2026-04-05 03:06:33 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-05 03:02:39 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-04-05 03:01:43 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-05 03:01:42 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-05 03:03:48 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.035 |  |
| 2026-04-05 03:13:51 | Kithulgala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.036 |  |
| 2026-04-05 03:05:50 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.040 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-05 03:03:53 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-04-05 03:04:25 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)