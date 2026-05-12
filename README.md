# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_07:20:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,577 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 07:20:59 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.077 |  |
| 2026-05-12 07:10:34 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.052 |  |
| 2026-05-12 07:10:31 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.043 |  |
| 2026-05-12 07:08:56 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.018 |  |
| 2026-05-12 07:08:51 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-12 07:08:37 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:08:28 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.027 |  |
| 2026-05-12 07:07:06 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-12 07:07:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-12 07:06:34 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:06:17 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | 14.286 | 🔺 Rising |
| 2026-05-12 07:06:10 | Thanthirimale (Malwathu Oya) | 3.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 07:05:04 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-12 07:04:48 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 07:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 07:04:14 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-05-12 07:04:06 | Thanamalwila (Kirindi Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-05-12 07:04:05 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:03:50 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:03:46 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.058 |  |
| 2026-05-12 07:03:43 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:03:21 | Katharagama (Menik Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-05-12 07:03:20 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.059 |  |
| 2026-05-12 07:03:02 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-05-12 07:03:01 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.029 |  |
| 2026-05-12 07:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-12 07:02:54 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:02:53 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.049 |  |
| 2026-05-12 07:02:19 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.010 |  |
| 2026-05-12 07:02:06 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.042 |  |
| 2026-05-12 07:02:05 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 14.286 | 🔺 Rising |
| 2026-05-12 07:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 07:01:54 | Wellawaya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-12 07:01:32 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-12 07:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:01:21 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:00:24 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 07:06:17 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | 14.286 | 🔺 Rising |
| 2026-05-12 07:01:32 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-12 06:02:26 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-12 07:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-12 07:07:06 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-12 06:03:01 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-12 07:05:04 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-12 07:00:24 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-12 07:07:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-12 07:08:51 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-12 06:05:22 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-12 07:04:48 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 07:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 07:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 07:06:10 | Thanthirimale (Malwathu Oya) | 3.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 07:02:54 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:06:34 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:08:37 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:04:05 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:01:21 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:03:50 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:03:43 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 07:04:06 | Thanamalwila (Kirindi Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-05-12 07:02:19 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.010 |  |
| 2026-05-12 07:01:54 | Wellawaya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-12 07:08:56 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.018 |  |
| 2026-05-12 07:03:02 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-05-12 07:08:28 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.027 |  |
| 2026-05-12 07:03:01 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.029 |  |
| 2026-05-12 07:04:14 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-05-12 07:03:21 | Katharagama (Menik Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-05-12 07:02:06 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.042 |  |
| 2026-05-12 07:10:31 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.043 |  |
| 2026-05-12 07:02:53 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.049 |  |
| 2026-05-12 07:10:34 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.052 |  |
| 2026-05-12 07:03:46 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.058 |  |
| 2026-05-12 07:03:20 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.059 |  |
| 2026-05-12 07:20:59 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)