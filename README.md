# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_09:51:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,268 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 09:51:55 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:48:55 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:09:02 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-05-06 09:07:55 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:07:42 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.024 |  |
| 2026-05-06 09:07:09 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.233 |  |
| 2026-05-06 09:06:29 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:06:15 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:06:09 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:06:08 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.009 |  |
| 2026-05-06 09:05:28 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-06 09:05:07 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-06 09:04:12 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-05-06 09:04:01 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-05-06 09:03:47 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.019 |  |
| 2026-05-06 09:03:21 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 09:03:02 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:59 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:53 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:32 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:30 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.044 |  |
| 2026-05-06 09:02:21 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-05-06 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.060 |  |
| 2026-05-06 09:02:11 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:03 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.034 |  |
| 2026-05-06 09:02:01 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-05-06 09:02:00 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.140 |  |
| 2026-05-06 09:01:55 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-06 09:01:52 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-06 09:01:31 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.012 |  |
| 2026-05-06 09:01:27 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-06 09:01:27 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:01:14 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-06 09:01:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:51 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:32 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:12 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 09:05:28 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-06 09:01:55 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-06 09:01:52 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-06 09:03:21 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 09:00:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:51 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:32 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:32 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:51:55 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:03:02 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:59 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:07:55 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:06:15 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:01:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:11 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:01:27 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:06:29 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:48:55 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:02:53 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:06:09 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:00:12 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-06 09:09:02 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-05-06 09:06:08 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.009 |  |
| 2026-05-06 09:02:21 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-05-06 09:05:07 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-06 09:01:27 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-06 09:01:14 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-06 09:02:01 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-05-06 09:01:31 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.012 |  |
| 2026-05-06 09:04:12 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-05-06 09:03:47 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.019 |  |
| 2026-05-06 09:07:42 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.024 |  |
| 2026-05-06 09:04:01 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-05-06 09:02:03 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.034 |  |
| 2026-05-06 09:02:30 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.044 |  |
| 2026-05-06 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.060 |  |
| 2026-05-06 09:02:00 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.140 |  |
| 2026-05-06 09:07:09 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.233 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)