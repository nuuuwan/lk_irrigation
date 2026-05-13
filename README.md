# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_08:22:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,509 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 08:22:23 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-05-13 08:16:17 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.661 | 🔺 Rising |
| 2026-05-13 08:14:02 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-13 08:10:41 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.081 |  |
| 2026-05-13 08:10:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-13 08:09:27 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:09:06 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-13 08:09:02 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:09:00 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-13 08:07:53 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-05-13 08:07:52 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 08:07:01 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:06:20 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 08:06:09 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:06:09 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2026-05-13 08:06:07 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:06:04 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-13 08:05:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-13 08:05:29 | Galgamuwa (Mee Oya) | 2.05 | 🟢 Normal | -0.031 |  |
| 2026-05-13 08:05:28 | Thanthirimale (Malwathu Oya) | 3.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-13 08:05:12 | Katharagama (Menik Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:04:26 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.060 |  |
| 2026-05-13 08:04:20 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-05-13 08:04:18 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:04:09 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:03:51 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-05-13 08:03:44 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-13 08:03:26 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-13 08:03:12 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:03:09 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:02:37 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.505 | 🔺 Rising |
| 2026-05-13 08:02:15 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-13 08:02:13 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:02:01 | Rathnapura (Kalu Ganga) | 4.82 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-05-13 08:01:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-13 08:00:54 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.050 |  |
| 2026-05-13 08:00:50 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:00:15 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 08:16:17 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.661 | 🔺 Rising |
| 2026-05-13 08:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.505 | 🔺 Rising |
| 2026-05-13 08:22:23 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-05-13 08:03:51 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-05-13 06:01:22 | Moragaswewa (Deduru Oya) | 1.82 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-13 08:02:01 | Rathnapura (Kalu Ganga) | 4.82 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-05-13 08:03:26 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-13 08:10:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-13 08:03:44 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-13 08:02:15 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-13 08:09:00 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-13 08:06:04 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-13 08:01:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-13 08:14:02 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-13 08:09:06 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-13 08:07:52 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 08:05:28 | Thanthirimale (Malwathu Oya) | 3.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-13 08:06:20 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 08:03:09 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:02:37 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:04:18 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:09:02 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:09:27 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:03:12 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:05:12 | Katharagama (Menik Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:07:01 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:00:50 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:06:07 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:02:13 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:06:09 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-13 08:04:20 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-05-13 08:05:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-13 08:07:53 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-05-13 08:05:29 | Galgamuwa (Mee Oya) | 2.05 | 🟢 Normal | -0.031 |  |
| 2026-05-13 08:00:15 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.044 |  |
| 2026-05-13 08:06:09 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2026-05-13 08:00:54 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.050 |  |
| 2026-05-13 08:04:26 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.060 |  |
| 2026-05-13 08:10:41 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)