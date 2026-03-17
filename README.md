# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_16:27:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,946 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 16:27:10 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-17 16:21:54 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:14:23 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:08:43 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-03-17 16:08:14 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:07:55 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:07:24 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:07:23 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:06:58 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.065 |  |
| 2026-03-17 16:06:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.117 |  |
| 2026-03-17 16:06:13 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-03-17 16:06:11 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 16:05:56 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:05:00 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:04:54 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:04:50 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:04:28 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:04:26 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:04:25 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-03-17 16:04:11 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:03:25 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.058 |  |
| 2026-03-17 16:03:22 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 16:03:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:03:19 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:03:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:03:15 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:03:13 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-03-17 16:02:59 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:02:48 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:02:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:59 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:43 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-17 16:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:09 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:08 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:01:01 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:00:21 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 16:03:13 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-03-17 16:01:43 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-17 16:00:21 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-17 16:06:11 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 16:03:22 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 16:27:10 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-17 16:04:28 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:01 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:09 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:04:50 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:21:54 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:03:15 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:04:26 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:07:55 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:03:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:04:54 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:07:23 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:03:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:05:00 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:02:48 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:02:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:07:24 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:14:23 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:59 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:08:43 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-03-17 16:08:14 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:04:11 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:03:19 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:05:56 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:02:59 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:01:08 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:06:13 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-03-17 16:04:25 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-03-17 16:03:25 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.058 |  |
| 2026-03-17 16:06:58 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.065 |  |
| 2026-03-17 16:06:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)