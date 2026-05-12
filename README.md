# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_06:31:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,540 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 06:31:04 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-12 06:11:00 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 06:10:13 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:08:12 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:08:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:06:32 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.093 |  |
| 2026-05-12 06:05:47 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:05:42 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:05:22 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-12 06:05:20 | Katharagama (Menik Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-05-12 06:05:07 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-05-12 06:04:48 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 06:04:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-12 06:03:18 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -18.000 |  |
| 2026-05-12 06:03:17 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.059 |  |
| 2026-05-12 06:03:05 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.090 |  |
| 2026-05-12 06:03:01 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-12 06:02:50 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -18.000 |  |
| 2026-05-12 06:02:49 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.059 |  |
| 2026-05-12 06:02:45 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-12 06:02:44 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 06:02:32 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 06:02:26 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-12 06:02:26 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:02:22 | Hanwella (Kelani Ganga) | 2.13 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-05-12 06:02:16 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-05-12 06:02:14 | Thanamalwila (Kirindi Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-05-12 06:02:08 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:01:55 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 06:01:41 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:01:32 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.031 |  |
| 2026-05-12 06:01:25 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.051 |  |
| 2026-05-12 06:01:21 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-05-12 06:01:18 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:01:17 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 06:01:14 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-05-12 06:01:08 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.010 |  |
| 2026-05-12 06:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:00:19 | Magura (Kalu Ganga) | 2.63 | 🟢 Normal | -0.078 |  |
| 2026-05-12 06:00:09 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 06:02:22 | Hanwella (Kelani Ganga) | 2.13 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-05-12 06:02:26 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-12 06:01:55 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 06:04:48 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 06:03:01 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-12 06:01:17 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 06:02:45 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-12 06:02:32 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 06:04:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-12 06:05:22 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-12 06:31:04 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-12 06:11:00 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 06:02:44 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 06:02:26 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:05:47 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:02:08 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:05:42 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:10:13 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:08:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:00:09 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:01:41 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:08:12 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 06:01:08 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.010 |  |
| 2026-05-12 06:02:14 | Thanamalwila (Kirindi Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-05-12 06:05:07 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-05-12 06:01:21 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-05-12 06:05:20 | Katharagama (Menik Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-05-12 06:01:32 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.031 |  |
| 2026-05-12 06:02:16 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-05-12 06:01:14 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.049 |  |
| 2026-05-12 06:01:25 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.051 |  |
| 2026-05-12 06:02:49 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.059 |  |
| 2026-05-12 06:03:17 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.059 |  |
| 2026-05-12 06:00:19 | Magura (Kalu Ganga) | 2.63 | 🟢 Normal | -0.078 |  |
| 2026-05-12 06:03:05 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.090 |  |
| 2026-05-12 06:06:32 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.093 |  |
| 2026-05-12 06:03:18 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)