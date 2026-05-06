# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_21:24:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,735 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 21:24:23 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:21:42 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:11:46 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-06 21:10:20 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 21:09:58 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-06 21:09:29 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-06 21:09:24 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.092 |  |
| 2026-05-06 21:09:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.059 |  |
| 2026-05-06 21:08:27 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-06 21:08:23 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:08:07 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:06:06 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-06 21:06:02 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-06 21:05:19 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-05-06 21:05:14 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 21:05:10 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.059 |  |
| 2026-05-06 21:05:07 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-06 21:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-06 21:04:44 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:04:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:03:56 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-06 21:03:39 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-06 21:03:26 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:03:20 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 21:02:53 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-06 21:02:53 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:02:49 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 21:02:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:02:26 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 21:02:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:02:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:01:49 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:01:42 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-06 21:01:09 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 21:00:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:00:45 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:00:14 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 21:01:42 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-06 21:09:58 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-06 21:06:06 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-06 21:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-06 21:11:46 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-06 21:03:56 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-06 21:03:39 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-06 21:02:53 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-06 21:03:20 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 21:06:02 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-06 21:05:14 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 21:10:20 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 21:02:49 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 21:02:26 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 21:01:09 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 21:08:23 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:00:45 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:00:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 20:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:03:26 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:02:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:02:53 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:04:44 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:01:49 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:04:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:02:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:24:23 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:21:42 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:05:07 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-06 21:08:27 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-06 21:09:29 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 21:05:19 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-05-06 21:00:14 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.046 |  |
| 2026-05-06 21:09:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.059 |  |
| 2026-05-06 21:05:10 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.059 |  |
| 2026-05-06 21:09:24 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)