# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_05:04:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 05:04:17 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:04:05 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.035 |  |
| 2026-07-05 05:04:01 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-07-05 05:03:50 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-05 05:03:44 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-07-05 05:03:29 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:03:14 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 05:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.078 |  |
| 2026-07-05 05:02:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.005 |  |
| 2026-07-05 05:02:28 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-05 05:01:42 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:01:31 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -1.305 |  |
| 2026-07-05 05:00:55 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:00:52 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:00:32 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-05 05:00:25 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:00:00 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -1.305 |  |
| 2026-07-05 04:42:48 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:37:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 4.696 | 🔺 Rising |
| 2026-07-05 04:37:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 4.696 | 🔺 Rising |
| 2026-07-05 04:36:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 4.696 | 🔺 Rising |
| 2026-07-05 04:36:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 4.696 | 🔺 Rising |
| 2026-07-05 04:35:50 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.063 |  |
| 2026-07-05 04:26:22 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.043 |  |
| 2026-07-05 04:26:17 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.063 |  |
| 2026-07-05 04:24:44 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -1.305 |  |
| 2026-07-05 04:22:44 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:19:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-05 04:18:47 | Dunamale (Aththanagalu Oya) | 1.79 | 🟢 Normal | -1.305 |  |
| 2026-07-05 04:18:07 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 04:37:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 4.696 | 🔺 Rising |
| 2026-07-05 04:02:55 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-07-05 04:19:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-05 05:00:32 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-07-05 05:02:28 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-05 04:02:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-05 05:03:14 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 04:01:45 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 05:02:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.005 |  |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:00:25 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:00:55 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:00:52 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:01:42 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:04:17 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:03:29 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:05:51 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:02:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:08:16 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:05:20 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:04:17 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:22:44 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:16 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:18:07 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 04:01:10 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:13 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 05:03:50 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-07-05 03:07:40 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.019 |  |
| 2026-07-05 05:03:44 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-07-05 05:04:05 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.035 |  |
| 2026-07-05 05:04:01 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-07-05 04:26:22 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.043 |  |
| 2026-07-05 04:35:50 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.063 |  |
| 2026-07-05 05:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.078 |  |
| 2026-07-05 04:07:21 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.126 |  |
| 2026-07-05 04:03:01 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.166 |  |
| 2026-07-05 05:01:31 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -1.305 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)