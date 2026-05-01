# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_13:14:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,011 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 13:14:27 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:11:57 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-01 13:11:51 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:08:48 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:08:35 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:08:03 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:07:31 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.011 |  |
| 2026-05-01 13:07:24 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:07:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-05-01 13:06:56 | Weraganthota (Mahaweli Ganga) | 1.24 | 🟢 Normal | 133.017 | 🔺 Rising |
| 2026-05-01 13:06:30 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.039 |  |
| 2026-05-01 13:06:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:05:54 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-01 13:05:48 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-01 13:05:11 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 13:06:56 | Weraganthota (Mahaweli Ganga) | 1.24 | 🟢 Normal | 133.017 | 🔺 Rising |
| 2026-05-01 13:05:54 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-01 13:01:42 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-01 13:11:57 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-01 13:02:58 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-01 12:05:59 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 13:01:24 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 13:04:44 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 13:02:29 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:08:35 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:02:44 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:14:27 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:02:16 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:08:48 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:07:24 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:06:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:05:11 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:01:17 | Thanthirimale (Malwathu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:08:03 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:03:48 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:11:51 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-01 13:07:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.009 |  |
| 2026-05-01 13:05:48 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-01 13:03:14 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-01 13:02:53 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-01 13:01:27 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-05-01 13:07:31 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.011 |  |
| 2026-05-01 13:02:28 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-05-01 13:02:05 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-05-01 13:00:36 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-05-01 13:01:00 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-05-01 13:03:38 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-05-01 13:04:17 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2026-05-01 13:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.029 |  |
| 2026-05-01 13:06:30 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.039 |  |
| 2026-05-01 13:01:16 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.052 |  |
| 2026-05-01 13:04:14 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.059 |  |
| 2026-05-01 13:04:07 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)